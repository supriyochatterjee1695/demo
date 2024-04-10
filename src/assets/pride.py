from assets.pivotdash import pivot_df
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from assets.calcpre import df_pride, personal, team, c_image, mainDiffBar, percentageDiffBar, compareBar

df = pd.read_csv('Test.csv')

df['nonPositive']=df['Neutral']+df['Negative']
pride_df = df[df['Dimension'] == 'Pride']
data = pride_df.drop(['Neutral', 'Negative'], axis=1)
data = data.sort_values(by='nonPositive', ascending=False)
# Create a bar chart using Plotly Express
filtered_data = data[data['nonPositive'] > 15]
figpride = px.bar(filtered_data, x='TrustIndexStatement', y='nonPositive', color='SubDimension',text_auto='.2s',
             
             color_discrete_sequence=['#007FFF','#4FFFB0','#FFC72C'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Non-Positive': 'Non Positive Score'})
figpride.update_layout(height=800,xaxis_title='', yaxis_title='Non-Positive Scores',xaxis_tickangle=90,plot_bgcolor='white',showlegend=True,legend_orientation='h',legend=dict(x=-0.2, y=1.5))

# Show the plot
# Create a bar chart using Plotly Express
psodata = data.sort_values(by='Positive', ascending=False)
pfiltered_data = psodata[psodata['Positive'] >= 85]
pfigpride = px.bar(pfiltered_data, x='TrustIndexStatement', y='Positive', color='SubDimension',text_auto='.2s',
             title='TrustIndexStatement vs Positive (Sorted by Most Positive)',
             color_discrete_sequence=['#007FFF','#4FFFB0'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Positive': 'Positive Score'})

pfigpride.update_layout(plot_bgcolor='white')

# Selecting specified columns from pivot_df to create pride_pivot
pride_selected_columns = [
    "I feel I make a difference here.",
    "My work has special meaning: this is not 'just a job'.",
    "When I look at what we accomplish, I feel a sense of pride.",
    "People here are willing to put in extra effort to get the job done.",
    "People here quickly adapt to changes needed for our organization’s success.",
    "I want to work here for a long time.",
    "I'm proud to tell others I work here.",
    "People look forward to coming to work here.",
    
    "I would strongly endorse my company to friends and family as a great place to work.",]
    

pride_pivot = pivot_df.loc[:, pride_selected_columns]



# Create dropdown options for sections and columns
sections_options = [{'label': section, 'value': section} for section in pride_pivot.index.get_level_values('Section').unique()]
columns_options = [{'label': column, 'value': column} for column in pride_pivot.columns]

# Calculate minimum values for each column
min_values = pride_pivot.min()

# Define app layout
pride_layout = html.Div([
    html.H2('P R I D E', className = "mt-4", style={"color":"#007FFF", "margin-bottom":"2rem"}),
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        dbc.Col([
            html.H4("Indexes with Most Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            dcc.Graph(figure=figpride),
        ],  width=6),
        dbc.Col([
            html.H4("Demography-Wise Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            html.Label('Select Demography', style={"color":"#007FFF"}),
            html.Br(),
            dcc.Dropdown(
                id='pride-section-dropdown',
                options=sections_options,
                value=sections_options[0]['value']
            ),
            html.Label('Index Statements', style={"color":"#007FFF"}),
            dcc.Dropdown(
                id='pride-column-dropdown',
                options=columns_options,
                value=columns_options[0]['value']
            ),
            dcc.Graph(id='pride-bar-chart'),
            html.Div(id='pride-report-card'),
        ],  width=6),
    ],className = "mb-5"),

    dbc.Row([
        html.H4("Indexes with Most Positive Scores", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=pfigpride),
    ]),
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        html.H4("Difference of Our Scores from Benchmark Scores (in %)", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=mainDiffBar(df_pride)),
    ]),
    html.H4("COMPARISON OF INDEX STATEMENTS WITH BENCHMARK SCORES DIMENSION WISE", style={"color":"#007FFF","margin-top":"3rem"}),
    dbc.Row([
        html.H4("Personal", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(personal)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(personal)),  width=6),
        
    ],className = "mb-5"),
    dbc.Row([
        html.H4("Team", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(team)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(team)),  width=6),
        
    ],className = "mb-5"),

    dbc.Row([
        html.H4("Corporate Image", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(c_image)),  width=6),
        dbc.Col(dcc.Graph(figure=compareBar(c_image)),  width=6),
        
    ],className = "mb-5"),
    
    
    
    
    
    
])
