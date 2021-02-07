Numero = input('Digite o número a ser convertido para a base 10: ')
Base = input('Qual a base do número informado? ')
Numero = Numero.replace(',','.')
if (Numero.count('.') > 1) or (Numero.count(Base) > 0):
    print('Numero', Numero, 'na base', Base, 'é inválido')
else:
    Lista = []
    for d in Numero:
        Lista.append(d)
    sd = Numero.find('.')
    x = 0.0
    i = 0
    print(Lista)
    print('sd', sd)
    for e in Lista:
        i += 1
        exp = (sd-i)
        y = int(e, base = Base)
        if (i == (sd + 1)):
            x += 0.0
        else:
             x +=  y * Base ** exp
        print(x)
    print('Número', Numero, 'na base', Base, 'convertido é:', x)
