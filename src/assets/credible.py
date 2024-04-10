from assets.pivotdash import pivot_df
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from assets.calcpre import df_credibility, mainDiffBar, percentageDiffBar, compareBar, communication, competence, integrity


df = pd.read_csv('Test.csv')

df['nonPositive']=df['Neutral']+df['Negative']
credfilter_df = df[df['Dimension'] == 'Credibiity']  # Note the typo correction from 'Credibility' to 'Credibiity'
data = credfilter_df.drop(['Neutral', 'Negative'], axis=1)
data = data.sort_values(by='nonPositive', ascending=False)

#OVERVIEW OF POSNEGS
# Create a bar chart using Plotly Express
filtered_data = data[data['nonPositive'] > 15]
figcred = px.bar(filtered_data, x='TrustIndexStatement', y='nonPositive', color='SubDimension',text_auto='.2s',
             
             color_discrete_sequence=['#007FFF','#4FFFB0','#FFC72C'],
             )
figcred.update_layout(height=800,xaxis_title='', yaxis_title='Non-Positive Scores',xaxis_tickangle=90,plot_bgcolor='white',showlegend=True,legend_orientation='h',legend=dict(x=-0.2, y=1.5))

# Create a bar chart using Plotly Express
psodata = data.sort_values(by='Positive', ascending=False)
pfiltered_data = psodata[psodata['Positive'] >= 85]
pfigcred = px.bar(pfiltered_data, x='TrustIndexStatement', y='Positive', color='SubDimension',text_auto='.2s',
             
             color_discrete_sequence=['#007FFF','#4FFFB0'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Positive': 'Positive Score'})
pfigcred.update_layout(plot_bgcolor='white')
# Show the plot

cred_selected_columns = [
    'Management keeps me informed about important issues and changes.',
    'Management makes its expectations clear.',
    'I can ask management any reasonable question and get a straight answer.',
    'Management is approachable, easy to talk with.',
    'Management is competent at running the business.',
    'Management hires people who fit in well here.',
    'Management does a good job of assigning and coordinating people.',
    'Management trusts people to do a good job without watching over their shoulders.',
    'People here are given a lot of responsibility.',
    'Management has a clear view of where the organization is going and how to get there.',
    'Management delivers on its promises.',
    "Management's actions match its words.",
    'I believe management would lay people off only as a last resort.',
    'Management is honest and ethical in its business practices.',
    'Our executives fully embody the best characteristics of our company.'
]




credibility_pivot = pivot_df.loc[:, cred_selected_columns]


# Create dropdown options for sections and columns
sections_options = [{'label': section, 'value': section} for section in credibility_pivot.index.get_level_values('Section').unique()]
columns_options = [{'label': column, 'value': column} for column in credibility_pivot.columns]


# Define app layout
cred_layout = html.Div([
    html.H2("C R E D I B I L I T Y", className = "mt-4", style={"color":"#007FFF", "margin-bottom":"2rem"}),
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        dbc.Col([
            html.H4("Indexes with Most Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            dcc.Graph(id='cred-graph', figure=figcred),

        ], width=6),
        dbc.Col([
            html.H4("Demography-Wise Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            html.Label('Select Demography', style={"color":"#007FFF"}),
            html.Br(),
            dcc.Dropdown(
                id='credsection-dropdown',
                options=sections_options,
                value=sections_options[0]['value']
            ),
            
            html.Label('Select Index Statements', style={"color":"#007FFF"}),
            dcc.Dropdown(
                id='credcolumn-dropdown',
                options=columns_options,
                value=columns_options[0]['value']
            ),
            html.Br(),
            dcc.Graph(id='credbar-chart', style={"margin-bottom":"3rem"}),
            html.Br(),
            html.Div(id='credreport-card'),
                ], width=6, ),
    ],),

    
    
    dbc.Row([
        html.H4("Indexes with Most Positive Scores", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=pfigcred),
    ]),
    
    
   
    
    html.H4("DIFFERENCE OF OUR SCORES FROM THE BENCHMARK SCORES (in %)", style={"color":"#007FFF","margin-top":"3rem"}),
    html.Hr( style={"color":"#007FFF"}),
    dcc.Graph(figure=mainDiffBar(df_credibility)),
    html.Hr( style={"color":"#007FFF"}),
    
    html.H4("COMPARISON OF INDEX STATEMENTS WITH BENCHMARK SCORES DIMENSION WISE", style={"color":"#007FFF","margin-top":"3rem"}),
    dbc.Row([
        html.H4("Communication", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col([

            dcc.Graph(figure=percentageDiffBar(communication))], width=6),
        dbc.Col(dcc.Graph(figure=compareBar(communication)), width=6),
    ], className = "mb-5"),
    
    dbc.Row([
        
        html.H4("Competence", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(competence)), width=6),
        dbc.Col(dcc.Graph(figure=compareBar(competence)), width=6),
        
    ], className = "mb-5"),
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        html.H4("Integrity", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(integrity)), width=6),
        dbc.Col(dcc.Graph(figure=compareBar(integrity)), width=6),
    ], className = "mb-5"),
    
    
    
    
    
    
])
