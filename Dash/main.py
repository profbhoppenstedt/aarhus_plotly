import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset
file_path = 'test.csv'
data = pd.read_csv(file_path)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1('Titanic Passenger Data Dashboard'),
    dcc.Dropdown(
        id='pclass-dropdown',
        options=[{'label': f'Class {i}', 'value': i} for i in sorted(data['Pclass'].unique())],
        value=1,
        placeholder='Select a class'
    ),
    dcc.Graph(id='age-histogram'),
    dcc.Graph(id='gender-pie-chart'),
    dcc.Graph(id='fare-age-scatter')
])

# Callback to update the age histogram based on Pclass
@app.callback(
    Output('age-histogram', 'figure'),
    Input('pclass-dropdown', 'value')
)
def update_histogram(selected_class):
    filtered_data = data[data['Pclass'] == selected_class]
    fig = px.histogram(filtered_data, x='Age', title=f'Age Distribution for Class {selected_class}')
    return fig

# Callback to update the gender pie chart based on Pclass
@app.callback(
    Output('gender-pie-chart', 'figure'),
    Input('pclass-dropdown', 'value')
)
def update_pie_chart(selected_class):
    filtered_data = data[data['Pclass'] == selected_class]
    fig = px.pie(filtered_data, names='Sex', title=f'Gender Distribution for Class {selected_class}')
    return fig

# Callback to update the fare vs age scatter plot
@app.callback(
    Output('fare-age-scatter', 'figure'),
    Input('pclass-dropdown', 'value')
)
def update_scatter_plot(selected_class):
    filtered_data = data[data['Pclass'] == selected_class]
    fig = px.scatter(filtered_data, x='Age', y='Fare', color='Pclass', title='Fare vs Age by Class')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)