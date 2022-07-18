import webbrowser

class GetHTML():
    def __init__(self, cliente, razones):
        self.cliente = cliente 
        self.razones = razones

    def get_html(self):       
        f = open(str(self.cliente.dni) + str(self.cliente.apellido) +'.html', 'w', encoding='utf-8')

        CONTENIDO= f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                <link rel="stylesheet" href="style.css">

                <title>ITBANK - GRUPO 6</title>
            </head> 
            <body class="fondo">
                <h2 class="titulo">Detalle Cuenta</h2> <br>
                <div class=" titular">
                    <div><p>Nombre: {self.cliente.nombre + " " + self.cliente.apellido}<p><div>
                    <div><p>DNI: {self.cliente.dni}</p></div>
                    <div><p>Direccion: {self.cliente.dir.calle} {self.cliente.dir.numero}, {self.cliente.dir.ciudad} </p></div>
                    <div><p>Tipo de cuenta: {self.cliente.tipo}</p></div>
                </div>
                <div class="container">
                    <table class="tabla col-5">
                        <tr class="prin">
                            <th >Fecha</th>
                            <th>Tipo</th> 
                            <th>Estado</th> 
                            <th>Monto</th> 
                            <th>Razón</th> 
                        </tr> """

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
                </div>            
            </body>
            </html>"""

        
        f.write(CONTENIDO)
        f.close()
        webbrowser.open_new_tab(str(self.cliente.dni) + str(self.cliente.apellido) + '.html')