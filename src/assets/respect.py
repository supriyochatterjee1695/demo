from assets.pivotdash import pivot_df
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from assets.calcpre import df_respect, mainDiffBar, percentageDiffBar, compareBar, support, colab, caring


df = pd.read_csv('Test.csv')

df['nonPositive']=df['Neutral']+df['Negative']
respect_df = df[df['Dimension'] == 'Respect']  
data = respect_df.drop(['Neutral', 'Negative'], axis=1)
data = data.sort_values(by='nonPositive', ascending=False)
# Create a bar chart using Plotly Express
filtered_data = data[data['nonPositive'] > 15]
figrespect = px.bar(filtered_data, x='TrustIndexStatement', y='nonPositive', color='SubDimension',text_auto='.2s',
             
             color_discrete_sequence=['#007FFF','#4FFFB0','#FFC72C'],
             )
figrespect.update_layout(height=800,xaxis_title='', yaxis_title='Non-Positive Scores',yaxis_title_standoff=30 ,xaxis_tickangle=90,plot_bgcolor='white',showlegend=True,legend_orientation='h',legend=dict(x=-0.2, y=2))

# Show the plot
psodata = data.sort_values(by='Positive', ascending=False)
pfiltered_data = psodata[psodata['Positive'] >= 85]
pfigrespect = px.bar(pfiltered_data, x='TrustIndexStatement', y='Positive', color='SubDimension',text_auto='.2s',
             title='TrustIndexStatement vs Positive (Sorted by Most Positive)',
             color_discrete_sequence=['#007FFF','#4FFFB0'],
             labels={'TrustIndexStatement': 'Trust Index Statement', 'Positive': 'Positive Score'})
pfigrespect.update_layout(plot_bgcolor='white')



res_selected_columns = [
    'I am offered training or development to further myself professionally.',
    'I am given the resources and equipment to do my job.',
    'Management shows appreciation for good work and extra effort.',
    'Management recognizes honest mistakes as part of doing business.',
    'We celebrate people who try new and better ways of doing things, regardless of the outcome.',
    'Management genuinely seeks and responds to suggestions and ideas.',
    'Management involves people in decisions that affect their jobs or work environment.',
    'This is a physically safe place to work.',
    'This is a psychologically and emotionally healthy place to work.',
    'Our facilities contribute to a good working environment.',
    'People are encouraged to balance their work life and their personal life.',
    'Management shows a sincere interest in me as a person, not just an employee.',
    'We have special and unique benefits here.',
    'I am able to take time off from work when I think it\'s necessary.'
]

res_pivot = pivot_df.loc[:, res_selected_columns]


# Create dropdown options for sections and columns
sections_options = [{'label': section, 'value': section} for section in res_pivot.index.get_level_values('Section').unique()]
columns_options = [{'label': column, 'value': column} for column in res_pivot.columns]

# Calculate minimum values for each column
min_values = res_pivot.min()

# Define app layout
res_layout = html.Div([
    html.H2("R E S P E C T", className = "mt-4", style={"color":"#007FFF", "margin-bottom":"2rem"}),
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        dbc.Col([
            html.H4("Indexes with Most Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            dcc.Graph(id='respect-graph', figure=figrespect),
        ], width=6),
        
        dbc.Col([
            html.H4("Demography-Wise Non-Positive Scores", style={"color":"#007FFF"}),
            html.Hr( style={"color":"#007FFF"}),
            html.Label('Select Demography', style={"color":"#007FFF"}),
            html.Br(),
            dcc.Dropdown(
                id='ressection-dropdown',
                options=sections_options,
                value=sections_options[0]['value']
            ),
            html.Label('Index Statements', style={"color":"#007FFF"}),
            dcc.Dropdown(
                id='rescolumn-dropdown',
                options=columns_options,
                value=columns_options[0]['value']
            ),
            html.Br(),
            dcc.Graph(id='resbar-chart'),
            html.Div(id='resreport-card'),
        ], width=6, style={}),
    ],className = "mb-5"),

    dbc.Row([
        html.H4("Indexes with Most Positive Scores", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=pfigrespect),
    ]),
    
    
    
    html.Hr( style={"color":"#007FFF"}),
    dbc.Row([
        html.H4("Difference of Our Scores from Benchmark Scores (in %)", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dcc.Graph(figure=mainDiffBar(df_respect)),
    ]),
    html.H4("COMPARISON OF INDEX STATEMENTS WITH BENCHMARK SCORES DIMENSION WISE", style={"color":"#007FFF","margin-top":"3rem"}),
    
    dbc.Row([
        html.H4("Collaboration", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(support)), width=6),
        dbc.Col(dcc.Graph(figure=compareBar(support)), width=6),
        
    ],className = "mb-5"),
    dbc.Row([
        html.H4("Support", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(colab)), width=6),
        dbc.Col(dcc.Graph(figure=compareBar(colab)), width=6),
        
    ],className = "mb-5"),
    dbc.Row([
        html.H4("Caring", style={"color":"#007FFF","margin-top":"2rem"}),
        html.Hr( style={"color":"#007FFF"}),
        dbc.Col(dcc.Graph(figure=percentageDiffBar(caring)), width=6),
        dbc.Col(dcc.Graph(figure=compareBar(caring)), width=6),
        
        
    ],className = "mb-5"),
    
    
    
    
    
    
   
    
])

