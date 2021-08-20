from Imports import *
from Código_Fonte import Cidadao
@app.route("/")
def padrao():
    return "backend operante"
@app.route("/ficha_cadastral")
def ficha_cadastral():
    cidadao = db.session.query(Cidadao).all()
    retorno = []
    for i in cidadao:
        retorno.append(i.json())

    listagem = jsonify(retorno)
    return listagem
app.run(debug=True)

#Basicamente o Host inteiro 