import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

current_moisture = 0.9
high_value = 0
low_value = 0

range_high_line = go.Scatter(
    x=[0, 1],
    y=[high_value, high_value],
    mode='lines',
)

range_low_line = go.Scatter(
    x=[0, 1],
    y=[low_value, low_value],
    mode='lines',
)

current_line = go.Scatter(
    x=[0, 1],
    y=[current_moisture, current_moisture],
    line=dict(
        color='rgba(26, 33, 117, 1.0)'
    )
)
green_bar = go.Bar(
    x=[0.5],
    y=[1],
    name='good',
    marker = dict(
    	color = 'rgba(126, 232, 74, 0.6)',
    	line = dict(
			color = 'rgba(126, 232, 74, 1.0)',
			width = 1
		)
	)
)
yellow_bar = go.Bar(
    x=[0.5],
    y=[0.4],
    name='ok',
    marker = dict(
    	color = 'rgba(255, 250, 0, 0.6)',
		line = dict(
			color = 'rgba(255, 250, 0, 1.0)',
			width = 1
		)
	)
)
red_bar = go.Bar(
    x=[0.5],
    y=[0.2],
    name='bad',
    	marker = dict(
		color = 'rgba(211, 8, 12, 0.6)',
		line = dict(
			color = 'rgba(211, 8, 12, 1.0)',
			width = 1
		)
	)
)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Graphs'),

    # html.Div(children='''
    #     Dash: A web application framework for Python.
    # '''),

    dcc.Graph(id='a_graph',
              figure={
        'data': [
        		green_bar,
        		yellow_bar,
        		red_bar,
        		current_line
        ],
        'layout': go.Layout(
        	barmode='overlay'
        	)

    }),
    html.H1(children='Grain Loss')
])

if __name__ == '__main__':
    app.run_server(debug=True)









