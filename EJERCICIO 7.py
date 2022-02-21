import re
def buscar(patrones, texto):
    for patron in patrones:
    print(re.findll(patron, texto) )
    texto = "hola h0la Hola mola m0la Mol
    patrones = {'´{a-z}la', 'h{0-9}la', '´{A-z}{4}', '{A-Z}{A-z0-9}{3}'}
    
    Print (buscar(patrones, texto))
    