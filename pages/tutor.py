import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import base64
import os

dash.register_page(__name__, path="/tutor")

UPLOAD_FOLDER = "certificados"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

layout = dbc.Container(
    [
        html.H2("🎓 Seja um Tutor na Scambly", style={"marginTop": "30px", "marginBottom": "30px"}),
        html.P("Preencha o formulário abaixo para se candidatar como tutor."),

        dbc.Label("Nome Completo"),
        dbc.Input(id="tutor-nome", type="text", placeholder="Digite seu nome completo", className="mb-3"),

        dbc.Label("E-mail"),
        dbc.Input(id="tutor-email", type="email", placeholder="Digite seu e-mail", className="mb-3"),

        dbc.Label("Idiomas que você domina"),
        dbc.Input(id="tutor-idiomas", type="text", placeholder="Ex: Inglês, Espanhol", className="mb-3"),

        dbc.Label("1. Descreva sua metodologia para ensinar um aluno iniciante"),
        dcc.Textarea(id="pergunta1", placeholder="Sua resposta...", style={"width": "100%"}, className="mb-3"),

        dbc.Label("2. Como você avalia o progresso dos seus alunos?"),
        dcc.Textarea(id="pergunta2", placeholder="Sua resposta...", style={"width": "100%"}, className="mb-3"),

        dbc.Label("3. Quais ferramentas você usa para ensinar online?"),
        dcc.Textarea(id="pergunta3", placeholder="Sua resposta...", style={"width": "100%"}, className="mb-3"),

        dbc.Label("📁 Envie seus certificados de proficiência"),
        dcc.Upload(
            id="upload-certificado",
            children=html.Div(["Arraste ou clique para enviar arquivos (PDF, JPG...)"]),
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

        html.Div(id="arquivo-certificado", style={"marginBottom": "20px"}),

        dbc.Button("Enviar Candidatura", id="botao-enviar-tutor", color="primary",
                   style={"backgroundColor": "#8000ff", "border": "none"}),

        html.Div(id="mensagem-tutor", className="mt-3", style={"fontWeight": "bold"})
    ],
    style={"maxWidth": "800px", "paddingBottom": "40px"},
    fluid=True
)

@callback(
    Output("arquivo-certificado", "children"),
    Input("upload-certificado", "contents"),
    State("upload-certificado", "filename"),
    prevent_initial_call=True
)
def salvar_certificado(conteudo, nome_arquivo):
    if conteudo and nome_arquivo:
        data = conteudo.encode("utf8").split(b";base64,")[1]
        path = os.path.join(UPLOAD_FOLDER, nome_arquivo)
        with open(path, "wb") as f:
            f.write(base64.b64decode(data))
        return f"📄 Arquivo recebido: {nome_arquivo}"
    return ""

@callback(
    Output("mensagem-tutor", "children"),
    Input("botao-enviar-tutor", "n_clicks"),
    State("tutor-nome", "value"),
    State("tutor-email", "value"),
    State("tutor-idiomas", "value"),
    State("pergunta1", "value"),
    State("pergunta2", "value"),
    State("pergunta3", "value"),
    prevent_initial_call=True
)
def enviar_candidatura(n, nome, email, idiomas, r1, r2, r3):
    if not all([nome, email, idiomas, r1, r2, r3]):
        return "⚠️ Preencha todos os campos obrigatórios antes de enviar."

    # Simulação de envio — você pode salvar no banco depois
    return "✅ Sua candidatura foi enviada com sucesso! Entraremos em contato por e-mail."
