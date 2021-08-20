from ast import Num, Str
from Imports import * #Mais alguns Imports hehe

# Classe de Cadastro do cidadão
class Cidadao(db.Model):
    Cpf = db.Column(db.String, primary_key=True)
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
            "Nauseas? ": self.Nauseas,
            "Fraqueza? ": self.Fraqueza,
            "Sintomas? ": self.Sintomas
            }

# Bloqueia as seguintes funções quando importado
if __name__ == "__main__":
    
    # Apaga arquivos já existentes para que não tenha repetição de dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all() # Cria as tabelas do banco de dados

    
    
    # Inputs de informações para teste 
    p1 = Paciente(Nome_Completo = "Felipe I S Rungue", Data_Nascimento = "31/10/2001", Genero = "M", Cpf = "022.452.252-36", Email = "feliperungue@hmail.com", Senha = "Xero123", \
    Dor = True, Nauseas = False, Fraqueza = True, Sintomas = "Choro Abundante")
    
    db.session.add(p1) # Adiciona na lista de commit
    db.session.commit() # Grava os dados no banco de dados

    Info = db.session.query(Paciente).all() # Traz os dados do banco para uma lista 
    # E finalmente imprime as informações
    print("")
    for i in Info:
        print(i)
        print(i.json())
        print("")
#FIM#
    