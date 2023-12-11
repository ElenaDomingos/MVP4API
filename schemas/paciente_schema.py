from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

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
    """Define como um paciente será retornado
    """
    id: int = 1
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
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    id: int = 1

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    id: int = 1
    
# Apresenta apenas os dados de um paciente    
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
        "fastingbloodsugar": paciente.fastingbloodsugar,
        "restingrelectro": paciente.restingrelectro,            
        "maxheartrate": paciente.maxheartrate,            
        "exerciseangia": paciente.exerciseangia,
        "oldpeak": paciente.oldpeak, 
        "slope": paciente.slope,   
        "noofmajorvessels" : paciente.noofmajorvessels,
        "target": paciente.target
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
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

