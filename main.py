from itba import parseador
from itba import errores
#from itba import reporte 

data = parseador.Parser('.\itba\eventos\eventos_black.json') and parseador.Parser('.\itba\eventos\eventos_classic.json') and parseador.Parser('.\itba\eventos\eventos_gold.json')
cliente = data.cliente 
eventos = data.eventos
print(cliente)
buscador = errores.Buscador(eventos)

