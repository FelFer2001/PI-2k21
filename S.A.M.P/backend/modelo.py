from ast import Num
from config import *

# Classe pai para funcionário e cidadão
class Pessoa(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    NomeCompleto = db.Column(db.String(200))
    DtNascimento = db.Column(db.String(100))
    Genero = db.Column(db.String(1))
    Cpf = db.Column(db.String(100))
    Cep = db.Column(db.String(100))
    Complemento = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Senha = db.Column(db.String(100))
    Type = db.Column(db.String(50)) # Discriminador
    __mapper_args__ = {
        'polymorphic_identity':'Pessoa', 
        'polymorphic_on':Type # nome do campo que vincula os filhos
    }
    def __str__(self):
        return f'{self.Id}, {self.NomeCompleto}, {self.DtNascimento}, {self.Genero}, {self.Cpf},{self.Cep}, {self.Complemento}, {self.Email}, {self.Senha}'

    def json(self):
        return{
            "Id": self.Id,
            "NomeCompleto": self.NomeCompleto,
            "DtNascimento": self.DtNascimento,
            "Genero": self.Genero,
            "Cpf": self.Cpf,
            "Cep": self.Cep,
            "Complemento": self.Complemento,
            "Email": self.Email,
            "Senha": self.Senha

        }
class Paciente(Pessoa):
    NomePai = db.Column(db.String(50))
    NomeMae = db.Column(db.String(50))
    DoencaHereditaria = db.Column(db.String(200))
    Sintomas = db.Column(db.String(200))
    Tipo_Sanguineo = db.Column(db.String(200))
    __mapper_args__ = { 
        'polymorphic_identity':'Paciente',
    }

    # Formatação do print no terminal
    def __str__(self):
        return f'{super().__str__()}, {self.NomePai}, {self.NomeMae}, {self.DoencaHereditaria}, {self.Sintomas}, {self.Tipo_Sanguineo}'

    def json(self):
        return{
        "Pessoa": super().json(),
        "NomePai": self.NomePai,
        "NomeMae": self.NomeMae,
        "DoencaHereditaria": self.DoencaHereditaria,
        "Sintomas": self.Sintomas,
        "Tipo_Sanguineo": self.Tipo_Sanguineo
        }



class Medico(Pessoa):
    Crm = db.Column(db.String(100))
    Area_Atuacao = db.Column(db.String(100))
    Especialidade = db.Column(db.String(100))
    __mapper_args__ = { 
        'polymorphic_identity':'Medico',
    }

    # Formatação do print no terminal
    def __str__(self):
        return f'{super().__str__()}, {self.Crm}, {self.Area_Atuacao}, {self.Especialidade}'
    
    # Criando arquivo Json para envio
    def json(self):
        return {
            "Pessoa": super().json(),
            "Crm": self.Crm,
            "Area_Atuacao": self.Area_Atuacao,
            "Especialidade": self.Especialidade 
        }    

# Bloqueia as seguintes funções quando importado
if __name__ == "__main__":
    
    # Apaga arquivos já existentes para que não tenha repetição de dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all() # Cria as tabelas do banco de dados

    # Inputs de informações
    us1 = Paciente(NomeCompleto = "Zofia Cringe ", DtNascimento = "2000-06-29", Genero = "F", Cpf = "696.696.696-69", Cep = "69696-696", Complemento = "Posto Ipiranga",
    Email = "ZofiaCringe@gmail.com", Senha = "Zofia69", NomePai = "Jacir", NomeMae = "Graziela", DoencaHereditaria = "Transtorno Psiquiatrico",
    Sintomas = "Fraqueza e suor frio", Tipo_Sanguineo = "A-")

    med1 = Medico(NomeCompleto = "Daniel Passos Barroso", DtNascimento = "1996-10-29", Genero = "M", Cpf = "545.454.654-69", Cep = "40002-892", Complemento = "Banco Itáu",
    Email = "DanielBarroso@gmail.com", Senha = "Barros123", Crm = "SC - 9230", Area_Atuacao = "Adolescência", Especialidade = "Sexologia")


    
    # Adiciona na lista de commit
    db.session.add(us1)
    db.session.add(med1)

    db.session.commit() # Grava os dados no banco de dados

    TodosPessoa = db.session.query(Pessoa).all() # Traz os dados do banco para uma lista 
    # Imprime as informações
    print("")
    for i in TodosPessoa:
        print(i)
        print(i.json())
        print("")
