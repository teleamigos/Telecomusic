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
            print("--------------------------")
            nCH=audioToSend.getnchannels()
            time.sleep(1)
            connection.sendall(bytes([nCH]))
            samplew=audioToSend.getsampwidth()
            time.sleep(1)
            connection.sendall(bytes([samplew]))
            fs=audioToSend.getframerate()
            fs_str=str(fs)
            time.sleep(1)
            connection.sendall(bytes(fs_str,'utf-8'))
            nframes=audioToSend.getnframes()
            nframes_str=str(nframes)
            connection.sendall(bytes(nframes_str,'utf-8'))
            compress_type=audioToSend.getcomptype()
            time.sleep(1)
            connection.sendall(bytes(compress_type,'utf-8'))
            comp=audioToSend.getcompname()
            time.sleep(1)
            connection.sendall(bytes(comp,'utf-8'))
            print(nCH)
            print(samplew)
            print(fs)
            print(nframes)
            print(compress_type)
            print(comp)
            actualFrame=audioToSend.readframes(64)
            time.sleep(2)
            while len(actualFrame)>=0:
                connection.sendall(actualFrame)
                actualFrame=audioToSend.readframes(64)
            print("All frames were sent")
            audioToSend.close()
            connection.close()
