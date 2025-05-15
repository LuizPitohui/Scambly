import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
from database.db_handler import buscar_dados_usuario

dash.register_page(__name__, path="/home")

# Layout da Home
layout = dbc.Container(
    [
        html.H2(id="boas-vindas", children="Carregando...", style={"marginTop": "30px"}),
        html.H4(id="quantidade-pontos", children="Carregando...", style={"marginBottom": "30px"}),

        dbc.Row([
            dbc.Col(dbc.Button("📅 Agendar Aula", href="/agendar-aula", color="primary",
                               style={"backgroundColor": "#8000ff", "border": "none", "width": "100%"}), md=4),
            dbc.Col(dbc.Button("🛒 Loja de Pontos", href="/loja", color="light",
                               style={"color": "#8000ff", "borderColor": "#8000ff", "width": "100%"}), md=4),
            dbc.Col(dbc.Button("🎓 Seja um Tutor", href="/tutor", color="light",
                               style={"color": "#8000ff", "borderColor": "#8000ff", "width": "100%"}), md=4),
        ], className="mb-4"),

        html.H5("📌 Sua próxima aula:"),
        html.Div("15/05/2025 às 14:00",
                 style={"backgroundColor": "#f8f9fa", "padding": "12px", "borderRadius": "6px", "marginBottom": "30px"}),

        html.H5("👨‍🏫 Tutores recomendados:"),
        dbc.ListGroup([
            dbc.ListGroupItem("Ana — Inglês"),
            dbc.ListGroupItem("Carlos — Espanhol"),
            dbc.ListGroupItem("Sofia — Francês")
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(dbc.Button("⚙ Meu Perfil", href="/perfil", color="secondary", outline=True, style={"width": "100%"}), md=4),
            dbc.Col(dbc.Button("🆘 Suporte", href="/suporte", color="secondary", outline=True, style={"width": "100%"}), md=4),
            dbc.Col(dbc.Button("🚪 Sair", href="/", color="danger", outline=True, style={"width": "100%"}), md=4),
        ])
    ],
    fluid=True
)

# Callback que atualiza nome e pontos reais
@callback(
    Output("boas-vindas", "children"),
    Output("quantidade-pontos", "children"),
    Input("session-email", "data"),
    prevent_initial_call=True
)
def atualizar_home(email):
    if not email:
        return "Bem-vindo!", "Não foi possível carregar seus pontos."

    dados = buscar_dados_usuario(email)
    if dados:
        nome, pontos = dados
        return f"Olá, {nome} 👋", f"💰 Você tem {pontos} pontos disponíveis"
    else:
        return "Olá, usuário!", "💰 0 pontos"
