from sqlalchemy import or_, and_
from sqlalchemy.exc import IntegrityError
from typing import Optional

from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from model import Session, Medicamento

from app import app
from schemas import *

medicamento_tag = Tag(name="Crontrole de Medicamento", description="Cadastrar do medicação diaria para um melhor controle")


@app.get('/medicamento', tags=[medicamento_tag],
         responses={"200": MedicamentoSchema, "404": ErrorSchema})
def busca_id(query: PesquisaMedicamentoId):
    """ Busca o medicamento pelo codigo
    """
    id = query.id
    session = Session()
    med = session.query(Medicamento).filter(Medicamento.id == id).first()

    if not med:
        error_msg = "Não foi encontrado nenhum medicamento."
        return {"mesage": error_msg}, 404
    else :
        return medicamento_view(med)
    
@app.get('/medicamentos', tags=[medicamento_tag],
         responses={"200": ListagemMedicamentoSchema, "404": ErrorSchema})
def busca_todos_medicamentos():
    """ Retorna todos os medicamentos cadastrados
    """
    session = Session()
    medicamentos = session.query(Medicamento).all()

    if not medicamentos:
        return [], 200
    else:
        return medicamentos_view(medicamentos), 200
    


@app.get('/pesquisa', tags=[medicamento_tag],
         responses={"200": ListagemMedicamentoSchema, "400": ErrorSchema})
def pesquisa_medicamento(query: PesquisaMedicamento):
    """ pesquisa o medicamento pelo codigo e pela descrição, caso não passe nenhum parametro retorna a lista toda
    """
    session = Session()
    filters = []

    if query.id:
        filters.append(Medicamento.id == query.id)
    if query.descricao:
        filters.append(Medicamento.descricao.ilike(f"%{query.descricao}%"))
       
    medicamento = session.query(Medicamento).filter(and_(*filters)).all()

    if not medicamento:
        error_msg = "Não foi encontrado nenhum medicamento."
        return {"mesage": error_msg}, 400
    else :
        return medicamentos_view(medicamento), 200


@app.post('/medicamento', tags=[medicamento_tag],
         responses={"200": MedicamentoSchema, "400": ErrorSchema})
def adicionar(form: MedicamentoIncluirSchema):
    """ adiciona um medicamento novo
    """
    
    medicamento = Medicamento(form.descricao, form.quantidade_vezes_dia, 
                              form.data_inicio_medicacao, form.remedio_id, 
                              form.quantidade_dia, form.observacao) 
    try:
        session = Session()
        session.add(medicamento)
        session.commit()

        return medicamento_view(medicamento)
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo medicamento."
        return {"mesage": error_msg}, 400   



@app.delete('/delete', tags=[medicamento_tag],
         responses={"200": ErrorSchema, "404": ErrorSchema})
def deletar(query: PesquisaMedicamentoId):
    """ deletar um medicamento cadastrado
    """
    id = query.id
    session = Session()
    count = session.query(Medicamento).filter(Medicamento.id == id).delete()
    session.commit()

    if count:
        msg = "Medicamento foi excluido com sucesso."
        return {"mesage": msg}, 200
    else :
        error_msg = "Não foi encontrado nenhum medicamento."
        return {"mesage": error_msg}, 404
    

    
@app.put('/atualizar', tags=[medicamento_tag],
         responses={"200": MedicamentoSchema, "400": ErrorSchema})
def atualizar(form: MedicamentoAlterarSchema):
    """ atualizar um medicamento cadastrado
    """
    id = form.id
    session = Session()
    medicamento = session.query(Medicamento).filter(Medicamento.id == id).first()
    try:
    
        if not medicamento:
            error_msg = "Não foi possível atualizar o medicamento."
            return {"mesage": error_msg}, 400
        
        medicamento.descricao = form.descricao
        medicamento.quantidade_vezes_dia = form.quantidade_vezes_dia
        medicamento.data_inicio_medicacao = form.data_inicio_medicacao
        medicamento.remedio_id = form.remedio_id
        medicamento.quantidade_dia = form.quantidade_dia 
        medicamento.observacao = form.observacao

        session.add(medicamento)
        session.commit()

        return medicamento_view(medicamento)
        
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível atualizar o medicamento."
        return {"mesage": error_msg}, 400 