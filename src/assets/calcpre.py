import pandas as pd
import re
import plotly.graph_objects as go
df=pd.read_excel('Arranged.xlsx', sheet_name="Main")

r_columns = ['Professional','S1','TRANING & COMPLIANCE','Hyderabad','SYSTEMS','sales operations','property survey','human resource','land & industrial land','logistic&warehouse','MARKET RESEARCH','MARKETING','OFFICE STUFF','OPEN MARKET','EXPERIENCE','DIRECTOR','DIGITAL MARKETING','corporate communication','corp com & pre sales','compliance & training','compliance','CARE & DEVELOPMENT','accounts','Very little or none','Part time','Over 20 years','More than 6 months upto 1 year','Upto 6 months','55 years or older','Another gender not listed']
df = df.drop(r_columns, axis=1)

# Assuming df is your DataFrame
new_column_names = []

for col in df.columns:
    # Remove special characters and replace spaces with underscores
    new_col = re.sub(r'[^\w\s]', '', col).replace(' ', '_')
    new_column_names.append(new_col)

# Assign the new column names to the DataFrame
df.columns = new_column_names
x = df
x['percentDiff'] = ((df['best_scores'] - df['our_score']) / df['best_scores']) * 100
x['percentDiff'] = x['percentDiff'].round(2)
x['Main'].unique()

#Main Section Function
def mainDiffBar(df_subName):
    # Sort DataFrame by 'percentDiff' column in descending order
    sorted_df = df_subName.sort_values(by='percentDiff', ascending=False)
    p_name = sorted_df['Main'].unique()
    color_mapping = {
        sub: 'rgb({}, {}, {})'.format(i * 30 % 256, i * 60 % 256, i * 90 % 256)  # Example: Assigning a unique color for each unique 'Sub' value
        for i, sub in enumerate(sorted_df['Sub'].unique())
    }
    # Create a bar chart
    fig = go.Figure()

    # Add bars for 'percentDiff'
    fig.add_trace(go.Bar(
        x=sorted_df['Parameters'],
        y=sorted_df['percentDiff'],
        marker_color='#007FFF',
        text=sorted_df['percentDiff'],  # Values to display inside the bars
        textposition='auto',  # Positioning of the text inside the bars
        
        
    ))

    # Update layout
    fig.update_layout(
        title=None,
        xaxis=dict(title='Index Statements',tickangle=90),
        yaxis=dict(title='Percent Difference (in %)'),
        plot_bgcolor='rgba(0,0,0,0)',  # Set background color to transparent
        paper_bgcolor='rgba(0,0,0,0)',# Set paper color to transparent
        height=900
    )

    # Show the plot
    return fig
    
#SubSection Functions
def percentageDiffBar(df_subName):
    # Sort DataFrame by 'percentDiff' column in descending order
    sorted_df = df_subName.sort_values(by='percentDiff', ascending=False)
    p_name = sorted_df['Sub'].unique()
    # Create a bar chart
    fig = go.Figure()

    # Add bars for 'percentDiff'
    fig.add_trace(go.Bar(
        x=sorted_df['Parameters'],
        y=sorted_df['percentDiff'],
        marker_color='#007FFF',
        text=sorted_df['percentDiff'],  # Values to display inside the bars
        textposition='auto',  # Positioning of the text inside the bars
        
    ))

    # Update layout
    fig.update_layout(
        title=None,
        xaxis=dict(title='Index Statements',tickangle=90),
        yaxis=dict(title='Percent Difference (in %)'),
        plot_bgcolor='rgba(0,0,0,0)',  # Set background color to transparent
        paper_bgcolor='rgba(0,0,0,0)',# Set paper color to transparent
        # Set paper color to transparent
        height=900
    )

    # Show the plot
    return fig
    

#COMPARISON SECTION

def compareBar(df_subName):
    # Sort parameter names based on 'percentDiff' in descending order
    # Get unique Parameter names
    parameters = df_subName['Parameters'].unique()
    p_name = df_subName['Sub'].unique()

    # Sort unique parameter names in descending order of 'percentDiff'
    sorted_parameters = sorted(parameters, key=lambda x: df_subName[df_subName['Parameters'] == x]['percentDiff'].iloc[0], reverse=True)

    # Create a bar chart
    figure = go.Figure()

    # Add bars for 'our_score' and 'best_score'
    figure.add_trace(go.Bar(
        x=sorted_parameters,
        y=[df_subName[df_subName['Parameters'] == parameter]['our_score'].mean() for parameter in sorted_parameters],
        name='Our Score',
        marker_color='#fd5c63',
        text=[round(df_subName[df_subName['Parameters'] == parameter]['our_score'].mean(), 2) for parameter in sorted_parameters],  # Values to display inside the bars
        textposition='auto',  # Positioning of the text inside the bars
    ))

    figure.add_trace(go.Bar(
        x=sorted_parameters,
        y=[df_subName[df_subName['Parameters'] == parameter]['best_scores'].mean() for parameter in sorted_parameters],
        name='Benchmark Scores',
        marker_color='#007FFF',
        text=[round(df_subName[df_subName['Parameters'] == parameter]['best_scores'].mean(), 2) for parameter in sorted_parameters],  # Values to display inside the bars
        textposition='auto',  # Positioning of the text inside the bars
        
    ))

    # Update layout
    figure.update_layout(
        title= None,
        xaxis=dict(title='Index Statements',tickangle=90),
        yaxis=dict(title='Scores'),
        barmode='group',  # Display bars in grouped mode,
        plot_bgcolor='rgba(0,0,0,0)',  # Set background color to transparent
        paper_bgcolor='rgba(0,0,0,0)',  # Set paper color to transparent
        # Set paper color to transparent
        height=900
    )

    # Show the plot
    return figure

df_credibility = x[x['Main']=='Credibility']
communication = x[(x['Main'] == 'Credibility') & (x['Sub'] == 'Communication')]
competence = x[(x['Main'] == 'Credibility') & (x['Sub'] == 'Competence')]
integrity = x[(x['Main'] == 'Credibility') & (x['Sub'] == 'Integrity')]









df_respect = x[x['Main']=='Respect']
support = x[(x['Main'] == 'Respect') & (x['Sub'] == 'Support')]
colab = x[(x['Main'] == 'Respect') & (x['Sub'] == 'Collaboration')]
caring = x[(x['Main'] == 'Respect') & (x['Sub'] == 'Caring')]



df_fairness = x[x['Main']=='Fairness']
equity = x[(x['Main'] == 'Fairness') & (x['Sub'] == 'Equity')]
impartiality = x[(x['Main'] == 'Fairness') & (x['Sub'] == 'Impartiality')]
justice = x[(x['Main'] == 'Fairness') & (x['Sub'] == 'Justice')]



df_pride = x[x['Main']=='Pride']
personal = x[(x['Main'] == 'Pride') & (x['Sub'] == 'Personal Job')]
team = x[(x['Main'] == 'Pride') & (x['Sub'] == 'Team')]
c_image = x[(x['Main'] == 'Pride') & (x['Sub'] == 'Corporate Image')]



df_camaraderie = x[x['Main']=='Camaraderie']
intimacy = x[(x['Main'] == 'Camaraderie') & (x['Sub'] == 'Intimacy')]
hospitality = x[(x['Main'] == 'Camaraderie') & (x['Sub'] == 'Hospitality')]
community = x[(x['Main'] == 'Camaraderie') & (x['Sub'] == 'Community')]