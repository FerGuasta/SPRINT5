class Razon():
    def __init__(self, razon):
        self.razon = razon
    def resolver(self, cliente, evento):
        pass

class RazonAltaChequera(Razon):
    def resolver(self, cliente, evento):
        if cliente.puede_crear_chequera():
            print('Se creo chequera')
        else:
            print('No se creo chequera')

class RazonAltaTarjetaCredito(Razon):
    def resolver(self, cliente, evento):
        if cliente.puede_crear_tarjeta_credito():
            print('Se creo tarjeta de credito')
        else:
            print('No se creo tarjeta de credito')

class RazonCompraDolar(Razon):
    def resolver(self, cliente, evento):
        if cliente.puede_comprar_dolar():
            print('Se puede comprar dolar')
        else:
            print('No se puede comprar dolar')

class RazonRetiroEfectivo(Razon):
    pass

class RazonTransferenciaEnviada(Razon):
    pass

class RazonTransferenciaRecibida(Razon):
    pass