#import dash boilerplate
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from assets.layout import layout
from assets.respect import res_layout, res_pivot
from assets.credible import cred_layout, credibility_pivot
from assets.fair import fair_layout, fairness_pivot
from assets.pride import pride_layout, pride_pivot
import plotly.graph_objs as go
from assets.cama import cama_layout, camaraderie_pivot

app = Dash(__name__, external_stylesheets=[dbc.themes.LUMEN], suppress_callback_exceptions=True,
           meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],)
server = app.server


app.layout = layout
app.title = "NK Dashboard"
#Navigation Bar
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return cred_layout
    elif pathname == "/page-1":
        return res_layout
    elif pathname == "/page-2":
        return fair_layout
    elif pathname == "/page-3":
        return pride_layout
    elif pathname == "/page-4":
        return cama_layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )






#CREDIBILITY MAIN VIZ
# Define callback to update bar chart and report card
@app.callback(
    [Output('credbar-chart', 'figure'),
     Output('credreport-card', 'children')],
    [Input('credsection-dropdown', 'value'),
     Input('credcolumn-dropdown', 'value')]
)
def update_credibilitybar_chart(section, column):
    filtered_df = credibility_pivot.loc[section]
    sorted_df = filtered_df.sort_values(by=column)
    
    # Color the bars red if value is under 80
    colors = ['#fd5c63' if val < 80 else '#007FFF' for val in sorted_df[column]]
    
    data = [go.Bar(
        x=sorted_df.index.get_level_values('Parameters'),
        y=sorted_df[column],
        text =sorted_df[column],
        marker=dict(color=colors)
    )]
    
    min_val = sorted_df[column].min()
    min_param = sorted_df[sorted_df[column] == min_val].index.get_level_values('Parameters').values[0]
    
    report_text = html.Div([
        html.H6(f"{min_param}", style={"font-size":"16","padding-left":"4rem","align":"center",'color':'#007FFF'}),
        html.Div([
            html.P(f"Has the least score in the {section} for {column} with a value of {min_val}",style={"font-weight":"400","font-size":"10",'color':'#007FFF',"padding-left":"4rem","align":"center"}),
            
        ],style={"display":"flex","font-size":"10","align":"center"}),
        
        
    ] ,style={"margin-top":"1rem","":""})
    #html.P(f"{min_param} has the least score in {section} for {column} with a value of {min_val}.", style={"font-size":"12"})
    
    layout = go.Layout(
        
        xaxis=dict(title=None, tickangle=20),
        yaxis=dict(title=None),
        
    )

    return {'data': data, 'layout': layout}, report_text



#RESPECT MAIN CALLBACK
# Define callback to update bar chart and report card
@app.callback(
    [Output('resbar-chart', 'figure'),
     Output('resreport-card', 'children')],
    [Input('ressection-dropdown', 'value'),
     Input('rescolumn-dropdown', 'value')]
)
def update_respectbar_chart(section, column):
    filtered_df = res_pivot.loc[section]
    sorted_df = filtered_df.sort_values(by=column)
    
    # Color the bars red if value is under 80
    colors = ['#fd5c63' if val < 80 else '#007FFF' for val in sorted_df[column]]
    
    data = [go.Bar(
        x=sorted_df.index.get_level_values('Parameters'),
        y=sorted_df[column],
        text =sorted_df[column],
        marker=dict(color=colors)
    )]
    
    min_val = sorted_df[column].min()
    min_param = sorted_df[sorted_df[column] == min_val].index.get_level_values('Parameters').values[0]
    
    report_text = html.Div([
        html.H6(f"{min_param}", style={"font-size":"16","padding-left":"4rem","align":"center",'color':'#007FFF'}),
        html.Div([
            html.P(f"Has the least score in the {section} for {column} with a value of {min_val}",style={"font-weight":"400","font-size":"10",'color':'#007FFF',"padding-left":"4rem","align":"center"}),
            
        ],style={"display":"flex","font-size":"10","align":"center"}),
        
        
    ] ,style={"margin-top":"1rem","":""})
    
    layout = go.Layout(
        
        xaxis=dict(title=None, tickangle=20),
        yaxis=dict(title=None),
        
    )

    return {'data': data, 'layout': layout}, report_text

#FAIRNESS MAIN CALLBACK

@app.callback(
    [Output('fairness-bar-chart', 'figure'),
     Output('fairness-report-card', 'children')],
    [Input('fairness-section-dropdown', 'value'),
     Input('fairness-column-dropdown', 'value')]
)
def update_fairness_bar_chart(section, column):
    filtered_df = fairness_pivot.loc[section]
    sorted_df = filtered_df.sort_values(by=column)
    
    # Color the bars red if value is under 80
    colors = ['#fd5c63' if val < 80 else '#007FFF' for val in sorted_df[column]]
    
    data = [go.Bar(
        x=sorted_df.index.get_level_values('Parameters'),
        y=sorted_df[column],
        text =sorted_df[column],
        marker=dict(color=colors)
    )]
    
    min_val = sorted_df[column].min()
    min_param = sorted_df[sorted_df[column] == min_val].index.get_level_values('Parameters').values[0]
    
    report_text = html.Div([
        html.H6(f"{min_param}", style={"font-size":"16","padding-left":"4rem","align":"center",'color':'#007FFF'}),
        html.Div([
            html.P(f"Has the least score in the {section} for {column} with a value of {min_val}",style={"font-weight":"400","font-size":"10",'color':'#007FFF',"padding-left":"4rem","align":"center"}),
            
        ],style={"display":"flex","font-size":"10","align":"center"}),
        
        
    ] ,style={"margin-top":"1rem","":""})
    
    layout = go.Layout(
        
        xaxis=dict(title=None, tickangle=20),
        yaxis=dict(title=None),
        
    )

    return {'data': data, 'layout': layout}, report_text


#PRIDE MAIN CALLBACK
# Define callback to update bar chart and report card
@app.callback(
    [Output('pride-bar-chart', 'figure'),
     Output('pride-report-card', 'children')],
    [Input('pride-section-dropdown', 'value'),
     Input('pride-column-dropdown', 'value')]
)
def update_pride_bar_chart(section, column):
    filtered_df = pride_pivot.loc[section]
    sorted_df = filtered_df.sort_values(by=column)
    
    # Color the bars red if value is under 80
    colors = ['#fd5c63' if val < 80 else '#007FFF' for val in sorted_df[column]]
    
    data = [go.Bar(
        x=sorted_df.index.get_level_values('Parameters'),
        y=sorted_df[column],
        text =sorted_df[column],
        marker=dict(color=colors)
    )]
    
    min_val = sorted_df[column].min()
    min_param = sorted_df[sorted_df[column] == min_val].index.get_level_values('Parameters').values[0]
    
    report_text = html.Div([
        html.H6(f"{min_param}", style={"font-size":"16","padding-left":"4rem","align":"center",'color':'#007FFF'}),
        html.Div([
            html.P(f"Has the least score in the {section} for {column} with a value of {min_val}",style={"font-weight":"400","font-size":"10",'color':'#007FFF',"padding-left":"4rem","align":"center"}),
            
        ],style={"display":"flex","font-size":"10","align":"center"}),
        
        
    ] ,style={"margin-top":"1rem","":""})
    
    layout = go.Layout(
        
        xaxis=dict(title=None, tickangle=20),
        yaxis=dict(title=None),
        
    )

    return {'data': data, 'layout': layout}, report_text


#CAMARADERIE MAIN CALLBACK
@app.callback(
    [Output('camaraderie-bar-chart', 'figure'),
     Output('camaraderie-report-card', 'children')],
    [Input('camaraderie-section-dropdown', 'value'),
     Input('camaraderie-column-dropdown', 'value')]
)
def update_camaraderie_bar_chart(section, column):
    filtered_df = camaraderie_pivot.loc[section]
    sorted_df = filtered_df.sort_values(by=column)
    
    # Color the bars red if value is under 80
    colors = ['#fd5c63' if val < 80 else '#007FFF' for val in sorted_df[column]]
    
    data = [go.Bar(
        x=sorted_df.index.get_level_values('Parameters'),
        y=sorted_df[column],
        text =sorted_df[column],
        marker=dict(color=colors)
    )]
    
    min_val = sorted_df[column].min()
    min_param = sorted_df[sorted_df[column] == min_val].index.get_level_values('Parameters').values[0]
    
    report_text = html.Div([
        html.H6(f"{min_param}", style={"font-size":"16","padding-left":"4rem","align":"center",'color':'#007FFF'}),
        html.Div([
            html.P(f"Has the least score in the {section} for {column} with a value of {min_val}",style={"font-weight":"400","font-size":"10",'color':'#007FFF',"padding-left":"4rem","align":"center"}),
            
        ],style={"display":"flex","font-size":"10","align":"center"}),
        
        
    ] ,style={"margin-top":"1rem","":""})
    
    layout = go.Layout(
        
        xaxis=dict(title=None, tickangle=20),
        yaxis=dict(title=None),
        
    )

    return {'data': data, 'layout': layout}, report_text





@app.callback(
    [Output('cred-link', 'style'),
     Output('respect-link', 'style'),
     Output('fairness-link', 'style'),
     Output('pride-link', 'style'),
     Output('camaraderie-link', 'style')],
    [Input('url', 'pathname')]
)
def update_nav_links(pathname):
    default_style = {"color": "#007FFF"}
    active_style = {"color": "white", "background-color": "#007FFF"}

    styles = [default_style] * 5
    if pathname == "/":
        styles[0] = active_style
    elif pathname == "/page-1":
        styles[1] = active_style
    elif pathname == "/page-2":
        styles[2] = active_style
    elif pathname == "/page-3":
        styles[3] = active_style
    elif pathname == "/page-4":
        styles[4] = active_style

    return styles

# Run the app

if __name__ == '__main__':
    app.run_server(port=1995)