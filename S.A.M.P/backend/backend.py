import re
from flask.templating import render_template
from sqlalchemy.sql.elements import Null

from werkzeug.utils import secure_filename
from config import *
from modelo import Pessoa, Paciente, Medico
@app.route("/")
def padrao():
    return "backend operante"

@app.route("/listar_pessoas")
def listar_pessoas():
    pessoas = db.session.query(Pessoa).all()
    retorno = []
    for i in pessoas:
        retorno.append(i.json())

    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/incluir_paciente", methods=['post'])
def incluir_paciente():
    # Resposta
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # Receptor de informações
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    # Procura erros 
    semErro = True
    try: # tentar executar a operação
        # Puxa os dados do BD para verificar o CPF
        TodasPessoas = db.session.query(Pessoa).all()
        for i in TodasPessoas:
            # CPF existe = erro
            if i.Cpf == dados['Cpf']:
                resposta = jsonify({"resultado": "CPF", "detalhes": "CPF duplicado"})
                semErro = False
        # Caso a operação não tenha erros, faz o registro
        if semErro == True:
            nova = Paciente(**dados) # criar conta nova
            db.session.add(nova) # adicionar no BD
            db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder

@app.route("/incluir_medico", methods=['post'])
def incluir_medico():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    # Variavel que identifica se tem erros
    semErro = True
    try: # tentar executar a operação
        # Recuperando dados do banco para fazer validação do CPF
        TodasPessoas = db.session.query(Pessoa).all()
        for i in TodasPessoas:
            # Caso o CPF passado já exista no sistema, muda a variavel semErro para False
            if i.Cpf == dados['Cpf']:
                resposta = jsonify({"resultado": "CPF", "detalhes": "CPF duplicado"})
                semErro = False
        # Caso a operação não tenha erros, faz o registro
        if semErro == True:
            nova = Medico(**dados) # criar conta nova
            db.session.add(nova) # adicionar no BD
            db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder
app.run(debug=True)