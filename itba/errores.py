from .clases import razones 
class Buscador():
    def __init__(self,eventos):
        self.eventos_aceptados = [ x for x in eventos if x['estado']== 'ACEPTADA']
        self.eventos_rechazados = [ x for x in eventos if x['estado']== 'RECHAZADA']
        #print(self.eventos_aceptados)
        if self.eventos_rechazados['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            self.razon = razones.RazonRetiroEfectivo()
            print('algo')
        elif self.eventos_rechazados['tipo'] == 'ALTA_TARJETA_CREDITO':
            self.razon = razones.RazonAltaTarjetaCredito
            print('algo')
        elif self.eventos_rechazados['tipo'] == 'ALTA_CHEQUERA':
            self.razon = razones.RazonAltaChequera
            print('algo')
        elif self.eventos_rechazados['tipo'] == 'COMPRAR_DOLAR':
            self.razon = razones.RazonCompraDolar
            print('algo')
        elif self.eventos_rechazados['tipo'] == 'TRANSFERENCIA_ENVIADA':
            self.razon = razones.RazonTransferenciaEnviada
            print('algo')
        else:
            self.razon = razones.RazonTransferenciaRecibida
            print('algo')

        