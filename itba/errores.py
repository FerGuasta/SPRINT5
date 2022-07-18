from .clases import razones 
class Buscador():    
    def __init__(self,eventos,cuenta):
        self.razones = []
        self.eventos_aceptados = [ x for x in eventos if x['estado'] == 'ACEPTADA']
        self.eventos_rechazados = [ x for x in eventos if x['estado'] == 'RECHAZADA']
        #print(self.eventos_rechazado)
        for aceptado in self.eventos_aceptados:
            if aceptado['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                self.razon = razones.RazonRetiroEfectivo(aceptado, cuenta)
                self.razones.append(self.razon)
            elif aceptado['tipo'] == 'ALTA_TARJETA_CREDITO':
                self.razon = razones.RazonAltaTarjetaCredito(aceptado, cuenta)
                self.razones.append(self.razon)
            elif aceptado['tipo'] == 'ALTA_CHEQUERA':
                self.razon = razones.RazonAltaChequera(aceptado, cuenta)
                self.razones.append(self.razon)
            elif aceptado['tipo'] == 'COMPRA_DOLAR':
                self.razon = razones.RazonCompraDolar(aceptado, cuenta)
                self.razones.append(self.razon)
            elif aceptado['tipo'] == 'TRANSFERENCIA_ENVIADA':
                self.razon = razones.RazonTransferenciaEnviada(aceptado, cuenta)
                self.razones.append(self.razon)
            else:
                self.razon = razones.RazonTransferenciaRecibida(aceptado, cuenta)
                self.razones.append(self.razon)
                
        for rechazado in self.eventos_rechazados:
            if rechazado['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                self.razon = razones.RazonRetiroEfectivo(rechazado, cuenta)
                self.razones.append(self.razon)
            elif rechazado['tipo'] == 'ALTA_TARJETA_CREDITO':
                self.razon = razones.RazonAltaTarjetaCredito(rechazado, cuenta)
                self.razones.append(self.razon)
            elif rechazado['tipo'] == 'ALTA_CHEQUERA':
                self.razon = razones.RazonAltaChequera(rechazado, cuenta)
                self.razones.append(self.razon)
            elif rechazado['tipo'] == 'COMPRA_DOLAR':
                self.razon = razones.RazonCompraDolar(rechazado, cuenta)
                self.razones.append(self.razon)
            elif rechazado['tipo'] == 'TRANSFERENCIA_ENVIADA':
                self.razon = razones.RazonTransferenciaEnviada(rechazado, cuenta)
                self.razones.append(self.razon)
            else:
                self.razon = razones.RazonTransferenciaRecibida(rechazado, cuenta)
                self.razones.append(self.razon)
            
    

        