import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import bridge
from conector import validarUsuario, validarPlaca, updateSensorInterfaz
from conector import infoRealtime, updateSensor
root = Tk()
root.title("Smart Growing")
root.resizable(False,False)
root.geometry("620x420")
root.config(bg="green")

def logearUsuario():
    usuario = textoUsuario.get()
    password = textoPass.get()
    login = False
    if validarUsuario(usuario,password):
        login = True
        saludoBienvenida()
        checkUser = Label(monFrame, text="✓", fg="green")
        checkUser.grid(row=2, column=2)
        checkPass = Label(monFrame, text="✓", fg="green")
        checkPass.grid(row=3, column=2)
        habilitarPuerto()
    else:
        errorLogin = Label(monFrame, text="Usuario y/o contraseña incorrectos", fg="red")
        errorLogin.grid(row=3, column=2)
    return login

def saludoBienvenida():
    if logearUsuario:
        usuario = textoUsuario.get()
        textoBienvenida = Label(monFrame, text="Bienvenido " +usuario)
        textoBienvenida.grid(row=7, column=2, sticky="w", pady=5, padx=5)

def habilitarPuerto():
    modulo = False
    puertoSerial = opcionConexion.get()
    if bridge.receptInterfaz(puertoSerial):
        modulo = True
        checkPuerto = Label(monFrame, text="✓", fg="green")
        checkPuerto.grid(row=5, column=2)
        comprobarConexion()
    else:
        errorPuerto = Label(monFrame, text="✓ Datos actualizados", fg="green")
        errorPuerto.grid(row=11, column=2)
    return modulo

def comprobarConexion():
    checkAll = Label(monFrame, text="✓ Conexión Satisfactoria", fg="green")
    checkAll.grid(row=9, column=2)

def ejecutarFunciones():
    logearUsuario()
    while habilitarPuerto():
        puertoSerial = opcionConexion.get()
        bridge.receptInterfaz(puertoSerial)
        infoRealtime()
        updateSensor()
    
monFrame=Frame()
monFrame.pack(fill="y",expand="True")
monFrame.config(relief="sunken")
monFrame.config(bd=35)
monFrame.config(width="550",height="450")
monFrame.config(bg="yellow")
monFrame.config(cursor="hand2")

hidOriginal = (Image.open("img/hidro.png"))
resizeHidro = hidOriginal.resize((220,90), Image.ANTIALIAS)
hidroImagen = ImageTk.PhotoImage(resizeHidro)
hidroLabel = Label(monFrame, image=hidroImagen).place(x=65, y=260)

logoOriginal= (Image.open("img/smartgrowinglogo.png"))
resizeLogo= logoOriginal.resize((80,80), Image.ANTIALIAS)
imgLogo = ImageTk.PhotoImage(resizeLogo)
logoLabel = Label(monFrame, image=imgLogo)
logoLabel.grid(row=0,column=0, padx=5)

cloudOriginal = (Image.open("img/cloudIcon.png"))
resizeCloud = cloudOriginal.resize((80,60), Image.ANTIALIAS)
cloudImage = ImageTk.PhotoImage(resizeCloud)
cloudLabel = Label(monFrame, image=cloudImage)
cloudLabel.grid(row=0,column=2, padx=5)

blueOriginal = (Image.open("img/blue.png"))
resizeBlue = blueOriginal.resize((35,35), Image.ANTIALIAS)
blueImage = ImageTk.PhotoImage(resizeBlue)
blueLabel = Label(monFrame, image=blueImage)
blueLabel.grid(row=6,column=0,padx=5)

infoLabel = Label(monFrame, text="Conexión con Database \n Conectar bluetooth a la nube", fg="green", font=(18))
infoLabel.grid(row=0,column=1, padx=5)

textoUsuario=Entry(monFrame, width="40")
textoUsuario.grid(row=2,column=1, sticky="w", pady=5, padx=5)
textoUsuario.config(fg="green",justify="center")

textoPass=Entry(monFrame, width="40")
textoPass.grid(row=3,column=1, sticky="w", pady=5, padx=5)
textoPass.config(fg="green",justify="center",show="*")

opcionConexion=ttk.Combobox(
    monFrame, width="30",
    state="readonly",
    values=["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9",
    "COM10","COM11","COM12","COM13","COM14","COM15","COM16","COM17","COM18","COM19",
    "COM20","COM21","COM22","COM23","COM24","COM25","COM26","COM27","COM28","COM29",
    "COM30","COM31","COM32","COM33","COM34","COM35","COM36","COM37","COM38","COM39",
    "COM40","COM41","COM42","COM43","COM44","COM45","COM46","COM47"]
)
opcionConexion.grid(row=5,column=1, sticky="w", pady=5, padx=5)

usuarioLabel=Label(monFrame, text="Usuario : ")
usuarioLabel.grid(row=2,column=0, sticky="w", pady=5, padx=5)

passLabel=Label(monFrame, text="Contraseña : ")
passLabel.grid(row=3,column=0, sticky="w", pady=5, padx=5)

conexionLabel=Label(monFrame, text="Puerto Serial : ")
conexionLabel.grid(row=5,column=0, sticky="w", pady=5, padx=5)

botonInicio = Button(monFrame, text="Conectar Dispositivo", width=20, command=ejecutarFunciones)
botonInicio.grid(row=6, column=1, sticky="w", pady=5, padx=5)

root.mainloop()