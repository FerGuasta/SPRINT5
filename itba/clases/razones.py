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
        self.razon = None
        if self.evento['estado'] == 'ACEPTADA':
            self.razon = ' '
        if self.cuenta.tipo == 'CLASSIC':
            self.razon = 'No se pudo dar de alta la chequera porque el cliente tiene una cuenta Classic.'
        if self.cuenta.tipo == 'CLASSIC':
            self.razon = 'No se pudo dar de alta la chequera porque el cliente tiene una cuenta Classic.'
        elif self.cuenta.tipo == 'GOLD':
            if self.evento['totalChequerasActualmente'] == 1:
                self.razon = 'El cliente completó la cantidad de chequeras posibles para su tipo de cuenta (1).'
        elif self.cuenta.tipo == 'BLACK':
            if self.evento['totalChequerasActualmente'] == 2:
                self.razon = 'El cliente completó la cantidad de chequeras posibles para su tipo de cuenta (2).'
        
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        self.razon = None
        if self.evento['estado'] == 'ACEPTADA':
            self.razon = ' '
        elif self.cuenta.tipo == 'GOLD':
            if self.evento['totalTarjetasDeCreditoActualmente'] == 1:
                self.razon = 'El cliente completó la cantidad de tarj. de crédito posibles para su tipo de cuenta (1).'
        elif self.cuenta.tipo == 'BLACK':
            if self.evento['totalTarjetasDeCreditoActualmente'] == 5:
                self.razon = 'El cliente completó la cantidad de tarj. de crédito posibles para su tipo de cuenta (5).'
        
class RazonCompraDolar(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        self.razon = None
        if self.evento['estado'] == 'ACEPTADA':
            self.razon = ' '
        if self.cuenta.tipo == 'CLASSIC':
            self.razon = 'No se pudo comprar dólares porque el cliente tiene una cuenta Classic.'
        elif self.evento['saldoEnCuenta'] < self.evento['monto']:
            self.razon = "$" + str(self.cuenta.monto) + ' es un monto superior a los fondos existentes en la cuenta: $' + str(self.evento['saldoEnCuenta']) + "." 

class RazonRetiroEfectivo(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        self.razon = None
        if self.evento['estado'] == 'ACEPTADA':
            self.razon = ' '
        if self.cuenta.limite_extraccion_diario < self.evento['monto']:
            self.razon = "$" + str(self.evento["monto"]) + " supera el monto diario extraíble: $" + str(self.cuenta.limite_extraccion_diario) + "."
        elif self.evento['cupoDiarioRestante'] < self.evento['monto']:
            self.razon = "$" + str(self.evento["monto"]) + " supera el monto restante diario extraíble: $" + str(self.evento["cupoDiarioRestante"]) + "."
        elif self.evento['saldoEnCuenta'] < self.evento['monto']:
            self.razon = "$" +  str(self.evento["monto"]) + " monto superior a los fondos existentes en la cuenta: $" + str(self.evento["saldoEnCuenta"]) + "."

class RazonTransferenciaEnviada(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        self.razon = None
        self.extra = self.evento['monto'] + (self.evento['monto'] * self.cuenta.costo_transferencia)
        if self.evento['estado'] == 'ACEPTADA':
            self.razon = ' '
        if self.evento['saldoEnCuenta'] < self.evento['monto']:
            self.razon = "$" + str(self.evento["monto"]) + " monto superior a los fondos existentes en la cuenta para su transferencia: $" + str(self.evento['saldoEnCuenta']) + "."
        elif self.evento['saldoEnCuenta'] < self.extra:
            self.razon = "Faltan fondos para efectuar la transferencia, cuyo costo es " +str(self.cuenta.costo_transferencia * 100)+ "% del monto."

class RazonTransferenciaRecibida(Razon):
    def __init__(self, evento, cuenta):
        super().__init__(evento, cuenta)
        self.razon = None
        if self.evento['estado'] == 'ACEPTADA':
            self.razon = ' '
        if self.evento['saldoEnCuenta'] < self.evento['monto']:
            self.razon = "$" + str(self.evento["monto"]) + " monto superior a los fondos existentes en la cuenta: $" + str(self.evento['saldoEnCuenta']) + "."
        