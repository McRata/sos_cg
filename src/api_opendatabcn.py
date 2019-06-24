import requests #librería para llamar la API
import json
import pprint
import urllib

# Inspección de los datasets de open data
def inspeccion_api(results_request):
    for d in r.get('result').get('results'):
        print("-"*60)
        #Iteración con condicionales para poder ver los atributos del dataset
        for att, c in  d.items():
            print(att)  
            if att.find('url)'):
                print(c)
            #     for i,m in c.items():
            #         if i == 'es':
            #             print(att +'='+m)
            # elif att == 'api':
            #     print(c)
            # elif att == 'load_type':
            #     print(c)
            # elif att == 'frequency':
            #     print(c)
            # elif att == 'type':
            #     print(c)
            # elif att == 'notes':
            #     print(c)
            # elif att == 'tag':
            #     if c.find('trànsit'):
            #         print(c)
            # #El nombe de las variables no seleccionadas
            # else:
            #     print(att)








# Make a get request
response = requests.get("http://opendata-ajuntament.barcelona.cat/data/api/3/action/package_search?rows=1000")
r = response.json()



inspeccion_api(r)


# for d in r.get('result').get('results'):
#     print("-"*60)
#     #Iteración con condicionales para poder
#     for att, c in  d.items(): 
#         if
