class Buscador():
    def __init__(self,eventos):
        self.eventos = [ x for x in eventos if x['estado']== 'RECHAZADA']
        
        print(self.eventos)