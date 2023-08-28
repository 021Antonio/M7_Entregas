# API

### <b>Motivação</b> </h3>

A api utilizada foi o FLask. Utilizei como base 


### <b>Como utilizar</b> </h3>

O primeiro passo é criar uma venv utilizando os comandos 

``` 
mkdir venv
python -m venv vevn
venv/Scripts/activate
```

Agora, precisa baixar o Flask utilizando o comando 

```
pip install Flask
```
 Pronto, agora esta tudo certo para rodar o projeto. 

### <b>Pastas</b> </h3>

A pasta principal onde contem a aplicação é a 'src', nela contem o "dockerfile", "templates"(contem o html) e o "app.py" que é nossa api em flask ligando ao html

### <b>Sobre a api</b> </h3>

Aqui importamos o Flask e p render_template, que seria a biblioteca para gerar o nossa pagina html

```
from flask import Flask, render_template
```
Iniciamos a aplicação

```
app = Flask(__name__)
```
Aqui criamos a rota para a pagina inicial, que seria o index.html

```
@app.route('/')
def index():
    return render_template('index.html')
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

Para subir a imagem no docker hub, precisamos criar uma conta no site do docker hub. Após criar a conta, precisamos logar no docker hub utilizando o comando 

```
docker login
```
Após logar, precisamos criar uma tag para a imagem utilizando o comando 

```
docker tag python-docker nome_do_usuario/nome_do_repositorio
```
Após criar a tag, precisamos subir a imagem utilizando o comando 

```
docker push nome_do_usuario/nome_do_repositorio
```
Pronto, a imagem foi subida no [docker hub](https://hub.docker.com/r/antonioribeiro893/python-docker/tags).


<h1> OBS </h1>

Eu fiz fui pesquisando passo a passo em varios lugares diferentes ate consegui rodar. Com toda a certeza, eu cometi alguns erros e vou tentar corrigir o mais rápido possivel.

Um exemplo foi que eu criei o build 3 vezes, um normal, um com uma tag bonita e outro com o nome diferente. A questao é, como eu fiz isso?

Eu vou tentar descorbrir amanhã (14/08/2023) como eu fiz isso e vou refazer do zero para fazer melhor. 



