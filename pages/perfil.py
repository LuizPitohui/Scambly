import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from database.db_handler import buscar_dados_usuario, atualizar_dados_usuario

dash.register_page(__name__, path="/perfil")

layout = dbc.Container(
    [
        html.H2("⚙️ Configurações", className="mb-4", style={"marginTop": "30px"}),
        html.P("Gerencie os detalhes da sua conta.", className="mb-4"),

        html.H5("Informações da conta"),
        html.Div(id="user-id", className="mb-3", style={"fontSize": "14px", "color": "#666"}),

        dbc.Row([
            dbc.Col([
                dbc.Label("Nome de exibição"),
                dbc.Input(id="nome", placeholder="Seu nome completo"),
            ], md=6),
            dbc.Col([
                dbc.Label("E-mail"),
                dbc.Input(id="email", type="email", placeholder="seu@email.com")
            ], md=6),
        ], className="mb-4"),

        html.Hr(),

        html.H5("Detalhes pessoais"),

        dbc.Row([
            dbc.Col([
                dbc.Label("Nome"),
                dbc.Input(id="nome_pessoal"),
            ], md=6),
            dbc.Col([
                dbc.Label("Sobrenome"),
                dbc.Input(id="sobrenome"),
            ], md=6),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Label("Endereço 1"),
                dbc.Input(id="endereco1"),
            ], md=6),
            dbc.Col([
                dbc.Label("Endereço 2"),
                dbc.Input(id="endereco2"),
            ], md=6),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Label("Cidade"),
                dbc.Input(id="cidade"),
            ], md=4),
            dbc.Col([
                dbc.Label("Região/Estado"),
                dbc.Input(id="estado"),
            ], md=4),
            dbc.Col([
                dbc.Label("CEP"),
                dbc.Input(id="cep"),
            ], md=4),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Label("País"),
                dbc.Input(id="pais"),
            ], md=4)
        ]),

        dbc.Button("Salvar mudanças", id="botao-salvar", color="primary", className="mt-4",
                   style={"backgroundColor": "#8000ff", "border": "none"}),

        html.Div(id="mensagem-perfil", className="mt-3", style={"fontWeight": "bold"})
    ],
    style={"maxWidth": "900px", "paddingBottom": "40px"},
    fluid=True
)