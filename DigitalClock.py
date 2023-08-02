import time
from tkinter import Label, Tk

app_window = Tk()
app_window.title("Digital CLock")
app_window.geometry("300x100")
app_window.resizable(1,1)

text_font= ("Lato", 50, 'bold')
background = "black"
foreground= "white"
border_width = 20

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def dclock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, dclock)

dclock()
app_window.mainloop()