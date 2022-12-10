import dash
from dash import html, Input, Output, State
import dash_select as ds

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        ds.Select(
            id="my_select",
            options=list(range(10)),
            value=[2],
            multiple=True,
            size=10,
            style={"width": "200px"}
        ),
        html.Button("Add option", id="addopt_btn"),
        html.Div(id="output")
    ]
)


@app.callback(
    Output("output", "children"),
    Input("my_select", "value"),
)
def show_selection(selected):
    return f"You have selected {selected}"


@app.callback(
    Output("my_select", "options"),
    Input("addopt_btn", "n_clicks"),
    State("my_select", "options"),
    prevent_initial_call=True,
)
def add_option(n, options):
    return options + [len(options)]


if __name__ == "__main__":
    app.run_server(debug=True)