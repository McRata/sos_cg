import csv
import json
import networkx as nx #Libreria de las redes
import matplotlib.pyplot as plt #Libreria para la representacion de redes

jsonfile = open('file.json', 'w')

data = {}

csvfile = open('PDVR.csv', 'r')
reader = csv.Reader(csvfile)
mylist.append(reader)


for user in mylist.values():
        data[user] = []
        path = 'userdata/'+user+'.csv'
        fcsv = open(path,'r')
        readerr = csv.Reader(csvfile)
        mylistt = list(readerr)
        for usefollower in mylistt.values(): 
                data[user].append(follower)


with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)







# with open() as edge_list:
# data = json.load(edge_list)
# G = nx.Graph()

# for user in data['users']:
#     for follower in user['follower']
#         G.add_edge(user,follower)
# #Se dibuja la gráfica    
# nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')

# #Se pinta la gráfica
# plt.show() 
            
