class Divisao():
    def __init__(self, name, image, script_urls):
        self.name = name
        self.image = image
        self.script_urls = script_urls

g = Divisao('Guias', 'xpress/project/imgs/G.png', [('TF1', '')])

ap = Divisao('Academia Policial', 'xpress/project/imgs/Ap.png', [('TF1', ''), ('TF2', '')])

bme = Divisao('BME', 'xpress/project/imgs/BME.png', [('TF1', ''), ('TF2', ''), ('TF3', '')])

cro = Divisao('Corregedoria', 'xpress/project/imgs/Cro.png', [('TF1', ''), ('TF2', ''), ('TF3', ''), ('TF4', '')])

dd = Divisao('DD', 'xpress/project/imgs/DD.png', [('TF1', ''), ('TF2', ''), ('TF3', ''), ('TF4', ''), ('TF5', ''), ('TF6', ''), ('TF7', '')])

# got = Divisao('GOT', 'xpress/project/imgs/got.png', [])

# pf = Divisao('Professores', 'xpress/project/imgs/Pf.png', [])

# sl = Divisao('Sistema de Lotação', 'xpress/project/imgs/SL.png', [])

# sp = Divisao('Supervisores', 'xpress/project/imgs/Sp.png', [])


divisionsList = [g, ap, bme, cro, dd]
