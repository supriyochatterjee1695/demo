import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import dcc, html, Dash




app = Dash(external_stylesheets=[dbc.themes.LUMEN])

sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Sidebar", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)



# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


CONTENT_STYLE = {
    "margin-left": "17rem",
    "margin-right": "1rem",
    #"padding": "1rem 1rem",
}




sidebar = html.Div(
    [
        html.H2("Aidias InSights", className="display-4", style={"color":"#007FFF"}),
        html.Hr( style={"color":"#007FFF"}),
        html.P(
            "N K Realtors Great Place to Work Analysis", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Credibility", href="/", active="exact", id="cred-link"),
                dbc.NavLink("Respect", href="/page-1", active="exact", id="respect-link"),
                dbc.NavLink("Fairness", href="/page-2", active="exact", id="fairness-link"),
                dbc.NavLink("Pride", href="/page-3", active="exact", id="pride-link"),
                dbc.NavLink("Camaraderie", href="/page-4", active="exact", id="camaraderie-link"),
            ],
            vertical=True,
            pills=True,
            
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)


layout = html.Div([dcc.Location(id="url"), sidebar, content])



