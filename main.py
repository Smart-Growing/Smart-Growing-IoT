import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mongoclean
import firestore
import report


# VENTANA RAIZ

root = Tk()
root.title("Smart Growing")
root.resizable(False,False)
root.geometry("620x320")
root.config(bg="green")


# INVOCACION DE FUNCIONES





def internetOfThings():
    for i in range(20):
        mongoclean.mongoRealtime()
        mongoclean.mongoUpdate()
        mongoclean.fetchingData()
        firestore.updateFirestore()
        firestore.generarReportes()
        firestore.obtenerReportes()
        time.sleep(10)
        
def descargarReporte():
    report.crearJson()
    time.sleep(5)
    report.fetchReportes()



# INTERFAZ

monFrame=Frame()
monFrame.pack(fill="y",expand="True")
monFrame.config(relief="sunken")
monFrame.config(bd=35)
monFrame.config(width="350",height="380")
monFrame.config(bg="yellow")
monFrame.config(cursor="hand2")

hidOriginal = (Image.open("img/hidro.png"))
resizeHidro = hidOriginal.resize((220,90), Image.Resampling.LANCZOS)
hidroImagen = ImageTk.PhotoImage(resizeHidro)
hidroLabel = Label(monFrame, image=hidroImagen).place(x=105, y=160)

logoOriginal= (Image.open("img/smartgrowinglogo.png"))
resizeLogo= logoOriginal.resize((80,80), Image.Resampling.LANCZOS)
imgLogo = ImageTk.PhotoImage(resizeLogo)
logoLabel = Label(monFrame, image=imgLogo)
logoLabel.grid(row=0,column=0, padx=5)

cloudOriginal = (Image.open("img/cloudIcon.png"))
resizeCloud = cloudOriginal.resize((80,60), Image.Resampling.LANCZOS)
cloudImage = ImageTk.PhotoImage(resizeCloud)
cloudLabel = Label(monFrame, image=cloudImage)
cloudLabel.grid(row=0,column=2, padx=5)

blueOriginal = (Image.open("img/blue.png"))
resizeBlue = blueOriginal.resize((35,35), Image.Resampling.LANCZOS)
blueImage = ImageTk.PhotoImage(resizeBlue)
blueLabel = Label(monFrame, image=blueImage)
blueLabel.grid(row=6,column=0,padx=5)

infoLabel = Label(monFrame, text="Conexión con Database \n Conectar dispositivo a la nube", fg="green", font=(18))
infoLabel.grid(row=0,column=1, padx=5)

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

conexionLabel=Label(monFrame, text="Puerto Serial : ")
conexionLabel.grid(row=5,column=0, sticky="w", pady=5, padx=5)

# BOTON DE CONEXION PARA INVOCAR FUNCIONALIDADES

botonInicio = Button(monFrame, text="Sincronizar", width=20, command=internetOfThings)
botonInicio.grid(row=6, column=1, sticky="w", pady=5, padx=5)

botonReporte = Button(monFrame, text="Obtener Histórico", width=20, command=descargarReporte)
botonReporte.grid(row=6, column=2, sticky="w", pady=5, padx=5)

#if __name__ == '__main__':
#    root.mainloop()

root.mainloop()