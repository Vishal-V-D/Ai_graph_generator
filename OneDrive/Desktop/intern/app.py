import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import base64
import io
from flask_cors import CORS
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

sample_data = pd.DataFrame({
    "Date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
    "Sales": [100, 150, 120, 170, 200, 230, 180, 220, 190, 210],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West", "North", "South"],
    "Seed": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
CORS(app.server)
app.title = "AI-Powered Dashboard"

app.layout = dbc.Container([
    dbc.Navbar(
        dbc.Container([
            html.Div("AI-Powered Dashboard", className="navbar-brand", style={'textAlign': 'center', 'flex': '1'}),
            dbc.DropdownMenu(
                label="User",
                children=[
                    dbc.DropdownMenuItem("Profile Settings", href="#"),
                    dbc.DropdownMenuItem("Logout", href="#")
                ],
                toggleClassName="btn-secondary",
                className="d-flex align-items-center"
            )
        ], fluid=True),
        color="dark",
        dark=True,
        className="mb-4",
        style={'border': 'none', 'padding': '10px 0'}
    ),
    dbc.Row([
        dbc.Col([
            html.H5("Upload Your Dataset", className="text-secondary"),
            dcc.Upload(
                id='upload-data',
                children=html.Div(['Drag & Drop or ', html.A('Select a CSV File')]),
                style={
                    'width': '100%', 'height': '60px', 'lineHeight': '60px',
                    'borderWidth': '1px', 'borderStyle': 'dashed',
                    'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
                }
            ),
            html.Div(id='file-status', children="No file uploaded yet. Using sample data.")
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col(dbc.InputGroup([
            dbc.Input(id="user-query", placeholder="Ask an AI question about your data", type="text"),
            dbc.Button("Generate Insights", id="generate-button", color="primary")
        ]), width=12)
    ], className="my-3"),
    dbc.Row([
        dbc.Col([
            dbc.Label("Customize Graph Title:", className="text-secondary"),
            dbc.Input(id="graph-title", placeholder="Enter graph title (Optional)", type="text")
        ], width=6),
        dbc.Col([
            dbc.Label("Select Graph Type:", className="text-secondary"),
            dcc.Dropdown(
                id="graph-type-selector",
                options=[
                    {"label": "Line Chart", "value": "line"},
                    {"label": "Bar Chart", "value": "bar"},
                    {"label": "Scatter Plot", "value": "scatter"},
                    {"label": "Pie Chart", "value": "pie"},
                    {"label": "Histogram", "value": "histogram"}
                ],
                value="line",
                clearable=False
            )
        ], width=6)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Label("Select Row Range:", className="text-secondary"),
            dcc.RangeSlider(
                id='row-range-slider',
                min=0,
                max=9,
                step=1,
                marks={i: str(i) for i in range(10)},
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            html.Div(id='selected-range', className="mt-2")
        ], width=12)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Label("Select X-axis Column:", className="text-secondary"),
            dcc.Dropdown(id="x-axis-selector", clearable=False)
        ], width=6),
        dbc.Col([
            dbc.Label("Select Y-axis Column:", className="text-secondary"),
            dcc.Dropdown(id="y-axis-selector", clearable=False)
        ], width=6),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Loading(id="loading-output", type="circle", children=html.Div(id='output-graph')), width=12),
        dbc.Col(html.Div(id="ai-insights", className="mt-4 text-secondary", style={'border': '1px solid #ccc', 'padding': '15px'}), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.Div("© 2024 AI-Powered Dashboard | All Rights Reserved", className="text-center text-muted py-3"), width=12)
    ]),
    html.Div(id="data-storage", style={"display": "none"}),
    html.Div(id="processing-status", style={"display": "none"})
])

def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        return pd.read_csv(io.StringIO(decoded.decode('utf-8'))), None
    except Exception as e:
        return None, f"Error processing file: {str(e)}"

def query_gemini(data_description, user_query):
    try:
        response = model.generate_content(f"Dataset Description: {data_description}\nUser Query: {user_query}")
        response_text = response.text.strip() if response and response.text else "No response from Gemini AI."
        formatted_response = [html.Li(line.strip()) for line in response_text.split("\n") if line.strip()]
        return html.Ul(formatted_response)
    except Exception as e:
        return html.Div(f"Error in Gemini API interaction: {str(e)}")

@app.callback(
    [Output('file-status', 'children'),
     Output('data-storage', 'children'),
     Output('x-axis-selector', 'options'),
     Output('y-axis-selector', 'options')],
    Input('upload-data', 'contents'),
    prevent_initial_call=True
)
def load_data(contents):
    if contents:
        df, error_msg = parse_contents(contents)
        if df is None:
            return error_msg, sample_data.to_json(), [], []
        columns = [{"label": col, "value": col} for col in df.columns]
        return f"File uploaded successfully with {df.shape[0]} rows.", df.to_json(), columns, columns
    columns = [{"label": col, "value": col} for col in sample_data.columns]
    return "No file uploaded. Using sample data.", sample_data.to_json(), columns, columns

@app.callback(
    Output('selected-range', 'children'),
    Input('row-range-slider', 'value')
)
def update_row_range(value):
    return f"Selected Row Range: {value[0]} to {value[1]}" if value else "Select a range of rows."

@app.callback(
    [Output('output-graph', 'children'),
     Output('ai-insights', 'children'),
     Output('processing-status', 'children')],
    [Input('graph-type-selector', 'value'),
     Input('x-axis-selector', 'value'),
     Input('y-axis-selector', 'value'),
     Input('graph-title', 'value'),
     Input('row-range-slider', 'value')],
    State('user-query', 'value'),
    State('data-storage', 'children')
)
def update_graph(graph_type, x_column, y_column, graph_title, row_range, user_query, data_json):
    if not data_json:
        return "Please upload a dataset.", "No data available.", ""
    df = pd.read_json(data_json)
    if row_range:
        df = df.iloc[row_range[0]:row_range[1]+1]
    graph_title = graph_title or f"{x_column} vs {y_column}" if x_column and y_column else "Graph Title"
    if graph_type == "line":
        fig = px.line(df, x=x_column, y=y_column, title=graph_title)
    elif graph_type == "bar":
        fig = px.bar(df, x=x_column, y=y_column, title=graph_title)
    elif graph_type == "scatter":
        fig = px.scatter(df, x=x_column, y=y_column, title=graph_title)
    elif graph_type == "pie":
        fig = px.pie(df, names=x_column, values=y_column, title=graph_title)
    elif graph_type == "histogram":
        fig = px.histogram(df, x=y_column, title=graph_title)
    processing_message = html.Div("Analyzing data... Please wait.", className="text-center text-info")
    ai_response = ""
    if user_query:
        data_description = f"Data contains {df.shape[0]} rows and {df.shape[1]} columns: {', '.join(df.columns)}."
        ai_response = query_gemini(data_description, f"Generate insights for {graph_type} chart with {x_column} and {y_column}. {user_query}")
    return dcc.Graph(figure=fig), ai_response, processing_message

if __name__ == '__main__':
    app.run_server(debug=True)
