class Cuenta():
    def __init__(self, tipo, limite_extraccion_diario, limite_transferencia_recibida,
                monto, costo_transferencia, saldo_descubierto_disponible):
        self.tipo = tipo 
        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.monto = monto 
        self.costo_transferencia = costo_transferencia
        self.saldo_descubierto_disponible = saldo_descubierto_disponible
    def __repr__(self):
        return f'{self.limite_extraccion_diario}\n{self.limite_transferencia_recibida}\n{self.monto}\n{self.costo_transferencia}\n{self.saldo_descubierto_disponible}'