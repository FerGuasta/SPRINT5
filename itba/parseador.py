import json
from .clases import cliente
from .clases import cuenta 

class Parser():
    def __init__(self,file):
        self.file=file
        self.load()
        self.cuenta = None 
        self.eventos=self.data['transacciones']

        if self.data['tipo'] == 'BLACK':
            self.cuenta = cuenta.Cuenta('BLACK',100000,10000000000000,0,0,-10000)
            self.cliente= cliente.ClienteBlack(self.data, cuenta)
            #print('Se creo BLACK')
            #print(self.cuenta)
        elif self.data['tipo'] == 'GOLD':
            self.cuenta = cuenta.Cuenta('GOLD',20000,500000,0,0.5,-10000)
            self.cliente= cliente.ClienteGold(self.data, cuenta)
            #print('Se creo GOLD')
            #print(self.cuenta)
        else:
            self.cuenta = cuenta.Cuenta('CLASSIC',10000,150000,0,0.01,0)
            self.cliente=cliente.ClienteClassic(self.data, cuenta)
            #print('Se creo CLASSIC')
            #print(self.cuenta)
        
    def load(self):
        f=open(self.file)
        self.data=json.load(f)
        f.close()

    
            
 
