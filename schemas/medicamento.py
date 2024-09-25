from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from model import Medicamento

class PesquisaMedicamentoId(BaseModel):
    """ Fazer a busca pelo o campo da chave
    """
    id: int
  

class PesquisaMedicamento(BaseModel):
    """ Define os campos de pesquisa
    """
    id: Optional[int] = None
    descricao: Optional[str] = None


class MedicamentoSchema(BaseModel):
    """ Define o modelo do objeto modelo para representar na tela
    """
    id: int = 1
    descricao: str = "Dores de cabeça."
    quantidade_vezes_dia: int = 2
    observacao: str = "Ingerir após as refeições."
    quantidade_dia: Optional[int] = 5
    data_inicio_medicacao: str = "0000/00/00 00:00:00"
    remedio_id: int    

class MedicamentoIncluirSchema(BaseModel):
    """ Define o modelo do objeto medicamento para representar na tela de incluir
    """
    descricao: str 
    quantidade_vezes_dia: int 
    observacao: str = ""
    quantidade_dia: Optional[int] = None
    data_inicio_medicacao: datetime 
    remedio_id: int 

class MedicamentoAlterarSchema(MedicamentoIncluirSchema):
    """ Define o modelo do objeto medicamento para representar na tela de alteração
    """
    id:int


 

class ListagemMedicamentoSchema(BaseModel):
    """ Define como uma listagem de medicamento será retornada.
    """
    item:List[MedicamentoSchema]



def medicamento_view(medicamento: Medicamento):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return {
        "data_inicio_medicacao": medicamento.data_inicio_medicacao.strftime("%Y-%m-%d %H:%M:%S"),
        "descricao": medicamento.descricao,
        "id": medicamento.id,
        "quantidade_dia": medicamento.quantidade_dia,
        "quantidade_vezes_dia": medicamento.quantidade_vezes_dia,
        "observacao": medicamento.observacao,
        "remedio_id": medicamento.remedio_id, 
        }


def medicamentos_view(itens: List[Medicamento]):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    resultado = []
    for medicamento in itens:
        resultado.append({
        "data_inicio_medicacao": medicamento.data_inicio_medicacao.strftime("%Y-%m-%d %H:%M:%S"),
        "descricao": medicamento.descricao,
        "id": medicamento.id,
        "quantidade_dia": medicamento.quantidade_dia,
        "quantidade_vezes_dia": medicamento.quantidade_vezes_dia,
        "observacao": medicamento.observacao,
         "remedio_id": medicamento.remedio_id, 
        })
    return resultado

