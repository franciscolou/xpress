class Divisao():
    def __init__(self, name, image, script_urls):
        self.name = name
        self.image = image
        self.script_urls = script_urls

g = Divisao('Guias', 'project/imgs/G.png', [('TF1', '')])
ap = Divisao('Academia Policial', 'project/imgs/Ap.png', [('TF1', ''), ('TF2', '')])
bme = Divisao('BME', 'project/imgs/BME.png', [('TF1', ''), ('TF2', ''), ('TF3', '')])
cro = Divisao('Corregedoria', 'project/imgs/Cro.png', [('TF1', ''), ('TF2', ''), ('TF3', ''), ('TF4', '')])
dd = Divisao('DD', 'project/imgs/DD.png', [('TF1', ''), ('TF2', ''), ('TF3', ''), ('TF4', ''), ('TF5', ''), ('TF6', ''), ('TF7', '')])
# got = Divisao('GOT', 'project/imgs/got.png', [])
# pf = Divisao('Professores', 'project/imgs/Pf.png', [])
# sl = Divisao('Sistema de Lotação', 'project/imgs/SL.png', [])
# sp = Divisao('Supervisores', 'project/imgs/Sp.png', [])

divisionsList = [g, ap, bme, cro, dd]
