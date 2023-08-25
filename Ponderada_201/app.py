from flask import Flask, render_template, request, redirect

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

from model.base import Base
#da pasta, pego o arquivo e importo a classe
from model.user_base import UserBase

app = Flask('__name__')

engine = create_engine('sqlite:///database.db')

#criar uma sessão / bing = type of database e o nome do banco
Session = sessionmaker(bind=engine)

#cria uma variavel para a sessão
session = Session()

#cria o banco de dados
Base.metadata.create_all(engine)

@app.route('/')
def home():
    #pegar todas as user_login
    #da sessão, pego a query e passando a tabela user_login, pegando tudo
    user_login = session.query(UserBase).all()
    return render_template('index.html', user_login = user_login)

@app.route('/login', methods = ['POST'])
def create_user():

    name = request.form['name']
    password = request.form['password']
   
    #Add as informações na tabela
    user_base = User_Base(name = name, password = password)
    #add as informaçoes da user_base na sessão
    session.add(user_base)
    #salvar as informações
    session.commit()
    return redirect('/')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)