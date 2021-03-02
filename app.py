import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame({
    "Team": ["Seattle", "San Francisco", "Arizona", "Los Angeles"],
    "Wins": [12, 6, 8, 10],
    "Losses": [4, 10, 8, 6]
})

dcc.Dropdown(
    options=[
        {'label': 'NFC West', 'value': 'NFCW'},
        {'label': 'NFC North', 'value': 'NFCN'},
        {'label': 'NFC East', 'value': 'NFCE'},
        {'label': 'NFC South', 'value': 'NFCS'},
        {'label': 'AFC West', 'value': 'AFCW'},
        {'label': 'AFC North', 'value': 'AFCN'},
        {'label': 'AFC East', 'value': 'AFCE'},
        {'label': 'AFC South', 'value': 'AFCS'}
    ],
    placeholder="Select a division."
)

fig = px.bar(df, x="Team", y="Wins", color="Team", barmode="group", title="2020 NFC West")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.H1(children="NFC West 2020 Records"),

    dcc.Graph(
        id='NFC-Graph',
        figure=fig
    )
])

if __name__== '__main__':
    app.run_server(debug=True)