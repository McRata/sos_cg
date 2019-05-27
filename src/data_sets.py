import xml.etree.ElementTree as ET #Libreria para la importación del XML
import networkx as nx #Libreria de las redes
import matplotlib.pyplot as plt #Libreria para la representacion de redes

#Seleccionamos el XML
tree = ET.parse('llistatEntitats-associacions.xml')
root = tree.getroot()
#Una vez creado el objeto, trabajaremos con root
entitats = root.find('entitats')
#Abrimos un txt para el tratado de datos
outF = open("Associacions_dataset.txt","w") 
#escribimos los headers de la dataset
outF.write('nombre_tipo_finscripcion_cp_poblacio_comarca_class\n')

#Creamos la red
G = nx.Graph()


#Loop para el listado de atributos
    #s --> seran cada entidad de el XML
    #el metodo str(s.find().text)
        #s.find() -> busca la etiqueta de cada entidad
        #.text -> te da el valor de la etiqueta
        #str() lo convierte en string
for s in entitats:
    nom = str(s.find('nom').text)
    tipus = str(s.find('tipus').text)
    born = str(s.find('dataInscripcio').text)
    cp = str(s.find('codiPostal').text)
    poblacio = str(s.find('poblacio').text)
    comarca = str(s.find('comarca').text)
    classgeneral = str(s.find('classificacioGeneral').text)
    
    outF.write(nom+"_"+tipus+"_"+born+"_"+cp+"_"+poblacio+"_"+comarca+"_"+classgeneral+"\n")
    #usamos las string de los nombres como nodos
    G.add_nodes_from(nom)
    
#Se dibuja la gráfica    
nx.draw(G)

#Se pinta la gráfica
plt.show()

