from sqlalchemy import Column, String, Integer, Float
from  models import Base

class Paciente(Base):

    # Comentário de aula: a tabela no banco pode seguir um menemônico e 
    # ter um nome diferente do que poderia ser "mais apropriado". Aqui 
    # a tabela que vai representar o Paciente, se chama 'Paciente_catalog',
    # supondo o cenário em que o sufixo "catalog" é utilizado para 
    # indicar que é uma tabela de catálogo de Pacientes.
    __tablename__ = 'Paciente_list'

    # O nome de uma coluna também pode ter no banco um nome diferente
    # como é apresentado aqui no caso do Paciente.id que no banco será 
    # Paciente_catalog.pk_prod, o sufixo pk está sendo utilizado para 
    # indicar que é uma chave primária

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender = Column(String())
    chestpain =  Column(Integer())
    restingBP =  Column(Integer())
    serumcholestrol = Column(Integer())
    fastingbloodsugar = Column(Integer())
    restingrelectro = Column(Integer())
    maxheartrate = Column(Integer())
    exerciseangia = Column(Integer())
    oldpeak = Column(Float())
    slope = Column(Integer())
    noofmajorvessels = Column(Integer())
    target = Column(Integer())


    def __init__(self, age, gender, chestpain, restingBP, serumcholestrol, fastingbloodsugar, restingrelectro, maxheartrate, exerciseangia, oldpeak, slope, noofmajorvessels, target):
        """
        Cria um Paciente

        Arguments:
            age: nome do prmaxheartrater de serviço.
            gender: gender do autonomo
            chestpain: chestpain do endereço dele
            restingBP: endereço dele
            serumcholestrol: número da casa dele
            fastingbloodsugar: fastingbloodsugar onde ele mora
            restingrelectro: restingrelectro onde mora o prmaxheartrater de serviço
            maxheartrate: maxheartrate onde ele mora e presta o serviço
            exerciseangia: nome do serviço  
            oldpeak: descrição do serviço oferecido
            slope: noofmajorvessels do autônomo
            noofmajorvessels: noofmajorvessels do paciente
            target: target do paciente

        """
        self.age = age
        self.gender = gender
        self.chestpain = chestpain
        self.restingBP = restingBP
        self.serumcholestrol = serumcholestrol
        self.fastingbloodsugar = fastingbloodsugar
        self.restingrelectro = restingrelectro
        self.maxheartrate = maxheartrate        
        self.exerciseangia = exerciseangia
        self.oldpeak = oldpeak  
        self.slope = slope     
        self.noofmajorvessels = noofmajorvessels
        self.target = target
        

    def to_dict(self):
        """
        Retorna a representação em dicionário do Objeto Paciente.
        """
        return{
            "id": self.id,
            "age": self.age,
            "gender": self.gender,
            "chestpain": self.chestpain,
            "restingBP": self.restingBP,
            "serumcholestrol": self.serumcholestrol,
            "fastingbloodsugar": self.fastingbloodsugar,
            "restingrelectro": self.restingrelectro,
            "maxheartrate": self.maxheartrate,
            "exerciseangia": self.exerciseangia,
            "oldpeak": self.oldpeak,
            "slope": self.slope,
            "noofmajorvessels": self.noofmajorvessels,
            "target" : self.target
        }

    def __repr__(self):
        """
        Retorna uma representação do Paciente em forma de texto.
        """
        return f"Paciente(id={self.id}, age='{self.age}', gender={self.gender}, chestpain='{self.chestpain}', restingBP='{self.restingBP}', serumcholestrol='{self.serumcholestrol}', fastingbloodsugar='{self.fastingbloodsugar}', restingrelectro='{self.restingrelectro}', maxheartrate='{self.maxheartrate}', exerciseangia='{self.exerciseangia}',  oldpeak='{self.oldpeak}', slope='{self.slope}',  noofmajorvessels='{self.noofmajorvessels}',  target='{self.target}')"    
