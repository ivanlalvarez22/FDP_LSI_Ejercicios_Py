import pywhatkit as kit
import datetime

# Número de teléfono al que se enviará el mensaje (debe incluir el código de país sin el signo +)
numero = "+5493854742118"  # Reemplaza con el número al que quieras enviar el mensaje

# Mensaje que deseas enviar
mensaje = "Hola, este es un mensaje enviado desde Python usando pywhatkit!"

# Hora en la que quieres enviar el mensaje (formato HH, MM)
hora_envio = datetime.datetime.now().hour
minuto_envio = datetime.datetime.now().minute + 1  # Añade 1 minutos al tiempo actual

# Enviar el mensaje
kit.sendwhatmsg(numero, mensaje, hora_envio, minuto_envio)

print(f"Mensaje enviado a {numero} a las {hora_envio}:{minuto_envio}")
