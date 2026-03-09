from sqlmodel import Field, SQLModel, create_engine, Session, text
from pydantic import BaseModel, field_validator
from dotenv import load_dotenv
import os

class Tarefa(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    titulo : str = Field(
        nullable = False,
        max_length = 100
        )
    descricao : str | None
    concluida : bool = False

load_dotenv()

db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise ValueError("DATABASE_URL is not set in the .env file!")


engine = create_engine(db_url)

def test_connection():
    try:
        with Session(engine) as session:
            result = session.exec(text("SELECT 1")).first()
            print("Successfully connected to PostgreSQL! Result:", result)
    except Exception as e:
        print("Failed to connect:", e)

def init_db():
    SQLModel.metadata.create_all(engine)
    test_connection()

if __name__ == "__main__":
    init_db()
