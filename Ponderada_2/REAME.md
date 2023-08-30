# API

### <b>Motivação</b> </h3>

A api utilizada foi o FLask. Utilizei como base uma ponderada e prova referente ao modulo 5. 


### <b>Como utilizar</b> </h3>

A API utiliza o Flask, que é um microframework para Python e como banco de dados, utilizei SQLAlchemy. Para instalar o Flask, basta utilizar o comando

```
pip install Flask
pip install SQLAlchemy
```
 Pronto, agora esta tudo certo para rodar o projeto. 


### <b>Pastas</b> </h3>

A estrutura de pastas separa o banco de dados e o html da aplicação. 

A pasta model, contem o banco de dados. O arquivo "base.py" contem a estrutura do banco de dados, e o arquivo "model.py" contem as tabelas do banco de dados.

A pasta templates contem o html da aplicação. O arquivo "index.html" contem a pagina inicial da aplicação.

### <b>Sobre a api</b> </h3>

Aqui importamos o Flask e p render_template, que seria a biblioteca para gerar o nossa pagina html

```
from flask import Flask, render_template
```
Iniciamos a aplicação

```
app = Flask(__name__)
```
Nesta parte, chamo o banco de dados e crio a sessão

```
engine = create_engine('sqlite:///database.db')
#Identificando a rota onde o banco de dados será criado

Session = sessionmaker(bind=engine)
#Criando a sessão

session = Session()
#Iniciando a sessão

Base.metadata.create_all(engine)
#Criando o banco de dados

```

Aqui criamos a rota para a pagina inicial, que seria o index.html

```
@app.route('/')
def index():
    return render_template('index.html')
```
Criando uma rota para verificar o login existe no banco de dados

```
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']
    
    
    user = session.query(UserBase).filter_by(name=name, password=password).first()
    
    if user:
        return "Login bem-sucedido"
    else:
        return "Credenciais inválidas. Tente novamente."

```

E neste criamos um novo login para o usuario

```
@app.route('/creat_login', methods = ['POST'])
def create_user():

    name = request.form['name']
    password = request.form['password']
   
    user_base = UserBase(name = name, password = password)
    session.add(user_base)
    session.commit()
    return redirect('/')
```	

E aqui rodamos a aplicação
```
if __name__ == '__main__':
    app.run(debug=True)
```
### <b>Crinado o conteiner</b> </h3>

Agora, para criar o conteiner, precisamos criar um arquivo chamado 'dockerfile', que seria o arquivo que ira criar o conteiner.
Nele contem todas as configurações necessarias para criar o conteiner, como a porta que ira rodar, o que ira rodar, etc.

O proximo passo é criar um arquivo de requerimentos. Nele contem todas as bibliotecas que precisamos para rodar o projeto. No nosso caso, só precisamos do Flask.

```
mkdir requeriments.txt
pip freeze > requeriments.txt
```
Pronto, todas as configurações iniciais estão criadas. 

Agora, criamos o conteiner utilizando o comando 

```
docker build -t nome_do_conteiner .
```
Neste caso, seria 'python-docker'

Para verificar se o conteiner foi criado, utilizamos o comando 

``` 
docker images
```
Nele contem o nome, o id, o tamanho e quando foi criado.

E por fim, para rodar, basta utilizar o comando 

```
docker run -p 5000:5000 python-docker
```

### <b>Subindo a imagem no docker hub</b> </h3>

A meta da ponderada é criar um docker Composer, que seria um arquivo que ira criar varios conteineres.

<h1>EM Construção....


<h1> OBS </h1>

Fiz varias tentativas para subir o docker compose, mas não consegui. Ele da um erro de login mesmo ja estando logado. Acredito que seja algum erro na configuração do docker  



