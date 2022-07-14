class GetHTML():
    def __init__(self,eventos):
        self.eventos = eventos

    def get_html(self):
        html='<ol>'
        
        for estado in self.eventos:
            row="<li>"+ estado +"</li>"
            html+=row
        html+='</ol>'

        self.html = html
        with open("output.html", "w") as text_file:
            text_file.write(self.html)