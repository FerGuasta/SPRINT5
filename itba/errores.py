from .clases import razones 
class Buscador():
    def __init__(self,eventos,cuenta):
        self.eventos_aceptados = [ x for x in eventos if x['estado'] == 'ACEPTADA']
        self.eventos_rechazados = [ x for x in eventos if x['estado'] == 'RECHAZADA']
        #print(self.eventos_rechazado)
        for rechazado in self.eventos_rechazados:
            if rechazado['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                self.razon = razones.RazonRetiroEfectivo(rechazado, cuenta)
            elif rechazado['tipo'] == 'ALTA_TARJETA_CREDITO':
                self.razon = razones.RazonAltaTarjetaCredito(rechazado, cuenta)
            elif rechazado['tipo'] == 'ALTA_CHEQUERA':
                self.razon = razones.RazonAltaChequera(rechazado, cuenta)
            elif rechazado['tipo'] == 'COMPRAR_DOLAR':
                self.razon = razones.RazonCompraDolar(rechazado, cuenta)
            elif rechazado['tipo'] == 'TRANSFERENCIA_ENVIADA':
                self.razon = razones.RazonTransferenciaEnviada(rechazado, cuenta)
            else:
                self.razon = razones.RazonTransferenciaRecibida(rechazado, cuenta)
        return self.razon 
    

        