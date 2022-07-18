import webbrowser

class GetHTML():
    def __init__(self, cliente, razones):
        self.cliente = cliente 
        self.razones = razones

    def get_html(self):       
        f = open(str(self.cliente.dni) + '.html', 'w', encoding='utf-8')

        CONTENIDO= f"""
            <html>
            <head>
                <title>ITBANK - GRUPO 6</title>
            </head>
            <body>
                <div><p>Nombre: {self.cliente.apellido + " " +self.cliente.nombre}<p><div>
                <div><p>DNI: {self.cliente.dni}</p></div>
                <div><p>Direccion: {self.cliente.dir.calle} {self.cliente.dir.numero}, {self.cliente.dir.ciudad} </p></div>
                <div><p>Tipo de cuenta: {self.cliente.tipo}</p></div>
                <table>
                    <tr>
                        <th>Fecha</th>
                        <th>Tipo</th> 
                        <th>Estado</th> 
                        <th>Monto</th> 
                        <th>Razón</th> 
                    </tr>"""

        for razon in self.razones:
            CONTENIDO+=f""" 
                    <tr> 
                        <th>{razon.evento["fecha"]}</th>
                        <th>{razon.evento["tipo"]}</th> 
                        <th>{razon.evento["estado"]}</th> 
                        <th>${razon.evento["monto"]}</th> 
                        <th>{razon.razon}</th>
                    </tr>"""
                      

        CONTENIDO+=f""" 
                </table>               
            </body>
            </html>"""

        
        f.write(CONTENIDO)
        f.close()
        webbrowser.open_new_tab(str(self.cliente.dni) + '.html')