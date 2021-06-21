import random
import string
import webbrowser as wb

def generar_password(n):
    s = ''
    caracteres = list(string,printable)
    caracteres = caracteres[:-6]
    for i in range(n):
        s += random.choice(caracteres)
    print(s)
    m = len(caracteres)
    p = (1/len(caracteres))**n
    print('La probabilidad de que adivinen tu contraseña es {:.2e}'.format(p))
    
wb.open('https://twitch.tv/golduck06')
