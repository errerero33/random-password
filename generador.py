from random import choice

longitud = int(raw_input('Longitud del pass: '))
valores = “0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#%&+”
p = “”
p = p.join([choice(valores) for i in range(longitud)])
print p
raw_input()
