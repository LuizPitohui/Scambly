import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import base64
import os

dash.register_page(__name__, path="/suporte")

UPLOAD_FOLDER = "suporte_arquivos"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

tipos_problema = [
    "Erro na plataforma",
    "Problema com pagamento",
    "Não consigo agendar aula",
    "Outro"
]

layout = dbc.Container(
    [
        html.H2("🆘 Suporte ao Usuário", style={"marginTop": "30px", "marginBottom": "30px"}),
        html.P("Se estiver enfrentando algum problema, envie sua solicitação abaixo."),

        dbc.Label("Nome"),
        dbc.Input(id="suporte-nome", type="text", placeholder="Seu nome completo", className="mb-3"),

        dbc.Label("E-mail"),
        dbc.Input(id="suporte-email", type="email", placeholder="seu@email.com", className="mb-3"),

        dbc.Label("Tipo de Problema"),
        dcc.Dropdown(
            id="suporte-tipo",
            options=[{"label": t, "value": t} for t in tipos_problema],
            placeholder="Selecione uma opção",
            className="mb-3"
        ),

        dbc.Label("Descreva o que está acontecendo"),
        dcc.Textarea(id="suporte-msg", placeholder="Sua mensagem...", style={"width": "100%"}, className="mb-3"),

        dbc.Label("📁 Envie um print (opcional)"),
        dcc.Upload(
            id="upload-suporte",
            children=html.Div(["Arraste ou clique para enviar um print (PNG, JPG)"]),
            style={
                "width": "100%",
                "height": "80px",
                "lineHeight": "80px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "marginBottom": "15px"
            },
            multiple=False
        ),

        html.Div(id="arquivo-suporte", style={"marginBottom": "20px"}),

        dbc.Button("Enviar Solicitação", id="botao-suporte", color="primary",
                   style={"backgroundColor": "#8000ff", "border": "none"}),

        html.Div(id="mensagem-suporte", className="mt-3", style={"fontWeight": "bold"})
    ],
    style={"maxWidth": "800px", "paddingBottom": "40px"},
    fluid=True
)

@callback(
    Output("arquivo-suporte", "children"),
    Input("upload-suporte", "contents"),
    State("upload-suporte", "filename"),
    prevent_initial_call=True
)
def salvar_print(conteudo, nome_arquivo):
    if conteudo and nome_arquivo:
        data = conteudo.encode("utf8").split(b";base64,")[1]
        path = os.path.join(UPLOAD_FOLDER, nome_arquivo)
        with open(path, "wb") as f:
            f.write(base64.b64decode(data))
        return f"📄 Print recebido: {nome_arquivo}"
    return ""

@callback(
    Output("mensagem-suporte", "children"),
    Input("botao-suporte", "n_clicks"),
    State("suporte-nome", "value"),
    State("suporte-email", "value"),
    State("suporte-tipo", "value"),
    State("suporte-msg", "value"),
    prevent_initial_call=True
)
def enviar_solicitacao(n, nome, email, tipo, msg):
    if not all([nome, email, tipo, msg]):
        return "⚠️ Por favor, preencha todos os campos obrigatórios."

    # Simulação — salvar no banco ou enviar para equipe no futuro
    return "✅ Sua solicitação foi enviada! Responderemos por e-mail em breve."
