from assets.pivotdash import pivot_df
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from assets.calcpre import mainDiffBar, compareBar, percentageDiffBar, df_camaraderie, intimacy, hospitality, community


df = pd.read_csv('Test.csv')

df['nonPositive']=df['Neutral']+df['Negative']
cama_df = df[df['Dimension'] == 'Camaraderie']
data = cama_df.drop(['Neutral', 'Negative'], axis=1)
data = data.sort_values(by='nonPositive', ascending=False)
# Create a bar chart using Plotly Express
filtered_data = data[data['nonPositive'] > 15]
figcama = px.bar(filtered_data, x='TrustIndexStatement', y='nonPositive', color='SubDimension',text_auto='.2s',
             
             color_discrete_sequence=['#007FFF','#4FFFB0','#FFC72C'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Non-Positive': 'Non Positive Score'})
figcama.update_layout(height=800,xaxis_title='', yaxis_title='Non-Positive Scores',xaxis_tickangle=90,plot_bgcolor='white',showlegend=True,legend_orientation='h',legend=dict(x=-0.2, y=1.5))

# Create a bar chart using Plotly Express
psodata = data.sort_values(by='Positive', ascending=False)
pfiltered_data = psodata[psodata['Positive'] >= 85]
pfigcama = px.bar(pfiltered_data, x='TrustIndexStatement', y='Positive', color='SubDimension',text_auto='.2s',
             title='TrustIndexStatement vs Positive (Sorted by Most Positive)',
             color_discrete_sequence=['#007FFF','#4FFFB0','#FFC72C'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Positive': 'Positive Score'})

pfigcama.update_layout(plot_bgcolor='white')

# Specified column names for camaraderie
camaraderie_selected_columns = [
    "I can be myself around here.",
    "People celebrate special events around here.",
    "People care about each other here.",
    "This is a fun place to work.",
    "When you join the organization, you are made to feel welcome.",
    "When people change jobs or work units, they are made to feel right at home.",
    "You can count on people to cooperate."
]

# Creating camaraderie_pivot DataFrame
camaraderie_pivot = pivot_df.loc[:, camaraderie_selected_columns]


# Create dropdown options for sections and columns
sections_options = [{'label': section, 'value': section} for section in camaraderie_pivot.index.get_level_values('Section').unique()]
columns_options = [{'label': column, 'value': column} for column in camaraderie_pivot.columns]

# Define app layout
cama_layout = html.Div([
    html.H2("C A M A R A D E R I E", className = "mt-4", style={"color":"#007FFF", "margin-bottom":"2rem"}),
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        dbc.Col([
            html.H4("Indexes with Most Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            dcc.Graph(figure=figcama),
        ],  width=6),
        dbc.Col([
            html.H4("Demography-Wise Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            html.Label('Select Demography', style={"color":"#007FFF"}),
            html.Br(),
            dcc.Dropdown(
                id='camaraderie-section-dropdown',
                options=sections_options,
                value=sections_options[0]['value']
            ),
            html.Label('Index Statements',style={"color":"#007FFF"}),
            dcc.Dropdown(
                id='camaraderie-column-dropdown',
                options=columns_options,
                value=columns_options[0]['value']
            ),
            dcc.Graph(id='camaraderie-bar-chart'),
            html.Div(id='camaraderie-report-card'),
                ],  width=6),
    ],className = "mb-5"),

    dbc.Row([
        html.H4("Indexes with Most Positive Scores", style={"color":"#007FFF","margin-top":"2rem"}),
        dcc.Graph(figure=pfigcama),
    ]),
    
    
    
    dbc.Row([
        html.H4("Difference of Our Scores from Benchmark Scores (in %)", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=mainDiffBar(df_camaraderie)),
        
    ]),
    html.H4("COMPARISON OF INDEX STATEMENTS WITH BENCHMARK SCORES DIMENSION WISE", style={"color":"#007FFF","margin-top":"3rem"}),
    
    dbc.Row([
        html.H4("Intimacy", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(intimacy)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(intimacy)),  width=6),
        
    ],className = "mb-5"),
    dbc.Row([
        html.H4("Hospitality", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(hospitality)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(hospitality)),  width=6),
        
    ],className = "mb-5"),
    dbc.Row([
        html.H4("Community", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(community)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(community)),  width=6),
        
    ],className = "mb-5"),
    
    
    
    
    
    
])