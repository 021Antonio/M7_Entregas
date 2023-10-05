from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados (SQLite neste exemplo)
DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

app = FastAPI()
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
async def read_root():
    return FileResponse('templates/index.html')
    # return RedirectResponse(url="/index.html")

# Rota para criar um novo usuário
@app.post("/create_user", tags=["posts"])
def create_user(username: str, password: str):
    session = SessionLocal()
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    session.close()
    return "Criado com sucesso."

# Rota para realizar o login (apenas verifica se o usuário existe, não faz autenticação real neste exemplo)
@app.post("/login", tags=["posts"])
def login(username: str, password: str):
    session = SessionLocal()
    user = session.query(User).filter(User.username == username).first()
    session.close()
    if user:
        return {"message": "Login bem-sucedido para o usuário: {}".format(username)}
    else:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
