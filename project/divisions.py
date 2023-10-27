class Divisao():
    def __init__(self, name, image, script_urls, color):
        self.name = name
        self.image = image
        self.script_urls = script_urls
        self.color = color


g = Divisao("Guias", "xpress/project/imgs/G.png", [("CFSd", ""), ("CFCb", "")], "#530c0c")
c = Divisao("Comissão", "xpress/project/imgs/C.png", [("menor ideia", ""), ("menor ideia", ""), ("menor ideia", ""), ("menor ideia", "")], "#fea901")
r = Divisao("Rondas", "xpress/project/imgs/R.png", [("menor ideia", ""), ("menor ideia", ""), ("menor ideia", ""), ("menor ideia", "")], "#ea7400")
amfe = Divisao("AMFE", "xpress/project/imgs/AMFE.png", [("menor ideia", ""), ("menor ideia", ""), ("menor ideia", ""), ("menor ideia", "")], "#1f1f1f")
epfo = Divisao("EPFO", "xpress/project/imgs/EPFO.png", [("menor ideia", ""), ("menor ideia", ""), ("menor ideia", ""), ("menor ideia", "")], "#ae0709")
pf = Divisao("Pf", "xpress/project/imgs/Pf.png", [("menor ideia", ""), ("menor ideia", ""), ("menor ideia", ""), ("menor ideia", "")], "#d2d2d2")


divisionsList = [g, c, r, amfe, epfo, pf]
