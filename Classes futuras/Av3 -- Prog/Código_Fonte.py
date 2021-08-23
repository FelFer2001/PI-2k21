from ast import Num, Str
from Imports import * #Mais alguns Imports hehe

# Classe de Cadastro do cidadão
class Cidadao(db.Model):
    Cpf = db.Column(db.String(14), primary_key=True)
    Nome_Completo = db.Column(db.String(200))
    Data_Nascimento = db.Column(db.String(100))
    Genero = db.Column(db.String(1))
    Email = db.Column(db.String(100))
    Senha = db.Column(db.String(100))
    type = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity':'Cidadão', 
        'polymorphic_on':type #definindo a variavél de herança
    }
    def __str__(self):
        return f'{self.Cpf}, {self.Nome_Completo}, {self.Data_Nascimento}, {self.Genero}, {self.Email}, {self.Senha}, {self.type}'

#Classe que representa uma clinica na vida real
class Clinica(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(200))
    Cep = db.Column(db.String(50))
    Complemento = db.Column(db.String(100))

    def __str__(self):
        return f'{str(self.Id)}, {self.Nome}, {self.Cep}, {self.Complemento}'
    
    def json(self):
        return {
            "id": self.Id,
            "nome": self.Nome,
            "Cep": self.Cep,
            "Complemento": self.Complemento,
        }

# Classe dos sintomas do paciente
class Paciente(Cidadao):
    Dor = db.Column(db.Boolean)
    Nauseas = db.Column(db.Boolean)
    Fraqueza = db.Column(db.Boolean)
    Sintomas = db.Column(db.String(100))

    __mapper_args__ = { 
        'polymorphic_identity':'Paciente', # Configura a herança 
    }    
    def __str__(self):
        return f'{super().__str__()}, {str(self.Dor)}, {str(self.Nauseas)}, {str(self.Fraqueza)}, {str(self.Sintomas)}'
    
    def json(self): # Criação do arquivo json
        return {
            "Cpf": self.Cpf,
            "Nome_completo": self.Nome_Completo,
            "Data_Nascimento": self.Data_Nascimento,
            "Gênero": self.Genero,
            "Email": self.Email,
            "Senha": self.Senha,
            "Dor? ": self.Dor,
            "Type": self.type,
            "Nauseas? ": self.Nauseas,
            "Fraqueza? ": self.Fraqueza,
            "Sintomas? ": self.Sintomas
            }

#Classe que representa um médico na vida real
class Medico(Cidadao):
    ClinicaId = db.Column(db.Integer, db.ForeignKey(Clinica.Id), nullable = True) # Chave estrangeira
    Clinica = db.relationship('Clinica') # Associação com a classe clinica
    __mapper_args__ = { 
        'polymorphic_identity':'Médico',
    }

    def __str__(self):
        return f'{super().__str__()}, {str(self.ClinicaId)}, {Clinica}, {self.type}' 

    def json(self):
        return {
            "Cpf": self.Cpf,
            "Nome_completo": self.Nome_Completo,
            "Data_Nascimento": self.Data_Nascimento,
            "Gênero": self.Genero,
            "Email": self.Email,
            "Senha": self.Senha,
            "Type": self.type,
            "ClinicaId": self.ClinicaId,
            "Clinica": self.Clinica.json() # Utilizando a função da classe Clinica
        }

class Consulta(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Data = db.Column(db.String(50))

    PacienteId = db.Column(db.String(14), db.ForeignKey(Paciente.Cpf), nullable = True) # Chave estrangeira
    Paciente = db.relationship('Paciente') # Associação com a classe Paciente

    ClinicaId = db.Column(db.Integer, db.ForeignKey(Clinica.Id), nullable = True) # Chave estrangeira
    Clinica = db.relationship('Clinica') # Associação com a classe clinica

    def __str__(self):
        return f'{str(self.Id)}, {self.Data}, {self.PacienteId}, {self.Paciente}, {self.ClinicaId}, {self.Clinica}' 

    def json(self):
        return {
            "Id": self.Id,
            "Data": self.Data,
            "PacienteId": self.PacienteId,
            "Paciente": self.Paciente.json(), # Utilizando a função da classe Paciente
            "MedicoID": self.ClinicaId,
            "Medico": self.Clinica.json(), # Utilizando a função da classe Medico
        }

# Bloqueia as seguintes funções quando importado
if __name__ == "__main__":
    
    # Apaga arquivos já existentes para que não tenha repetição de dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all() # Cria as tabelas do banco de dados
    
    # Inputs de informações para teste
    c1 = Clinica(Nome = "Clinica de Saúde", Cep = "41242121", Complemento = "Número 105")

    p1 = Paciente(Nome_Completo = "Felipe I S Rungue", Data_Nascimento = "31/10/2001", Genero = "M", Cpf = "022.452.252-36",\
        Email = "feliperungue@hmail.com", Senha = "Xero123", Dor = True, Nauseas = False, Fraqueza = True, Sintomas = "Choro Abundante")

    m1 = Medico(Nome_Completo = "Laura Zimermann", Data_Nascimento = "15/9/2001", Genero = "F", Cpf = "052.872.252-44",\
        Email = "laurazimermann@gmail.com", Senha = "SouLinda123", ClinicaId = 1, Clinica = c1)

    con1 = Consulta(Data = "22/12/2021", PacienteId = 1, Paciente = p1, ClinicaId = 1, Clinica = c1)

    db.session.add(c1) # Adiciona na lista de commit
    db.session.add(p1) # Adiciona na lista de commit
    db.session.add(m1) # Adiciona na lista de commit
    db.session.add(con1) # Adiciona na lista de commit
    db.session.commit() # Grava os dados no banco de dados

    clinicas = db.session.query(Clinica).all() # Traz os dados do banco para uma lista 
    # E finalmente imprime as informações
    print("")
    for i in clinicas:
        print(i)
        print(i.json())
        print("")

    cidadoes = db.session.query(Cidadao).all() # Traz os dados do banco para uma lista 
    # E finalmente imprime as informações
    print("")
    for i in cidadoes:
        print(i)
        print(i.json())
        print("")

    consultas = db.session.query(Consulta).all() # Traz os dados do banco para uma lista 
    # E finalmente imprime as informações
    print("")
    for i in consultas:
        print(i)
        print(i.json())
        print("")
#FIM#
    