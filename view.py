# Importing modules
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

'''
MAIN LAYOUTS
'''
# Navbar layout
def navbar():
    navbar = dbc.Navbar(
        [
            dbc.NavbarBrand(
                [
                    html.H5(html.I(className="fas fa-cannabis")),
                    html.H5("CannaRec")
                ]
                
            ),
            dbc.Collapse(
                [
                    html.Ul(
                        [
                            dbc.NavItem(html.A("Home", href = '#home', className = "nav-link")),
                            dbc.NavItem(html.A("Search By Strain", href = '#by-strain', className = "nav-link")),
                            dbc.NavItem(html.A("Search By Flavors & Feelings", href = '#by-flavfeel', className = "nav-link")),  
                            dbc.NavItem(html.A("Contact", href = 'https://www.linkedin.com/in/dylan-mendonca-65165898/', className = "nav-link"))
                        ], className = "nav navbar-nav ml-auto"
                    )
                ], className = "navbar-collapse"),
        ], fixed = 'top', className = "main-navbar bg-transparent", light=False, 
    )
    return navbar

# Home Page Layout
def jumbotron():
    jumbotron = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Jumbotron(
                                [
                                    html.H1("CannaRec", className="display-3"),
                                    html.P(
                                        ["Picking a new strain can be hard.",
                                        html.Br(),
                                        "We're here to help."],
                                        className="lead",
                                    ),
                                    html.Hr(className="my-2"),
                                    html.P(
                                        "Click one of the options below to get started."
                                    ),
                                    html.P(
                                        [
                                            dbc.Button(html.A("Search By Strain", href = "#by-strain", className = "white_link"), color="primary",),
                                            dbc.Button(html.A("Search By Flavors & Feelings", href = "#by-flavfeel", className = "white_link"), color="primary",style = {'margin-left':'15px'})
                                        ], className="lead"),
                                ], className = "landingj container"
                            )
                        ], width = {'size': 3, 'offset':2}, className = "margin-up"
                    )
                ]
            )
        ], className = "landing", id = "home"
    )
    return jumbotron

# Search By Strain Page Layout
def by_strain(strain_dropdown):
    body = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Jumbotron(
                                [
                                    html.Div(
                                        [
                                            html.H4("Search By Strain"),
                                            html.Br(),
                                            html.H6("What strain do you like?"),
                                            dcc.Dropdown(
                                                id = "strain_name",
                                                options = strain_dropdown.to_dict(orient='records'),
                                                value = None,
                                                placeholder = "Select a Strain"
                                            ),
                                            html.Br(),
                                            html.H6("Why do you like this strain?"),
                                            dcc.Dropdown(
                                                id = "why_strain",
                                                options = [
                                                    {'label':"Feels Great", "value":"general"},
                                                    {'label':"Tastes Amazing", "value":"flavors"},
                                                    {'label':"Treats a Medical Condition", "value":"medical"},
                                                    ],
                                                value = None,
                                                placeholder = "Select the Reason"
                                            ),
                                            html.Br(),
                                            dbc.Button("CannaRec Me!", id = "letsgo", color = "primary")
                                        ], className = "question-section"
                                    ),
                                    
                                ], className = "logon container", 
                            )
                        ], width = {'size':4, 'offset':1}, className = "margin-up"
                    ),

                    dbc.Col(
                        [
                            dcc.Loading(
                                [
                                    html.Div(
                                        [

                                        ], id = "results", className = "results"
                                    )
                                ]
                            )

                        ], width = {'size': 6}, className = "margin-up"
                    )
                ], 
            )     


        ], id = "by-strain"
    )

    return body

# Search By Flavors and Feelings Layout
def by_flavfeels(general_dropdown, flavor_dropdown, medical_dropdown):
    body2 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Jumbotron(
                                    [
                                        html.Div(
                                            [
                                                html.H4("Search By Flavors & Feelings"),
                                                html.Br(),
                                                html.H6("What feelings do you like?"),
                                                dcc.Dropdown(
                                                    id = "feelings_drop",
                                                    options = general_dropdown.to_dict(orient='records'),
                                                    value = None,
                                                    placeholder = "Select Feelings",
                                                    multi = True
                                                ),
                                                html.Br(),
                                                html.H6("What flavors do you like?"),
                                                dcc.Dropdown(
                                                    id = "flavors_drop",
                                                    options = flavor_dropdown.to_dict(orient='records'),
                                                    value = None,
                                                    placeholder = "Select Flavors",
                                                    multi = True
                                                ),
                                                html.Br(),
                                                html.H6("What medical conditions do you want to treat?"),
                                                dcc.Dropdown(
                                                    id = "medical_drop",
                                                    options = medical_dropdown.to_dict(orient='records'),
                                                    value = None,
                                                    placeholder = "Select Medical Condition to Treat",
                                                    multi = True
                                                ),
                                                html.Br(),
                                                dbc.Button("CannaRec Me!", id = "letsgo2", color = "primary")
                                            ], className = "question-section"
                                        )
                                    ], className = "logon container margin-up"
                            )
                        ], width = {'size':4, 'offset':1 }
                    ),

                    dbc.Col(
                        [
                            dcc.Loading(
                                [
                                    html.Div(
                                        [

                                        ], id = "results2", className = "results"
                                    )
                                ]
                            )
                        ], width = {'size': 6}, className = "margin-up"
                    )
                ], 
            )     
        ], id = "by-flavfeel"
    )
    return body2


'''
HELPER FUNCTIONS
'''
# Creates a little rectangular shaped card for a strain with all info
def create_cannacard(strain_name, strain_type, strain_symbol, strain_url, similarity):
    if similarity > 0.90:
        sim = "high"
    elif similarity > 0.70:
        sim = "med"
    else:
        sim = "low"
    
    div = html.Div(
        [
            html.Div(
                [
                    strain_type.title()
                ], className = "strain-header",
            ),
            html.Div(
                [
                    "%d%% Match" % (similarity*100)
                ], className = f"strain-similarity {sim}", 
            ),
            html.Div(
                [
                    strain_symbol.title()
                ], className = "strain-symbol", 
            ),
            html.Div(
                [
                    strain_name
                ], className = "strain-name", 
            ),
        ], className = f"strain-card {strain_type.lower()}"
    )
    return html.A([div], href = strain_url, className = "strain-l")

# Create arrow at bottom right on scroll
def create_arrow():
    div = html.Div(
        [
            html.Span(
                [
                    html.A(html.I(className = "fa fa-3x fa-arrow-circle-up"), href = "#home")
                ], className = "scroll-top-inner"
            )
        ], className = "scroll-top-wrapper"
    )
    return div