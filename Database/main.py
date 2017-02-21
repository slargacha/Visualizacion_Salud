# import libraries necessaries
from csv import DictReader
from pymongo import MongoClient

# Reading files: Departamentos
departamentos = DictReader(open('Information/Departamentos.csv','r'))

#client connection
client = MongoClient('localhost', 27017)  
mdiDb = client.mdi

# Creation of collections
departamentosCollection = mdiDb.departamentos #1

# Save collection
def saveLine(line):
    for key, value in line.items():
        #print(key)
        #print(value)
       
        if(key != "Codigo Departamento" and key != "Codigo Municipio" key != ""):  #remove spaces
            if(num==1):
                departamentos = {
                    'dep': key,
                    'mun': key
                }
                departamentosCollection.insert(departamentos)
           
# Selection of the line to adding            
for line1 in departamentos:
    num=int(1)
    saveLine(line1)
    
