from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicacao rodando"

# @app.post("/api/pressaovazao")
@app.route("/api/pressaovazao", methods=['POST'])
def api_pressao_vazao():
    # Receber um JSON
    # Validar dados do JSON
    # Salvar na base
    # Retornar Sucesso ou Falha
    return "API PRESSAO VAZAO"

if __name__ == '__main__':
    app.run(debug=True)
