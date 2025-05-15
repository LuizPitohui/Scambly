import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback
from database.db_handler import inserir_usuario

dash.register_page(__name__, path="/cadastro")

layout = dbc.Container(
    [
        dbc.Row(
            [
                # Lado esquerdo com branding
                dbc.Col(
                    html.Div(
                        [
                            html.H1("Scambly", style={"color": "white", "fontSize": "50px"}),
                            html.P("Comunique e conquiste", style={"color": "white", "fontSize": "18px"}),
                            html.H5("Crie sua conta e comece a ensinar e aprender!", style={"color": "white", "marginTop": "30px"})
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

                # Formulário de cadastro
                dbc.Col(
                    html.Div(
                        [
                            html.H3("CADASTRO", style={"marginBottom": "30px", "fontWeight": "bold"}),

                            dbc.Label("Nome Completo:"),
                            dbc.Input(type="text", id="nome-cadastro", placeholder="Digite seu nome completo"),

                            dbc.Label("E-mail:", style={"marginTop": "15px"}),
                            dbc.Input(type="email", id="email-cadastro", placeholder="Digite seu e-mail"),

                            dbc.Label("Senha:", style={"marginTop": "15px"}),
                            dbc.Input(type="password", id="senha-cadastro", placeholder="Crie uma senha"),

                            dbc.Button("Cadastrar", id="botao-cadastro", color="primary",
                                       style={"backgroundColor": "#8000ff", "border": "none", "marginTop": "25px", "width": "100%"}),

                            html.Div(
                                [
                                    html.Span("Já tem uma conta? "),
                                    html.A("Faça login", href="/", style={"color": "#8000ff"})
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

@callback(
    Output("botao-cadastro", "children"),
    Input("botao-cadastro", "n_clicks"),
    State("nome-cadastro", "value"),
    State("email-cadastro", "value"),
    State("senha-cadastro", "value"),
    prevent_initial_call=True
)
def cadastrar_usuario(n_clicks, nome, email, senha):
    print(f"→ Dados recebidos: nome={nome}, email={email}, senha={senha}")

    if not nome or not email or not senha:
        return "Preencha todos os campos"

    try:
        sucesso = inserir_usuario(nome, email, senha)
        return "Cadastro realizado!" if sucesso else "E-mail já cadastrado"
    except Exception as e:
        print("Erro no callback de cadastro:", e)
        return "Erro interno"