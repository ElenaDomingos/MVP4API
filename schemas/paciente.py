from pydantic import BaseModel
from typing import Optional, List
from models.paciente import Paciente


class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    age: int = 42
    gender: str = '1'
    chestpain: int = 2
    restingBP: int = 123
    serumcholestrol: int = 0
    fastingbloodsugar: int = 1
    restingrelectro: int = 0
    maxheartrate: int = 147
    exerciseangia = 0
    oldpeak: float = 5.3
    slope: int = 3
    noofmajorvessels: int = 3
    target: int = 1


class PacienteViewSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    age: int = 42
    gender: str = '1'
    chestpain: int = 2
    restingBP: int = 123
    serumcholestrol: int = 0
    fastingbloodsugar: int = 1
    restingrelectro: int = 0
    maxheartrate: int = 147
    exerciseangia = 0
    oldpeak: float = 5.3
    slope: int = 3
    noofmajorvessels: int = 3
    target: int = 1 


class PacienteBuscaPorIdSchema(BaseModel):
    """ Define como deve ser a eintutura que representa a busca. Que será
        feita apenas com base no ID do paciente.
    """
    id: Optional[int] = 1

class ListagemPacientesSchema(BaseModel):
    """ Define como uma listagem de pacientes será retornada.
    """
    pacientes:List[PacienteSchema]


def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        ListagemPacientesSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "age": paciente.age,
            "gender": paciente.gender,
            "chestpain": paciente.chestpain,        
            "restingBP": paciente.restingBP,    
            "serumcholestrol": paciente.serumcholestrol,
            "fastingbloodsugar": paciente.fastingbloodsugar,
            "restingrelectro": paciente.restingrelectro,            
            "maxheartrate": paciente.maxheartrate,            
            "exerciseangia": paciente.exerciseangia,
            "oldpeak": paciente.oldpeak, 
            "slope": paciente.slope,   
            "noofmajorvessels" : paciente.noofmajorvessels,
            "target": paciente.target
        })

    return {"pacientes": result}


class pacienteDelSchema(BaseModel):
    """ Define como deve ser a eintutura do dado retornado após uma requisição
        de remoção.
    """
    message: int
    id: int


def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "age": paciente.age,
        "gender": paciente.gender,
        "chestpain": paciente.chestpain,
        "restingBP": paciente.restingBP,
        "serumcholestrol": paciente.serumcholestrol,
        "restingrelectro": paciente.restingrelectro,
        "maxheartrate" : paciente.maxheartrate,
        "exerciseangia": paciente.exerciseangia,
        "oldpeak": paciente.oldpeak,
        "slope": paciente.slope,     
        "noofmajorvessels" : paciente.noofmajorvessels,
        "target": paciente.target
    }
