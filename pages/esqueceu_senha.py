import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/esqueceu-senha")

layout = dbc.Container(
    [
        dbc.Row(
            [
                # Coluna da marca
                dbc.Col(
                    html.Div(
                        [
                            html.H1("Scambly", style={"color": "white", "fontSize": "50px"}),
                            html.P("Comunique e conquiste", style={"color": "white", "fontSize": "18px"}),
                            html.H5("Esqueceu sua senha?", style={"color": "white", "marginTop": "30px"})
                        ],
                        style={
                            "backgroundColor": "#8000ff",
                            "height": "100vh",
                            "padding": "50px",
                            "textAlign": "center"
                        }
                    ),
                    md=4,
                    style={"padding": "0px"}
                ),

                # Coluna do formulário
                dbc.Col(
                    html.Div(
                        [
                            html.H3("Redefinir Senha", style={"marginBottom": "30px", "fontWeight": "bold"}),

                            dbc.Label("Digite o e-mail cadastrado:"),
                            dbc.Input(type="email", id="email-recuperar", placeholder="exemplo@dominio.com"),

                            dbc.Button("Redefinir Senha", id="botao-redefinir", color="primary",
                                       style={"backgroundColor": "#8000ff", "border": "none", "marginTop": "25px", "width": "100%"}),

                            html.Div(
                                html.A("Voltar para Login", href="/", style={"color": "#8000ff"}),
                                style={"marginTop": "20px"}
                            )
                        ],
                        style={"padding": "50px"}
                    ),
                    md=8
                )
            ],
            style={"height": "100vh"}
        )
    ],
    fluid=True
)
