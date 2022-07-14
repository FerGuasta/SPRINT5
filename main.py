from itba import parseador
from itba import errores
#from itba import reporte 

data = parseador.Parser('.\itba\eventos\eventos_black.json')
cliente = data.cliente 
eventos = data.eventos
print(cliente)
buscador = errores.Buscador(eventos)

