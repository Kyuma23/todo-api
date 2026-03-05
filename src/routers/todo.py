from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import SQLModel, Session, select, Field
from src.db import engine, Tarefa


router = APIRouter(prefix="/tarefas", tags=["Arquivo de tarefas"])

class TarefaBase(SQLModel):
    titulo : str = Field(
        max_length = 100
        )
    descricao : str | None
    concluida : bool = False

def get_session():
    with Session(engine) as session:
        yield session


@router.post("/", response_model= Tarefa)
def newTarefa(tarefa:TarefaBase, session: Session = Depends(get_session)):
    db_tarefa= Tarefa.model_validate(tarefa)

    session.add(db_tarefa)
    session.commit()
    session.refresh(db_tarefa)
     
    # Devolvemos apenas a tarefa gravada.
    return db_tarefa


@router.get("/", response_model=list[Tarefa])
def getAllTarefas(session: Session = Depends(get_session)):
    stmt = select(Tarefa)

    todas_as_tarefas = session.exec(stmt).all()

    return todas_as_tarefas

@router.put("/{id}")
def concluir_tarefa(id : int, session: Session = Depends(get_session)):
    tarefa = session.get(Tarefa, id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada na base de dados")

    tarefa.concluida = True

    session.add(tarefa)
    session.commit()
    session.refresh(tarefa)

    return {"mensagem": "Tarefa concluida com sucesso"}

@router.delete("/{id}")
def delete_tarefa(id: int, session: Session = Depends(get_session)):
    tarefa = session.get(Tarefa, id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada na base de dados")

    session.delete(tarefa)
    session.commit()

    return {"mensagem": "Tarefa eliminada com sucesso"}
    
