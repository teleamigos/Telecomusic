
from tkinter import *
import socket


"""---------------------------------------------------------------------
--------------------------SendInfo-----------------------------------"""

def SendInfo(Information):
    #Realiza la conexion con el servidor para enviar informacion.
    IP='127.0.0.1'
    PORT=3000
    print("This is your petition : ")
    print(Information)



"""---------------------------------------------------------------------
--------------------------DownloadButton-----------------------------"""

def DownloadButton():
    #### Manda  una solicitud en forma de string al servvidor sobre la cancion
    ## que se quiere
    txt=entry.get()
    SendInfo(txt)
    root.destroy()


"""--------------------------------------------------------------------
--------------------------Ventana principal-------------------------"""
root=Tk()
root.title("Telecomusic")
root.configure(background="pale goldenrod")
entry=Entry(root)
entry.pack()
entry.focus_set()
Dbutton=Button(root,text="Download",width=10,command=DownloadButton)
Dbutton.pack()

root.mainloop()

"""Se cierra la ventana y continua con la conexion"""

print("Ya se mando")
