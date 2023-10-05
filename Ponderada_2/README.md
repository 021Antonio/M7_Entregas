
# API

### <b>Motivação</b> </h3>


Fiz a reconstrução do projeto ponderado 2 para melhorá-lo. Em vez de utilizar o Flask como API, optei por usar o FastAPI para padronizar, já que a ponderada 4, como base, utiliza o FastAPI.


### <b>Como utilizar</b> </h3>

#### Rodando localmente sem o docker

O primeiro passo, é criar um ambiente virtual para instalar as bibliotecas necessarias. Para isso, basta utilizar o comando
 
```
python -m venv venv
```
Apois isso, dirija-se para a pasta venv/Scripts e utilize o comando

```
cd venv
cd Scripts
activate
```
Pronto, sua venv está funcionando. Agora, basta instalar as bibliotecas necessarias. Para isso, utilize o comando

```
pip instsall -r requirements.txt

```
 Este comando irá instalar todas as bibliotecas utilizadas a partir de um arquivo chamado requirements.txt, que contém todas as bibliotecas necessárias para executar o projeto.

### Principais bibliotecas utilizadas

" API utiliza o FastAPI, um microframework para Python, e como banco de dados, utilizei o SQLAlchemy. Além disso, estamos usando o Uvicorn, um servidor ASGI de alto desempenho, para executar a API.


### <b>Pastas</b> </h3>

A estrutura de pastas separa o banco de dados e o html da aplicação. 

A pasta model, contem o banco de dados. O arquivo "base.py" contem a estrutura do banco de dados, e o arquivo "model.py" contem as tabelas do banco de dados.

A pasta templates contem o html da aplicação. O arquivo "index.html" contem a pagina inicial da aplicação.

### <b>Sobre a api</b> </h3>

Aqui importamos as bibliotecas necessarias para rodar a aplicação


```
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse 
import uvicorn #
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

```
Aqui criamos o banco de dados e a sessão

```
DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()
```
Nesta parte, criamos a estrutura do banco de dados

```
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

app = FastAPI()
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


```

Nesta parte, temos as rotas da aplicação

```
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
    return "Credenciais inválidas. Tente novamente."

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


```

### Construindo uma imagem docker

O primeiro passo, é criar um arquivo chamado "requeriments.txt" na pasta "APP" ,Para isso, basta utilizar o comando
 
``` 
pip install > requirements.txt

```
Ele ira baixar todas as bibliotecas necessarias. Um ponto negativo, é que ele irá baixar algumas coisas que necessariamente não são necessarias, mas não tem problema.
Caso deseje escrever as dependencias manualmente, basta escrever as bibliotecas no arquivo "requirements.txt".
Por exemplo:
    
    ```
    fastapi
    uvicorn
    ...
    sqlalchemy
    ```

Apos gerar o requiremnets.txt, basta criar um arquivo chamado "Dockerfile" na pasta "APP".
```
FROM python:3.10

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

EXPOSE 8000
```

Criando os arquivos, estamos prontos para criar nossa imagem.
Para isso, utilizamos o comando

```
docker build -t nome_da_imagem .
```
Apos isso, rodamos nossa imagem com o comando
    
    ```
    docker run -d -p 8000:8000 nome_da_imagem
    ```
e pronto, nossa imagem está rodando.

### Docker compose


<h1>EM Construção....



