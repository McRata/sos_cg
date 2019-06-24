import numpy as np
import matplotlib.pyplot as plt  # To visualize
import statsmodels.api as sm
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression


#####                    #####
#### Tratamiento de Datos ####
#####                    #####
#--> Importación de excels
data = pd.read_excel(r'C:\Users\McRat\Google Drive\sos_gc\Datasets\participacio\Votacions_bcn_locales.xlsx', sheet_name='Hoja1')
data2 = pd.read_excel(r'C:\Users\McRat\Google Drive\sos_gc\Datasets\participacio\ocupacion_bcn__barrios_2007_2018.xlsx', sheet_name='Hoja1')


#---> Para la tabla de Votos - data (Tiene una condición en el proceso)
list_aux = []
df = data.filter(items=['Any','Codi_barri','Camp','Nombre'])
for i,t in df.iterrows():
    if df.at[i,'Camp'] == 'Vots totals':
       dict0 = {}
       dict0.update(t)
       list_aux.append(dict0)
df_votacions = pd.DataFrame(list_aux)

#---> Para la tabla de Ocupacion - data2 
# 
# (Este proceso se debería hacer cómo función,
#  pasando cómo variables el data frame inicial, 
#  la lista de items que necesitas
#  y que devuelva (return) el dataframa)
#
# def csv_to_df(dataframe,(['Columns',..,'Columns']))
#
#    return pd.DataFrame(list_aux)
#
list_aux = []
df = data2.filter(items=['Any','Codi_Barri','Ocupats','Votants_locals']) #
for i,t in df.iterrows():
     dict0 = {}
     dict0.update(t)
     list_aux.append(dict0)
df_ocupats = pd.DataFrame(list_aux)

#####             ##### |
#### Subdataframes #### |--> Filtros a los data frames de cada uno de les CSV, se puede hacer por varios valores
#####             ##### |
sub_dfocupats = df_ocupats[df_ocupats['Any'].isin(['2016'])]
sub_dfvotacions = df_votacions[df_votacions['Any'].isin(['2016'])]
#####                         #####
#### Construcción de variables ####
#####                         #####

#--> Lineal - escogemos un valor del df y lo parametizamos de -1 a 1,
# me acuerdo de este proceso en la uni, pero no del todo
#
X = df_votacions['Any'].values.reshape(-1,1)
m = df_ocupats['Any'].values.reshape(-1,1)
n = df_ocupats["Codi_Barri"].values.reshape(-1,1)
#X = df_votacions["Any"].values.reshape(-1,1)
y = sub_dfvotacions["Nombre"].values.reshape(-1,1)
l = df_ocupats["Ocupats"].values.reshape(-1,1)
r = df_ocupats["Votants_locals"].values.reshape(-1,1)
#--> Multi - conjunto de variables
Xmulti = df_ocupats[['Any','Ocupats']]

#####                         ##### |
#### Construcción de funciones #### |--> Convertidas a función, más abajo se ejecutan
#####                         ##### |

#--> Lineal : Y=mX
def R_Lineal(x,y):
     linear_regressor = LinearRegression()
     linear_regressor.fit(x, y)# perform linear regression
     plt.scatter(x, y)
     Y_pred = linear_regressor.predict(y)  # make predictions
     plt.plot(x, y, color='yellow')
     plt.plot(x, Y_pred, color='red')
     plt.show()
     return

#-->Multilineal : Y=mX1 + ... + rXn -Da un summary de las
# estadisiticas de la regressión.
#
def R_Multi(x,y):
     linear_regressor = LinearRegression()
     linear_regressor.fit(X, y)
     print('Intercept: \n', linear_regressor.intercept_)
     print('Coefficients: \n', linear_regressor.coef_)
     # with statsmodels
     X = sm.add_constant(X) # adding a constant
     model = sm.OLS(y, X).fit()
     predictions = model.predict(X) 
     print(model.summary())
     return
#####                         #####
#### Ejecución de los análisis ####
#####                         #####

R_Lineal(n,l)