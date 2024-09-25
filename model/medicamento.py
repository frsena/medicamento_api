from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Medicamento(Base):
    __tablename__ = 'medicamento'

    id = Column("id", Integer, primary_key=True)
    descricao = Column(String(100))
    quantidade_vezes_dia = Column(Integer) 
    observacao = Column(String(150))
    quantidade_dia = Column(Integer)
    data_inicio_medicacao = Column(DateTime, default=datetime.now())
    data_insercao = Column(DateTime, default=datetime.now())
    remedio_id = Column(Integer, nullable=False)

    def __init__(self, descricao:str, quantidade_vezes_dia:int, data_inicio_medicacao:DateTime, remedio_id:int,
                  quantidade_dia:int,  observacao:str, data_insercao:Union[DateTime, None] = None):
    
        self.descricao = descricao
        self.quantidade_vezes_dia = quantidade_vezes_dia
        self.observacao = observacao
        self.data_inicio_medicacao = data_inicio_medicacao
        self.quantidade_dia = quantidade_dia
        self.remedio_id = remedio_id
        if data_insercao:
            self.data_insercao = data_insercao



