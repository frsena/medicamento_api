from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS


info = Info(title="Cadastro de Remedio", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)


import documentacao_service 
import medicamento_service

app.run(port=5001, debug=True)