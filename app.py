import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly import tools
import plotly.plotly as py

############### BAR FORMATS ###############

green_bar_format = dict(
    color = 'rgba(126, 232, 74, 0.7)',
    line = dict(
        color = 'rgba(126, 232, 74, 1.0)',
        width = 1
    )
)

yellow_bar_format = dict(
    color = 'rgba(255, 250, 0, 0.8)',
    line = dict(
        color = 'rgba(255, 250, 0, 1.0)',
        width = 1
    )
)

red_bar_format = dict(
    color = 'rgba(211, 8, 12, 0.6)',
    line = dict(
        color = 'rgba(211, 8, 12, 1.0)',
        width = 1
    )
)

############### MOISTURE SETTINGS ###############

current_moisture = 33
high_value_moisture = 25
low_value_moisture = 0

range_high_line_moisture = go.Scatter(
    x=[0, 1],
    y=[high_value_moisture, high_value_moisture],
    mode='lines',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        dash = 'dash'
    )
)

range_low_line_moisture = go.Scatter(
    x=[0, 1],
    y=[low_value_moisture, low_value_moisture],
    mode='lines',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        dash = 'dash'
    )
)

current_line_moisture = go.Scatter(
    x=[0, 1],
    y=[current_moisture, current_moisture],
    line=dict(
        color='rgba(26, 33, 117, 1.0)'
    )
)
green_bar_moisture = go.Bar(
    x=[0.5], y=[15],
    name='good', marker = green_bar_format
)
yellow_bar_moisture = go.Bar(
    x=[0.5], y=[25],
    name='ok', marker = yellow_bar_format
)
red_bar_moisture = go.Bar(
    x=[0.5], y=[40],
    name='bad', marker = red_bar_format
)

############### GRAIN LOSS SETTINGS ###############

current_gloss = 0.015
high_value_gloss = .02
low_value_gloss = 0

range_high_line_gloss = go.Scatter(
    x=[0, 1],
    y=[high_value_gloss, high_value_gloss],
    mode='lines',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        dash = 'dash'
    )
)

range_low_line_gloss = go.Scatter(
    x=[0, 1],
    y=[low_value_gloss, low_value_gloss],
    mode='lines',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        dash = 'dash'
    )
)

current_line_gloss = go.Scatter(
    x=[0, 1],
    y=[current_gloss, current_gloss],
    line=dict(
        color='rgba(26, 33, 117, 1.0)'
    )
)
green_bar_gloss = go.Bar(
    x=[0.5], y=[0.01],
    name='good', marker = green_bar_format
)
yellow_bar_gloss = go.Bar(
    x=[0.5], y=[0.02],
    name='ok', marker = yellow_bar_format
)
red_bar_gloss = go.Bar(
    x=[0.5], y=[0.05],
    name='bad', marker = red_bar_format
)

############### FUEL EFFICIENCY SETTINGS ###############

current_fe = 7
high_value_fe = 15.5
low_value_fe = 0

range_high_line_fe = go.Scatter(
    x=[0, 1],
    y=[high_value_fe, high_value_fe],
    mode='lines',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        dash = 'dash'
    )
)

range_low_line_fe = go.Scatter(
    x=[0, 1],
    y=[low_value_fe, low_value_fe],
    mode='lines',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        dash = 'dash'
    )
)

current_line_fe = go.Scatter(
    x=[0, 1],
    y=[current_fe, current_fe],
    line=dict(
        color='rgba(26, 33, 117, 1.0)'
    )
)
green_bar_fe = go.Bar(
    x=[0.5], y=[11.44],
    name='good', marker = green_bar_format
)
yellow_bar_fe = go.Bar(
    x=[0.5], y=[15.5],
    name='ok', marker = yellow_bar_format
)
red_bar_fe = go.Bar(
    x=[0.5], y=[20],
    name='bad', marker = red_bar_format
)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Graphs'),

    dcc.Graph(id='a_graph',
        figure={
            'data': [
        		red_bar_moisture,
        		yellow_bar_moisture,
        		green_bar_moisture,
        		current_line_moisture,
                range_high_line_moisture,
                range_low_line_moisture
            ],
            'layout': go.Layout(
        	   barmode='overlay',
               title = 'Moisture',
               autosize=False,
               width=400,
               height=500,
               showlegend=False,
               xaxis=dict(
                    showgrid=False,
                    showline=False,
                    showticklabels=False,
                )
        	)
        }),
    dcc.Graph(id='b_graph',
        figure={
            'data': [
                red_bar_gloss,
                yellow_bar_gloss,
                green_bar_gloss,
                current_line_gloss,
                range_high_line_gloss,
                range_low_line_gloss
            ],
            'layout': go.Layout(
               barmode='overlay',
               title = 'Grain Loss',
               autosize=False,
               width=400,
               height=500,
               showlegend=False,
               xaxis=dict(
                    showgrid=False,
                    showline=False,
                    showticklabels=False,
                )
            )
        }),
    dcc.Graph(id='c_graph',
        figure={
            'data': [
                red_bar_fe,
                yellow_bar_fe,
                green_bar_fe,
                current_line_fe,
                range_high_line_fe,
                range_low_line_fe
            ],
            'layout': go.Layout(
               barmode='overlay',
               title = 'Fuel Efficiency',
               autosize=False,
               width=400,
               height=500,
               showlegend=False,
               xaxis=dict(
                    showgrid=False,
                    showline=False,
                    showticklabels=False,
                )
            )
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)









