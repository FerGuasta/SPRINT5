from .direccion import Direccion

class Cliente:
    def __init__(self,data):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.dir = Direccion(data['direccion']) 
        print('Se creo cliente ' + self.dni)
        
    def baja(self):
        self.tipo='baja'
"""*** Gold ***  
-   Tarjeta de debito
-   Caja de ahorro ARS:     No
-   Cuenta corriente:       Si. Hasta $-10K
-   Caja de ahorro USD:     Si
-   Puede comprar USD:      Si
-   Tarjeta de credito:     Si (1)
-   Extraccion max:         $20K
-   Chequera:               Si
-   Comision por transf:    0.5% 
-   Recibir transf (max):   $500K  (Sin prev. aviso)
"""
class ClienteGold(Cliente):
    def __init__(self, data):
        print('Se creo gold')  
        super().__init__(data)
    def puede_crear_chequera(Self): 
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True
    
"""*** Classic ***  
-   Tarjeta de debito
-   Caja de ahorro ARS:     Si
-   Cuenta corriente:       No
-   Caja de ahorro USD:     No
-   Puede comprar USD:      No
-   Tarjeta de credito:     No
-   Extraccion max:         $10K
-   Chequera:               No
-   Comision por transf:    1% 
-   Recibir transf (max):   $150K  (Sin prev. aviso)
"""    
class ClienteClassic(Cliente):
    def __init__(self, data):
        print('Se creo classic')
        super().__init__(data)
    def puede_crear_chequera(Self): 
        return False
    def puede_crear_tarjeta_credito(self):
        return False
    def puede_comprar_dolar(self):
        return False     

"""*** Black ***  
-   Tarjeta de debito
-   Caja de ahorro ARS:     Si
-   Cuenta corriente:       Si
-   Caja de ahorro USD:     Si ($-10K)
-   Puede comprar USD:      Si
-   Tarjeta de credito:     Si (5)
-   Extraccion max:         $100K
-   Chequera:               Si (2)
-   Comision por transf:    0% 
-   Recibir transf (max):   $10e15  (Sin prev. aviso)
"""  
class ClienteBlack(Cliente):
    def __init__(self, data):
        print('Se creo black')
        super().__init__(data)
    def puede_crear_chequera(Self): 
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True
    


