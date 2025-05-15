import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from database.db_handler import criar_tabela_usuarios
import flask

criar_tabela_usuarios()

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True  # ✅ isso permite callbacks com IDs que aparecem depois
)

criar_tabela_usuarios()

app.layout = html.Div([
    dcc.Store(id="session-email", storage_type="session"),  # ← guarda e-mail do login
    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True)

@app.server.route("/uploads/<filename>")
def baixar_arquivo(filename):
    return flask.send_from_directory("uploads", filename)

import flask

@app.server.route("/certificados/<filename>")
def baixar_certificado(filename):
    return flask.send_from_directory("certificados", filename)
