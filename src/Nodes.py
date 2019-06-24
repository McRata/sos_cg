
# Dataset de usuarios y followers

import networkx as nx #Libreria de las redes
import matplotlib.pyplot as plt #Libreria para la representacion de redes
import pandas as pd
import json
import os

orig_user = pd.read_csv("userdata/PDVR.csv")
orig_user.columns = ['PDVR']

full_edge_list = []
for user in orig_user['PDVR']:
    # Lee cada archivo
    filename = str(user) + ".csv"
    path = os.path.join(os.getcwd(),"userdata") # Concatena el nombre de archivo
    file = os.path.join(path,filename)
    df = pd.read_csv(file, index_col=None)
    
    # Crea la lista de followers
    followers_list = list(df['username'])
    data = {user : followers_list}
    
    full_edge_list.append(data)

    result = {}
    for d in full_edge_list:
        result.update(d)


with open('nodes.json', 'w') as fp:
    json.dump(result, fp)


with open("nodes.json", "r") as edge_list:
    data = json.load(edge_list)
    G = nx.Graph()

for user in data.keys():
    G.add_node(user)
    for follower in data.values():
        G.add_edge(user, str(follower))


#Se dibuja la gráfica    
nx.draw(G,node_color='r', edge_color='y')
plt.show()


subgraph_list = []
D = nx.Graph()

for node in G.nodes:
    if node  in followers_list:
        D.add_edge(node,G.neighbors(node))
        



nx.draw(D,node_color='r', edge_color='y')
#Se pinta la gráfica
plt.show()
