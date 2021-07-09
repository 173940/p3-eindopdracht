import tkinter as tk
from tkinter import *
#dit is om tkinter te launchen
window = tk.Tk()
#dit is om de tekst in tkinter te ztten
label_out = tk.Label(master=window, text='Vul hier de prijs van je product in.')
label_out.pack()
#hier kan je de input doen
entry = tk.Entry(master=window, width=10)
entry.pack()
#hier kan je het submitten
btn_submit = tk.Button(master=window, text="Submit")
btn_submit.pack()

def submit(event):

    class BTW:

        def __init__(self, geld):
            self.geld = geld
        #dit is voor de berekening van de btw
        def berekeningen(self):
            try:
                label_out["text"] = "te betalen bedrag is: € " + str(int(self.geld) * 0.21)

            except:
                label_out["text"] = "je moet een getal invullen"
        
    p = BTW(entry.get())
    p.berekeningen()

btn_submit.bind("<Button-1>", submit)

window.mainloop()
