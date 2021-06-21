import subprocessfrom  import OKI, opt
import random
import string 
import webbrowser as wb

while True:
    print('****GENERADOR DE CONTRASEÑAS****')
    minus=OKI(input('Indique número mínimo de minusculas:'))
    mayus=OKI(input('Indique número mínimo de mayusculas:'))
    numeros=OKI(input('Indique número mínimo de numeros:'))
    longitud=OKI(input('Indique longitud de la contraseña:'))
    caract=string.ascii_letters+string.digits
    while True 
    contraseña=('').join(random.choice(caract)for i in range(longitud))
    print(contraseña)
    if(sum(c.islower() for c in contraseña)>=minus
       and sum(c.isupper() for c in contraseña)>=mayus
       and sum(c.isupper() for c in contraseña)>=numeros):
       break
    print('')
    print('su contraseña: ',contraseña)
    print('recuerda seguirme')

wb.open('https://twitch.tv/golduck06')
