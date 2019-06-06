import socket
import wave
import time




"""---------------------------------------------------------------------
--------------------------findFile-------------------------------------"""
def findFile(lista,nombre):
    if nombre in lista:
        index = lista.index(nombre)
        return index
    else:
        return 14

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
        'Soko',
        'Orlando Glez-']

"""Server"""
IP='127.0.0.1'
PORT=3000
escritor=wave.open("tobesent.wav","wb")#Archivo que contiene info sobre la cancion elegida.

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Descriptor
sock.bind((IP,PORT))
sock.listen(1)
while True:
    print("waiting...")
    connection,client_address=sock.accept()
    while True:
        print("Connecting...")
        data=connection.recv(1024)
        if not data:
            break
        nombre=data.decode('utf-8')
        print("your petition : ",nombre)
        """Searching the song"""
        InList=findFile(lista,nombre)
        if InList==14:
            print("your petition is not in our list")
            time.sleep(2)
            connection.sendall('0'.encode('utf-8'))
            connection.close()
        else:
            print("Index in list: ",InList)
            time.sleep(2)
            connection.sendall('1'.encode('utf-8'))
            """Opening the wav file"""
            file_name=nombre+'.wav'
            audioToSend=wave.open(file_name,'rb')
            print("abierto ok")
            nCH=audioToSend.getnchannels()
            time.sleep(1)
            connection.sendall(bytes([nCH]))
            samplew=audioToSend.getsampwidth()
            connection.sendall(bytes([samplew]))
            fs=audioToSend.getframerate()
            fs_str=str(fs)
            connection.sendall(bytes(fs_str,'utf-8'))
            nframes=audioToSend.getnframes()
            connection.sendall(bytes([nf]))
            compress_type=audioToSend.getcomptype()
            connection.sendall(bytes([compress_type]))
            comp=audioToSend.getcompname()
            connection.sendall(bytes([comp]))
            print(nCH)
            print(samplew)
            print(fs)
            print(nframes)
            print(compress_type)
            print(comp)
