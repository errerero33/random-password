import webbrowser as wb

print('si te sientes incomomdo respondiendo alguna pregunta pon algo random XD,lo usara igual')
Message1 = """Recuerda seguir a golduck06 en twitch \n
Antes de proceder, llene el siguiente formulario por favor(para hacer tu contraseña)."""


Message2 = '''Muchas gracias por tomarse el tiempo de llenar el formulario. 
De acuerdo a la informacion que nos acaba de proveer, procedemos a 
mostrarle su password para sus futuras operaciones.'''


Message3 = "Su password ha sido enviado a su escritorio en un documento de texto."

print (Message1)


name = input("Por favor introduzca su nombre: ")
country = input ('Por favor introduzca su pais de procedencia: ')
birthday = input ('Por favor introduzca su fecha de nacimiento: ')
city = input ('Por favor introduzca el estado donde vive: ')
phone = input ("Por favor introduzca su numero de telefono: ")
special = input('Por favor introduzca al menos tres caracteres especiales: ')


password = name[3]+country[4]+birthday[7]+city[2]+phone[1]+special[1]


print ('\n' + Message2 +" "+ password +'\n')


print (Message3 + '\n')

wb.open('https://twitch.tv/golduck06')


file = open ("/home/Desktop/password.txt","w" )
file.write (password)
file.close()

