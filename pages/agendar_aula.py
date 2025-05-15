import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from datetime import date, timedelta

dash.register_page(__name__, path="/agendar-aula")

# Dados simulados
idiomas = ["Inglês", "Espanhol", "Francês", "Alemão"]
tutores_disponiveis = {
    "Inglês": ["Ana", "Bruno"],
    "Espanhol": ["Carlos"],
    "Francês": ["Sofia"],
    "Alemão": ["Lukas"]
}
horarios = ["09:00", "10:00", "14:00", "16:00", "18:00"]

layout = dbc.Container(
    [
        html.H2("📅 Agendar Aula", className="mb-4", style={"marginTop": "30px"}),

        dbc.Row([
            dbc.Col([
                dbc.Label("Idioma desejado"),
                dcc.Dropdown(
                    id="dropdown-idioma",
                    options=[{"label": i, "value": i} for i in idiomas],
                    placeholder="Selecione um idioma"
                )
            ], md=6),

            dbc.Col([
                dbc.Label("Tutor disponível"),
                dcc.Dropdown(id="dropdown-tutor", placeholder="Selecione um tutor")
            ], md=6)
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                dbc.Label("Data"),
                dcc.DatePickerSingle(
                    id="date-picker",
                    min_date_allowed=date.today(),
                    max_date_allowed=date.today() + timedelta(days=30),
                    placeholder="Escolha uma data"
                )
            ], md=6),

            dbc.Col([
                dbc.Label("Horário"),
                dcc.Dropdown(
                    id="dropdown-horario",
                    options=[{"label": h, "value": h} for h in horarios],
                    placeholder="Escolha um horário"
                )
            ], md=6)
        ], className="mb-4"),

        dbc.Button("Confirmar Agendamento", id="botao-agendar", color="primary",
                   style={"backgroundColor": "#8000ff", "border": "none", "marginTop": "20px"}),

        html.Div(id="mensagem-agendamento", className="mt-4", style={"fontWeight": "bold"})
    ],
    style={"maxWidth": "800px", "paddingBottom": "40px"},
    fluid=True
)

@callback(
    Output("dropdown-tutor", "options"),
    Input("dropdown-idioma", "value")
)
def atualizar_tutores(idioma):
    if idioma and idioma in tutores_disponiveis:
        return [{"label": t, "value": t} for t in tutores_disponiveis[idioma]]
    return []

@callback(
    Output("mensagem-agendamento", "children"),
    Input("botao-agendar", "n_clicks"),
    State("dropdown-idioma", "value"),
    State("dropdown-tutor", "value"),
    State("date-picker", "date"),
    State("dropdown-horario", "value"),
    prevent_initial_call=True
)
def confirmar_agendamento(n_clicks, idioma, tutor, data, horario):
    if not all([idioma, tutor, data, horario]):
        return "⚠️ Preencha todos os campos para agendar a aula."

    return f"✅ Aula de {idioma} com {tutor} agendada para {data} às {horario}!"
