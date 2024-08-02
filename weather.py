from tkinter import *
from PIL import Image,ImageTk
import requests
url="https://api.openweathermap.org/data/2.5/weather"
Apikey="65e907399b855ece5bc78addbabcb3b2"
iconUrl="https://openweathermap.org/img/wn/{}@2x.png"


app=Tk()
app.geometry("300x450")
app.title("Cash Hava Durumu")

metrapol= Entry(app,justify="center")
metrapol.pack(fill=BOTH,ipady=10,padx=10,pady=5)
metrapol.focus()

aramaB=Button(app,text="Arama",font=("arabolical",15))
aramaB.pack(fill=BOTH,ipady=10,padx=20)

iconL=Label(app)
iconL.pack()

locationL= Label(app,font=("arabolical",40))
locationL.pack()

tempL=Label(app,font=("arabolical",50,"bold"))
tempL.pack()

condL=Label(app,font=("arabolical",20))
condL.pack()

app.mainloop()