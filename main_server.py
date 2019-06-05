import socket
import wave




"""---------------------------------------------------------------------
--------------------------findFile-------------------------------------"""
def findFile(lista,nombre):
    if nombre in lista:
        return 1
    else:
        return 0

"""---------------------------------------------------------------------
--------------------------main-------------------------------------"""
"""List of songs"""

lista = ['LaFemme.wav',
        'PinkFloyd',
        'ACDC',
        'LedZeppelin',
        'TheDoors',
        'TheRollingStones',
        'Queen',
        'Soko']

"""Server"""
IP='127.0.0.1'
PORT=3000
escritor=wave.open("tobesent.wav","wb")#Archivo que contiene info sobre la cancion elegida.

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((IP,PORT))
    s.listen()
    conn,addr=s.accept()
    with conn:
        print("Conected with ",addr)
        while True:
            data=conn.recv(1024)
            #print(data)
            if not data:
                break
"""Searching the song"""
isInList=findFile(lista,data)

if isInList == 1:
    print('Se envia la cancion al cliente')
    if nombre == 'Soko':
        print('funcion para elegir Soko.wav')
        #Nombre_archivo="nombredelarchivo.wav"
    if nombre == 'LaFemme':
        print('funcion para elegir LaFemme.wav')
    if nombre == 'PinkFloyd':
        print('funcion para elegir PinkFloyd.wav')
    if nombre == 'ACDC':
        print('funcion para elegir ACDC.wav')
    if nombre == 'LedZeppelin':
        print('funcion para elegir LedZeppelin.wav')
    if nombre == 'TheDoors':
        print('funcion para elegir TheDoors.wav')
    if nombre == 'TheRollingStones':
        print('funcion para elegir TheRollingStones.wav')
    if nombre == 'Queen':
        print('funcion para elegir Queen.wav')
    """Envia confirmacion"""
    #s.sendall(isInList)
    """Opening a audio file"""
    audioToSend=wave.open(Nombre_archivo,'rb')
    audioPackage=audioToSend.readframes(64)
    escritor.setparams(audioToSend.getparams())#Configuramos una variable que se ajuste a la cancion que vamos a enviar.
    """Enviar contenedor de archivo"""
    s.sendall(escritor.encode())
    """Enviando archivo por cada Frame"""
    while len(audioPackage)==256:
        s.sendall(audioPackage)
        audioPackage=audioToSend.readframes(64)
    print("All frames were sent")

else:
    print('Se devuelve mensaje de error al cliente')
    #Envia error





"""---------------------------------------------------------------------
--------------------------Sending your song--------------------------"""


s.sendall(audioPackage)
