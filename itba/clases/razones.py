from .cuenta import Cuenta 

class Razon():
    def __init__(self, evento, cuenta):
        self.evento = evento 
        self.cuenta = cuenta 
        self.cuenta.monto = evento['monto']
        
    def resolver(self, cliente, evento):
        pass

class RazonAltaChequera(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        if self.cuenta.tipo == 'CLASSIC':
            self.razon = 'No se pudo dar de alta la chequera porque el cliente tiene una cuenta Classic.'
        elif self.cuenta.tipo == 'GOLD':
            if self.evento['totalChequerasActualmente'] == 1:
                self.razon = 'El cliente completó la cantidad de chequeras posibles para su tipo de cuenta (GOLD).'
        elif self.cuenta.tipo == 'BLACK':
            if self.evento['totalChequerasActualmente'] == 2:
                self.razon = 'El cliente completó la cantidad de chequeras posibles para su tipo de cuenta (BLACK).'
        
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        if self.cuenta.tipo == 'CLASSIC':
            self.razon = 'No se pudo dar de alta la tarjeta de crédito porque el cliente tiene una cuenta Classic.'
        elif self.cuenta.tipo == 'GOLD':
            if self.evento['totalTarjetasDeCreditoActualmente'] == 1:
                self.razon = 'El cliente completó la cantidad de tarj. de crédito posibles para su tipo de cuenta (GOLD).'
        elif self.cuenta.tipo == 'BLACK':
            if self.evento['totalTarjetasDeCreditoActualmente'] == 5:
                self.razon = 'El cliente completó la cantidad de tarj. de crédito posibles para su tipo de cuenta (BLACK).'
        
class RazonCompraDolar(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        if self.cuenta.tipo == 'CLASSIC':
            self.razon = 'No se pudo comprar dólares porque el cliente tiene una cuenta Classic.'
        elif self.evento['saldoEnCuenta'] < self.evento['monto']:
            self.razon = self.cuenta.monto + ' es un monto superior a los fondos existentes en la cuenta: ' + self.evento['saldoEnCuenta'] 

class RazonRetiroEfectivo(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        if self.cuenta.limite_extraccion_diario < self.evento['monto']:
            self.razon = self.evento["monto"] + " supera el monto diario extraíble: " + self.cuenta.limite_extraccion_diario + "."
        elif self.evento['cupoDiarioRestante'] < self.evento['monto']:
            self.razon = self.evento["monto"] + " supera el monto restante diario extraíble: " + self.evento["cupoDiarioRestante"] + "."
        elif self.evento['saldoEnCuenta'] < self.evento['monto']:
            self.razon = self.evento["monto"] + "Monto superior a los fondos existentes en la cuenta" + self.evento["saldoEnCuenta"] + "."

class RazonTransferenciaEnviada(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        if self.cuenta.limite_transferencia_recibida < self.evento['monto']:
            self.razon = self.evento["monto"] + " supera el límite de transferencia recibida: " + self.cuenta.limite_transferencia_recibida + "."

class RazonTransferenciaRecibida(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        if self.evento['saldoEnCuenta'] < self.evento['monto']:
            self.razon = self.evento["monto"] + " monto superior a los fondos existentes en la cuenta: " + self.evento['saldoEnCuenta'] + "."
        