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

lista = ['LaFemme',
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
else:
    print('Se devuelve mensaje de error al cliente')
"""---------------------------------------------------------------------
--------------------------Opening a audio file-----------------------"""

audioToSend=wave.open('Orlando Glez-.wav','rb')
audioPackage=audioToSend.readframes(16)


"""---------------------------------------------------------------------
--------------------------Sending your song--------------------------"""


s.sendall(audioPackage)
