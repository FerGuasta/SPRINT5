from .direccion import Direccion

class Cliente:
    def __init__(self,data,cuenta):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.dir = Direccion(data['direccion']) 
        self.cuenta = cuenta
        #print('Se creo cliente ' + self.dni)
        
    def baja(self):
        self.tipo='baja'
"""*** Gold ***  
-   Tarjeta de debito
-   Caja de ahorro ARS:     No
-   Caja de ahorro USD:     Si
-   Puede comprar USD:      Si
-   Tarjeta de credito:     Si (1)
-   Chequera:               Si

* Para el objeto cuenta * 
-   Extraccion max:         $20K
-   Recibir transf (max):   $500K  (Sin prev. aviso)
-   Monto 
-   Comision por transf:    0.5% 
-   Cuenta corriente
    (Saldo descubierto):    Si. Hasta $-10K

"""
class ClienteGold(Cliente):
    def __init__(self, data, cuenta):
        super().__init__(data, cuenta)
    def puede_crear_chequera(self): 
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True
    
"""*** Classic ***  
-   Tarjeta de debito
-   Caja de ahorro ARS:     Si
-   Caja de ahorro USD:     No
-   Puede comprar USD:      No
-   Tarjeta de credito:     No
-   Chequera:               No 

* Para el objeto cuenta * 
-   Extraccion max:         $10K
-   Recibir transf (max):   $150K  (Sin prev. aviso)
-   Monto 
-   Comision por transf:    1% 
-   Cuenta corriente
    (Saldo descubierto):    No. Hasta $0
"""    
class ClienteClassic(Cliente):
    def __init__(self, data, cuenta):
        super().__init__(data, cuenta)
    def puede_crear_chequera(Self): 
        return False
    def puede_crear_tarjeta_credito(self):
        return False
    def puede_comprar_dolar(self):
        return False     

"""*** Black ***  
-   Tarjeta de debito
-   Caja de ahorro ARS:     Si
-   Caja de ahorro USD
-   Puede comprar USD:      Si
-   Tarjeta de credito:     Si (5)
-   Chequera:               Si (2)

* Para el objeto cuenta * 
-   Extraccion max:         $100K
-   Recibir transf (max):   $Sin limite  (Sin prev. aviso)
-   Monto 
-   Comision por transf:    0% 
-   Cuenta corriente
    (Saldo descubierto):    Si. Hasta $-10K
"""  
class ClienteBlack(Cliente):
    def __init__(self, data, cuenta):
        super().__init__(data, cuenta)
    def puede_crear_chequera(Self): 
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True
    


