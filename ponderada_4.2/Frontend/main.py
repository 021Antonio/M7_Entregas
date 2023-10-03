from flask import Flask, render_template, request, redirect

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

from model.base import Base
from model.user_base import UserBase

app = Flask('__name__')

engine = create_engine('sqlite:///database.db')

Session = sessionmaker(bind=engine)

session = Session()

Base.metadata.create_all(engine)

@app.route('/')
def home():
    user_login = session.query(UserBase).all()
    return render_template('index.html', user_login = user_login)

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']

    user = session.query(UserBase).filter_by(name=name, password=password).first()

    if user:
        # Redireciona para a rota do dashboard após um login bem-sucedido
        return redirect('/dashboard')
    else:
        return "Credenciais inválidas. Tente novamente."
        
@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Lógica para gerar o gráfico usando Streamlit
    # Substitua isso pela lógica real de geração do gráfico
    # Exemplo: return "Aqui está o gráfico gerado pelo Streamlit!"
    return render_template('dashboard.html')  # Se você quiser renderizar um template do Flask




@app.route('/creat_login', methods = ['POST'])
def create_user():

    name = request.form['name']
    password = request.form['password']
   
    user_base = UserBase(name = name, password = password)
    session.add(user_base)
    session.commit()
    return redirect('/')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)