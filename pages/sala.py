import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import base64
import datetime
import os

dash.register_page(__name__, path="/sala")

# Pasta de uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Layout principal
layout = dbc.Container(
    [
        html.H2("🎓 Sala de Aula", style={"marginTop": "30px", "marginBottom": "30px"}),

        dbc.Row([
            # VIDEO
            dbc.Col([
                html.H5("Videochamada"),
                html.Iframe(
                    src="https://meet.jit.si/ScamblyAulaDemo",
                    style={"width": "100%", "height": "400px", "border": "1px solid #ccc"}
                )
            ], md=6),

            # CHAT + MATERIAIS
            dbc.Col([
                # Chat
                html.H5("💬 Chat de Texto"),
                dcc.Textarea(
                    id="mensagem-chat",
                    placeholder="Digite sua mensagem...",
                    style={"width": "100%", "height": "100px"}
                ),
                dbc.Button("Enviar", id="botao-chat", color="primary", className="mt-2",
                           style={"backgroundColor": "#8000ff", "border": "none"}),
                html.Div(id="chat-historico", className="mt-3",
                         style={"height": "200px", "overflowY": "scroll", "backgroundColor": "#f8f9fa",
                                "padding": "10px", "border": "1px solid #ccc", "borderRadius": "5px"}),

                html.Hr(),

                # Materiais
                html.H5("📁 Materiais da Aula"),
                dcc.Upload(
                    id="upload-material",
                    children=html.Div(["Arraste ou clique para enviar arquivos"]),
                    style={
                        "width": "100%",
                        "height": "80px",
                        "lineHeight": "80px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                        "marginBottom": "10px"
                    },
                    multiple=False
                ),
                html.Div(id="lista-arquivos")
            ], md=6)
        ])
    ],
    fluid=True
)

# Armazena histórico temporariamente
chat_log = []

@callback(
    Output("chat-historico", "children"),
    Input("botao-chat", "n_clicks"),
    State("mensagem-chat", "value"),
    prevent_initial_call=True
)
def atualizar_chat(n, mensagem):
    if mensagem:
        agora = datetime.datetime.now().strftime("%H:%M")
        chat_log.append(f"[{agora}] {mensagem}")
    return html.Ul([html.Li(m) for m in chat_log])
