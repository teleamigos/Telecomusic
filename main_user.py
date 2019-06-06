
from tkinter import *
import socket
import wave
import time


"""---------------------------------------------------------------------
--------------------------SendInfo-----------------------------------"""

def SendInfo(InfoToSend):
    #Realiza la conexion con el servidor para enviar informacion.


    print("This is your petition : ")
    print(InfoToSend)

    #Descriptor del socket
    """Send"""
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Descriptor
    sock.connect((IP,PORT))
    print("connecting to %s with %s",IP,PORT)
    sock.sendall(InfoToSend.encode('utf-8'))
    """Waiting for the server"""
    print("Your petition is being processed")
    server_reply=sock.recv(64)
    reply=server_reply.decode('utf-8')
    if reply=='1':
        print("Downloading your song...")
        inforfromserver=sock.recv(64)
        nCH=int.from_bytes(inforfromserver,'big',signed=True)
        inforfromserver=sock.recv(64)
        samplew=int.from_bytes(inforfromserver,'big',signed=True)
        inforfromserver=sock.recv(64)
        fs=int(inforfromserver.decode('utf-8'))
        inforfromserver=sock.recv(128)
        nframes=int(inforfromserver.decode('utf-8'))
        inforfromserver=sock.recv(64)
        compress_type=inforfromserver.decode('utf-8')
        inforfromserver=sock.recv(64)
        comp=inforfromserver.decode('utf-8')
        print(nCH)
        print(samplew)
        print(fs)
        print(nframes)
        print(compress_type)
        print(comp)
        AudioReceived.setnchannels(nCH)
        AudioReceived.setsampwidth(samplew)
        AudioReceived.setframerate(fs)
        AudioReceived.setnframes(nframes)
        AudioReceived.setcomptype(compress_type,comp)
        FrameReceived=sock.recv(64)
        while len(FrameReceived)>=0:

            AudioReceived.writeframes(FrameReceived)
            FrameReceived=sock.recv(64)
            print(FrameReceived)
        print("It's ok")
        AudioReceived.close()
        sock.close()
    else:
        print("This song is not available")
        AudioReceived.close()
        sock.close()


"""---------------------------------------------------------------------
--------------------------DownloadButton-----------------------------"""

def DownloadButton():
    #### Manda  una solicitud en forma de string al servvidor sobre la cancion
    ## que se quiere
    txt=entry.get()
    SendInfo(txt)
    #root.destroy()


"""--------------------------------------------------------------------
--------------------------Ventana principal-------------------------"""


IP='127.0.0.1'
PORT=3000
AudioReceived=wave.open("nombre.wav",'wb')
root=Tk()
root.configure(background="pale goldenrod")

text = Text(root, height=20, width=50,bg='pale goldenrod')
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text.tag_configure('big', font=('Verdana', 20, 'bold'))

text.insert(END,'\nTelecomusic\n', 'big')
texto = """
Puedes descargar las siguientes canciones\n
°LaFemme
°PinkFloyd
°ACDC
°TheRollingStones
°TheDoors
°Queen
°Soko
"""
text.insert(END, texto)
text.pack(side='left')
scroll.pack(side='right')

entry=Entry(root)
entry.pack(side='top',padx=30,pady=30)
entry.focus_set()
Dbutton=Button(root,text="Download",width=10,command=DownloadButton)
Dbutton.pack(side='left',padx=30,pady=30)



root.mainloop()
