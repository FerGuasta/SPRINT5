class Cliente:
    def __init__(self,data):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        print('Se creo cliente: '+self.dni)
        
    def baja(self):
        self.tipo='baja'

class ClienteGold(Cliente):
    def puede_comprar_dolar(self):
        return True
    def __init__(self, data):
        print('Se creo gold')  
        super().__init__(data)

class ClienteClassic(Cliente):
    def puede_comprar_dolar(self):
        return False
    def __init__(self, data):
        print('Se creo classic')
        super().__init__(data) 
    

class ClienteBlack(Cliente):
    def puede_comprar_dolar(self):
        return True
    def __init__(self, data):
        print('Se creo black')
        super().__init__(data)


