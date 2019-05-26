import networkx as nx
import xml.etree.ElementTree as ET


tree = ET.parse('llistatEntitats-associacions.xml')
root = tree.getroot()


entitats = root.find('entitats')
outF = open("Associacions.txt","w") 
for s in entitats:
    nom = s.find('nom')
    outF.write(nom.text+'\n')
    print(nom.text)




G = nx.Graph()