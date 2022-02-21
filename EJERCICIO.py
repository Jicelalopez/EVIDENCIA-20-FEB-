import re

txt = "En esta cadena se encuentra una palabra magica"

x= re.search('magica', txt)
print(x.star () )
print(x.end() )
print(x.span() )
print(x.string )

if x:
    print("Si se ha encontrado!")
else:
    print("NO encontrado")