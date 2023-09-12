# Colab 
O dataset escolhido foi [Heart Attack](https://www.kaggle.com/datasets/bharath011/heart-disease-classification-dataset). O dataset contém 1319 amostras de pacientes com 9 atributos, sendo 8 deles numéricos e 1 categórico. O objetivo é prever se o paciente possui ou não doença cardíaca. O motivo da escolha foi pela curiosidade de entender os criterios utilizados para a classificação de doenças cardíacas. Analisando mais a fundo o dataset, descobri que so com esses dados não é possível fazer uma classificação precisa, pois não há informações sobre o histórico do paciente, como por exemplo, se ele já teve algum problema cardíaco, se ele é fumante, se ele tem diabetes, etc. Porém, como o objetivo é apenas praticar o uso de algoritmos de classificação, o dataset é suficiente para o propósito.

## Importando as bibliotecas
 As bibliotecas utilizadas foram: 
 
 ```
import pandas as pd # Manipulação de dados
import numpy as np # Manipulação de dados
from sklearn import preprocessing # Pré-processamento
from sklearn.preprocessing import MinMaxScaler # Pré-processamento-Normalização
import matplotlib.pyplot as plt # Visualização de dados-Graficos
import seaborn as sns # Visualização de dados-Graficos
from pycaret.classification import * # Machine Learning
from pycaret.datasets import get_data 
from sklearn.model_selection import train_test_split # Machine Learning-Separação de dados
from sklearn.ensemble import RandomForestClassifier # Machine Learning-modelo de classificação
from sklearn import metrics #
import matplotlib.pyplot as plt # Visualização de dados-Graficos
import pickle # Salvar modelo
 ```

 A explicação de cada parte do codigo se encontra diretamente no notebook.

 ## Resultados
 O modelo escolhido foi o Random Forest Classifier com uma acuracy de 97%. O modelo foi salvo e pode ser utilizado para prever se um paciente possui ou não doença cardíaca. O modelo pode ser encontrado na pasta [src](\src\modelo_treino.ipynb)

 O modelo em si, apresenta um overfitting, pois a acurácia do teste é de 97%. Isso pode ser resolvido com mais dados, porém, como o dataset é pequeno, não há muito o que fazer.

 ## Api

 A api foi feita utilizando o framework FastApi e criada direto pelo Pycaret. Quando tentei rodar direto pelo colab, não funcionou, então tive que criar um arquivo .py e rodar direto pelo terminal. O porem, foi que para rodar o arquivo .py, tive que instalar o pycaret direto pelo terminal e não foi possivel. A instalação deu erro e o motivo que encontrei foi: 
 ```
 RuntimeError: Cannot install on Python version 3.11.4; only versions >=3.7,<3.11 are supported.
 ```
 No presente momento, estou tendo resolver este problema sem desistalar o python.

 <h1>EM CONSTRUÇÃO . . .</h1>  