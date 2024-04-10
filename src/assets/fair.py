from assets.pivotdash import pivot_df
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from assets.calcpre import df_fairness, equity, impartiality, justice, mainDiffBar, percentageDiffBar, compareBar


df = pd.read_csv('Test.csv')

df['nonPositive']=df['Neutral']+df['Negative']
fair_df = df[df['Dimension'] == 'Fairness']  # Note the typo correction from 'Credibility' to 'Credibiity'

data = fair_df.drop(['Neutral', 'Negative'], axis=1)
data = data.sort_values(by='nonPositive', ascending=False)
# Create a bar chart using Plotly Express
filtered_data = data[data['nonPositive'] > 15]
figfair = px.bar(filtered_data, x='TrustIndexStatement', y='nonPositive', color='SubDimension',text_auto='.2s',
             
             color_discrete_sequence=['#007FFF','#4FFFB0','#FFC72C'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Non-Positive': 'Non Positive Score'})
figfair.update_layout(height=800,xaxis_title='', yaxis_title='Non-Positive Scores',xaxis_tickangle=90,plot_bgcolor='white',showlegend=True, legend_orientation='h', legend=dict(x=-0.2, y=1.5))

# Show the plot
# Create a bar chart using Plotly Express
psodata = data.sort_values(by='Positive', ascending=False)
pfiltered_data = psodata[psodata['Positive'] >= 85]
pfigfair = px.bar(pfiltered_data, x='TrustIndexStatement', y='Positive', color='SubDimension',text_auto='.2s',
             title='TrustIndexStatement vs Positive (Sorted by Most Positive)',
             color_discrete_sequence=['#007FFF','#4FFFB0'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Positive': 'Positive Score'})


pfigfair.update_layout(plot_bgcolor='white')



fairness_selected_columns = [
    'People here are paid fairly for the work they do.',
    'I feel I receive a fair share of the profits made by this organization.',
    'Everyone has an opportunity to get special recognition.',
    'I am treated as a full member here regardless of my position.',
    'Promotions go to those who best deserve them.',
    'Managers avoid playing favourites.',
    'People avoid politicking and backstabbing as ways to get things done.',
    'People here are treated fairly regardless of their age.',
    'People here are treated fairly regardless of their race or caste.',
    'People here are treated fairly regardless of their gender.',
    'If I am unfairly treated, I believe I\'ll be given a fair hearing if I appeal.',
    'People here are treated fairly regardless of their sexual orientation.'
]

fairness_pivot = pivot_df.loc[:, fairness_selected_columns]


# Create dropdown options for sections and columns
sections_options = [{'label': section, 'value': section} for section in fairness_pivot.index.get_level_values('Section').unique()]
columns_options = [{'label': column, 'value': column} for column in fairness_pivot.columns]

# Calculate minimum values for each column
min_values = fairness_pivot.min()

# Define app layout
fair_layout = html.Div([
    html.H2('F A I R N E S S', className = "mt-4", style={"color":"#007FFF", "margin-bottom":"2rem"}),
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        dbc.Col([
            html.H4("Indexes with Most Non-Positive Scores", style={"color":"#007FFF"}),
            
            html.Hr( style={"color":"#007FFF"}),
            dcc.Graph(figure=figfair),
        ], width=6),
        dbc.Col([
            html.H4("Demography-Wise Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            html.Label('Select Demography', style={"color":"#007FFF"}),
            html.Br(),
            dcc.Dropdown(
                id='fairness-section-dropdown',
                options=sections_options,
                value=sections_options[0]['value']
            ),
            html.Label('Index Statements', style={"color":"#007FFF"}),
            dcc.Dropdown(
                id='fairness-column-dropdown',
                options=columns_options,
                value=columns_options[0]['value']
            ),
            dcc.Graph(id='fairness-bar-chart'),
            html.Div(id='fairness-report-card'),
        ],width=6)
    ],className = "mb-5"),
    
    dbc.Row([
        html.H4("Indexes with Most Positive Scores", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=pfigfair),
        
    ]),
    
    
    
    dbc.Row([
        html.H4("Difference of Our Scores from Benchmark Scores (in %)", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=mainDiffBar(df_fairness)),
    ]),
    html.H4("COMPARISON OF INDEX STATEMENTS WITH BENCHMARK SCORES DIMENSION WISE", style={"color":"#007FFF","margin-top":"3rem"}),
    dbc.Row([
        html.H4("Equity", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(equity)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(equity)), width=6),
        
    ],className = "mb-5"),
    dbc.Row([
        html.H4("Impartiality", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(impartiality)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(impartiality)),  width=6),
        
    ],className = "mb-5"),
    dbc.Row([
        html.H4("Justice", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(justice)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(justice)),  width=6),
        
    ],className = "mb-5"),
    
    
    
    
    
    
])
