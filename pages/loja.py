import dash
from dash import html, callback, Output, Input
import dash_bootstrap_components as dbc
from dash import ctx

dash.register_page(__name__, path="/loja")

# Pacotes de pontos simulados
pacotes = [
    {"id": "p1", "pontos": 100, "preco": "R$ 24,99"},
    {"id": "p2", "pontos": 250, "preco": "R$ 59,90"},
    {"id": "p3", "pontos": 500, "preco": "R$ 118,70"},
    {"id": "p4", "pontos": 1000, "preco": "R$ 229,90"},
]

# Pacote temporariamente selecionado (em memória)
selected_package = {"pontos": 0}

# Função que gera um card para cada pacote
def gerar_card(pacote):
    return dbc.Card(
        dbc.CardBody([
            html.H4(f"{pacote['pontos']} Pontos", className="card-title"),
            html.H5(pacote['preco'], className="card-subtitle mb-2 text-muted"),
            dbc.Button("Comprar", id=f"btn-{pacote['id']}", n_clicks=0,
                       color="primary", style={"backgroundColor": "#8000ff", "border": "none"})
        ]),
        style={"marginBottom": "20px", "textAlign": "center"}
    )

# Layout da loja
layout = dbc.Container(
    [
        html.H2("🛒 Loja de Pontos", style={"marginTop": "30px", "marginBottom": "30px"}),

        dbc.Row([dbc.Col(gerar_card(p), md=3) for p in pacotes]),

        # Modal de confirmação
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Confirmar Compra")),
                dbc.ModalBody(id="modal-body-compra"),
                dbc.ModalFooter([
                    dbc.Button("Confirmar", id="confirmar-compra", color="success"),
                    dbc.Button("Cancelar", id="cancelar-compra", color="secondary", className="ms-2"),
                ])
            ],
            id="modal-compra",
            is_open=False,
            centered=True
        ),

        # Mensagem visual
        html.Div(id="mensagem-compra", style={"marginTop": "20px", "fontWeight": "bold"})
    ],
    fluid=True
)

@callback(
    Output("modal-compra", "is_open"),
    Output("modal-body-compra", "children"),
    Output("mensagem-compra", "children"),
    Input("btn-p1", "n_clicks"),
    Input("btn-p2", "n_clicks"),
    Input("btn-p3", "n_clicks"),
    Input("btn-p4", "n_clicks"),
    Input("confirmar-compra", "n_clicks"),
    Input("cancelar-compra", "n_clicks"),
    Input("modal-compra", "is_open"),
    prevent_initial_call=True
)
def controlar_modal(n1, n2, n3, n4, n_confirmar, n_cancelar, modal_aberto):
    triggered_id = ctx.triggered_id

    for p in pacotes:
        if triggered_id == f"btn-{p['id']}":
            selected_package["pontos"] = p["pontos"]
            texto = f"Você deseja comprar {p['pontos']} pontos por {p['preco']}?"
            return True, texto, ""

    if triggered_id == "confirmar-compra":
        return False, "", f"✅ Você comprou {selected_package['pontos']} pontos (simulado)."

    if triggered_id == "cancelar-compra":
        return False, "", "❌ Compra cancelada."

    return modal_aberto, "", ""