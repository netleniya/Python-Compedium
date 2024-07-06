import pathlib

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback

from styles import SIDEBAR_STYLE, CONTENT_STYLE


def get_data() -> pd.DataFrame:
    root_dir = pathlib.Path(__file__).parent.resolve()
    file = root_dir / "intro_bees.csv"
    df = pd.read_csv(file)

    df = (
        df.groupby(["State", "ANSI", "Affected by", "Year", "state_code"])[
            ["Pct of Colonies Impacted"]
        ]
        .mean()
        .reset_index()
    )
    return df


data = get_data()

app = Dash(__name__)

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("Select Year", className="lead"),
        dcc.Dropdown(
            id="select_year",
            options=[{"label": i, "value": i} for i in data["Year"].unique()],
            multi=False,
            value=data["Year"].min(),
        ),
        html.Br(),
        html.P("Select Disease", className="lead"),
        dcc.Dropdown(
            id="select_disease",
            options=[{"label": i, "value": i} for i in data["Affected by"].unique()],
            multi=False,
            value=data["Affected by"].min(),
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
    [
        html.H1("US Bee Colonies Impacted by Disease and Pests", className="display-3"),
        html.Div(id="output_container", children=[]),
        dcc.Graph(id="bee_map", figure={}),
    ],
    style=CONTENT_STYLE,
)

app.layout = html.Div([sidebar, content])


@callback(
    [
        Output(component_id="output_container", component_property="children"),
        Output(component_id="bee_map", component_property="figure"),
    ],
    [
        Input(component_id="select_year", component_property="value"),
        Input(component_id="select_disease", component_property="value"),
    ],
)
def update_map(year, disease):

    container = html.P(f"Bee Colonies affected by {disease} in {year}")

    df = data.copy()
    fig = px.choropleth(
        data_frame=df[(df["Year"] == year) & (df["Affected by"] == disease)],
        locationmode="USA-states",
        locations="state_code",
        scope="usa",
        color="Pct of Colonies Impacted",
        hover_name="State",
        hover_data=["Pct of Colonies Impacted"],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={"Pct of Colonies Impacted": "% Colonies Impacted"},
    )

    fig.update_layout(showlegend=False)

    return container, fig


if __name__ == "__main__":
    app.run_server(debug=True)
