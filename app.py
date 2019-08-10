# Importing modules
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
from flask import send_from_directory


# Importing stuff from model and view
from view import navbar, jumbotron, by_strain, by_flavfeels, create_cannacard, create_arrow
from model import similar_strain, find_me_strains


'''
LOADING DATA
'''
# Loading dropdown terms
strain_dropdown = pd.read_json("./assets/data/strain_dropdown.json", orient='split')
general_dropdown = pd.read_json("./assets/data/general_dropdown.json", orient='split')
medical_dropdown = pd.read_json("./assets/data/medical_dropdown.json", orient='split')
flavor_dropdown = pd.read_json("./assets/data/flavor_dropdown.json", orient='split')


'''
DECLARING APP
'''
# Declaring app and setting up some config variables
app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True
server = app.server
app.title = "CannaRec"


'''
APP LAYOUT
'''

# Compiling Layouts
app.layout = html.Div(
    [
        navbar(),
        jumbotron(),
        by_strain(strain_dropdown),
        by_flavfeels(general_dropdown, flavor_dropdown, medical_dropdown),
        create_arrow()
    ]
)


'''
CALLBACKS AND ROUTING
'''
# Routing for favicon
@server.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(server.root_path, 'assets'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Callback for By Strains Page Layout
@app.callback(
    Output("results","children"),
    [Input("letsgo","n_clicks")],
    [State("strain_name","value"),
    State("why_strain","value"),
    ]
)
def update_results(n_clicks, strain_name, why_strain):
    if strain_name is None or why_strain is None:
        raise dash.exceptions.PreventUpdate
    elif n_clicks > 0:
        data = pd.read_json("./assets/data/all_data.json", orient='split')
        if why_strain == "general":
            by = pd.read_json("./assets/data/general_sim.json", orient='split')
        elif why_strain == "medical":
            by = pd.read_json("./assets/data/medical_sim.json", orient='split')
        elif why_strain == "flavors":
            by = pd.read_json("./assets/data/flavor_sim.json", orient='split')
        similar_strains = similar_strain(strain = strain_name,  main_dataset = data, by = by).loc[0:8]
        output = []
        for _, row in similar_strains.iterrows():
            output.append(
                create_cannacard(strain_name = row['strains'], strain_type = row['Type'], strain_symbol = row['Symbol'], strain_url = row['url'], similarity = row[strain_name])
            )
        return html.Div(output, className = "grid")

# Callback for by flavors and feelings layout
@app.callback(
    Output("results2","children"),
    [Input("letsgo2","n_clicks")],
    [State("feelings_drop","value"),
    State("medical_drop","value"),
    State("flavors_drop","value")]
)
def update_body2(n_clicks, feelings, medical, flavors):
    if all([feelings is None, medical is None, flavors is None]):
        raise dash.exceptions.PreventUpdate
    elif n_clicks > 0:
        everything = pd.read_json("./assets/data/everything.json", orient='split')
        similar_strains = find_me_strains(general_liked=feelings or [], medical_liked=medical or [], flavors_liked=flavors or [], everything = everything)[0:8]
        main_dataset = pd.read_json("./assets/data/all_data.json", orient='split')
        concatenated = pd.concat([similar_strains, main_dataset], axis = 1, join = 'inner')
        output = []
        for strain, row in concatenated.iterrows():
            output.append(
                create_cannacard(strain_name = strain, strain_type = row['Type'], strain_symbol = row['Symbol'], strain_url = row['url'], similarity = row['Similarity_Score'])
            )        
        return html.Div(output, className = "grid")


'''
LAUNCHING APP
'''
# Running the app
if __name__ == "__main__":
    app.run_server(debug=True)