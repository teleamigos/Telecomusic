import socket
import wave


"""---------------------------------------------------------------------
--------------------------List of songs------------------------------"""



"""---------------------------------------------------------------------
--------------------------Server-------------------------------------"""
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


"""---------------------------------------------------------------------
--------------------------Searching the song-------------------------"""

"""---------------------------------------------------------------------
--------------------------Opening a audio file-----------------------"""

audioToSend=wave.open('Orlando Glez-.wav','rb')
audioPackage=audioToSend.readframes(16)


"""---------------------------------------------------------------------
--------------------------Sending your song--------------------------"""


s.sendall(audioPackage)
