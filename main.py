from itba import parseador
from itba import errores
from itba import reporte 
import sys
if str(sys.argv[1]) == "GOLD":
    dataGOLD = parseador.Parser('.\itba\eventos\eventos_gold.json')
    clienteGOLD = dataGOLD.cliente 
    eventosGOLD = dataGOLD.eventos
    razones = errores.Buscador(eventosGOLD, clienteGOLD.cuenta)
    htmlGOLD = reporte.GetHTML(clienteGOLD, razones.razones)
    htmlGOLD.get_html()

if str(sys.argv[1]) == "CLASSIC":
    dataCLASSIC = parseador.Parser('.\itba\eventos\eventos_classic.json')
    clienteCLASSIC = dataCLASSIC.cliente 
    eventosCLASSIC = dataCLASSIC.eventos
    razones = errores.Buscador(eventosCLASSIC, clienteCLASSIC.cuenta)
    htmlCLASSIC = reporte.GetHTML(clienteCLASSIC, razones.razones)
    htmlCLASSIC.get_html()

if str(sys.argv[1]) == "BLACK":
    dataBLACK = parseador.Parser('.\itba\eventos\eventos_black.json')
    clienteBLACK = dataBLACK.cliente 
    eventosBLACK = dataBLACK.eventos
    razones = errores.Buscador(eventosBLACK, clienteBLACK.cuenta)
    htmlBLACK = reporte.GetHTML(clienteBLACK, razones.razones)
    htmlBLACK.get_html()

