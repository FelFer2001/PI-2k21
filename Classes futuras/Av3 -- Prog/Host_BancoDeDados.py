from Imports import *
from Código_Fonte import Cidadao, Clinica, Consulta

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

@app.route("/lista_clinicas")
def lista_clinicas():
    clinica = db.session.query(Clinica).all()
    retorno = []
    for i in clinica:
        retorno.append(i.json())

    listagem = jsonify(retorno)
    return listagem

@app.route("/lista_consultas")
def lista_consultas():
    consultas = db.session.query(Consulta).all()
    retorno = []
    for i in consultas:
        retorno.append(i.json())

    listagem = jsonify(retorno)
    return listagem

app.run(debug=True)

#Basicamente o Host inteiro 