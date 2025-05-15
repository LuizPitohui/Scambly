import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, dcc
from database.db_handler import verificar_credenciais


# Registra a página no Dash Pages
dash.register_page(__name__, path="/")

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
                            html.H5("Seja bem-vindo(a) de volta!", style={"color": "white", "marginTop": "30px"})
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

                # Coluna do login
                dbc.Col(
                    html.Div(
                        [
                           html.H3("LOGIN", style={"marginBottom": "30px", "fontWeight": "bold"}),

                        dbc.Label("E-mail:"),
                        dbc.Input(type="email", id="email-login", placeholder="Digite seu e-mail"),

                        dbc.Label("Senha:", style={"marginTop": "15px"}),
                        dbc.Input(type="password", id="senha-login", placeholder="Digite sua senha"),

                        html.A("Esqueceu a senha?", href="/esqueceu-senha", style={"color": "#8000ff", "marginTop": "10px", "display": "block"}),

                        dbc.Button("Entrar", id="botao-login", color="primary", 
                                   style={"backgroundColor": "#8000ff", "border": "none", "marginTop": "20px", "width": "100%"}),

                        dcc.Location(id="url-login", refresh=True),  # ← ESSENCIAL PARA REDIRECIONAMENTO

                        html.Div(
                            [
                                html.Span("Não tem uma conta? "),
                                html.A("Cadastre-se", href="/cadastro", style={"color": "#8000ff"})
                            ],
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

from dash import callback, Input, Output, State, no_update
from database.db_handler import verificar_credenciais

@callback(
    Output("url-login", "href"),
    Output("session-email", "data"),
    Input("botao-login", "n_clicks"),
    State("email-login", "value"),
    State("senha-login", "value"),
    prevent_initial_call=True
)
def autenticar_usuario(n_clicks, email, senha):
    if not email or not senha:
        return no_update, no_update

    usuario = verificar_credenciais(email, senha)
    if usuario:
        return "/home", email  # ← salva o e-mail na sessão
    else:
        return no_update, no_update