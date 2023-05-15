import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

#function for creating a new file
def NewFile():
 Display.title("Untitled") 
 TextArea.delete(1.0, END)

#function for opening a file
def OpenFile():
 file = askopenfilename(defaultextension=".txt", file=[("All Files","*"), ("Text Documents", ".txt")])

#function for saving a file
def SaveFile():
 file= filedialog.asksaveasfilename(initialfile='unititled.txt',defaultextension=".txt", filetypes=[("All Files", "**"), ("Text Documents","*.txt")])

#function for changing color of text
def ColorChange():
 color = colorchooser.askcolor(title="Pick a color")
 TextArea.config(fg=color[1])

#function for changing color of font 
def ChangeFont(*args):
 TextArea.config(font=(FontName.get(), SizeBox.get()))


 if file is None:
  return

 else:
   try:
     Display.title(os.path.basename(file))
     TextArea.delete(1.0, END)

     file = open(file, "r")

     TextArea.insert(1.0, file.read())

   except Exception:
    print("couldn't read file")

   finally:
    file.close()


 if file is None:
  return

 else:
   try:
     Display.title(os.path.basename(file))
     file = open(file, "w")
     file.write(TextArea.get(1.0, END))

   except Exception: 
    print("couldn't save file")

   finally:
    file.close()

def cut():
 TextArea.event_generate("<<Cut>>")

def copy():
 TextArea.event_generate("<<Copy>>")

def paste():
 TextArea.event_generate("<<Paste>>")

def about():
 showinfo("About this program", "This is a text editor app")

def quit():
 Display.destroy()

Display= Tk()
Display.title("Text editor ")
file = None

window_width = 500
window_height = 500
screen_width = Display.winfo_screenwidth() 
screen_height = Display.winfo_screenheight()

x= int((screen_width/2) - (window_width/2))
y= int((screen_height/2) - (window_height/2))

Display.geometry("{}x{}+{}+{}".format(window_width,window_height, x, y))

FontName = StringVar(Display)
FontName.set("Arial")

FontName = StringVar(Display)

FontName.set("Arial")

FontSize = StringVar(Display) 
FontSize.set("25")

TextArea = Text(Display, font=(FontName.get(),FontSize.get()))

ScrollBar = Scrollbar(TextArea)

Display.grid_rowconfigure(0, weight=1) 
Display.grid_columnconfigure(0, weight=1)
TextArea.grid(sticky=N + E + S + W)

ScrollBar.pack(side=RIGHT, fill=Y) 
TextArea.config(yscrollcommand=ScrollBar.set)

Frame = Frame(Display) 
Frame.grid()

#making the color button
ColorButton= Button(Frame, text="color", command=ColorChange)
ColorButton.grid(row=0, column=0)

FontBox = OptionMenu(Frame, FontName, *font.families(), command=ChangeFont)
FontBox.grid(row=0, column=1)

SizeBox = Spinbox(Frame, from_=1, to=100, textvariable=FontSize, command=ChangeFont)
SizeBox.grid(row=0, column=2)


#Creating  menubar

MenuBar= Menu(Display)
Display.config(menu=MenuBar)

#File 
FileMenu = Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="File", menu=FileMenu)
FileMenu .add_command(label="New", command=NewFile)
FileMenu .add_command(label="Open", command=OpenFile)
FileMenu .add_command(label="Save", command=SaveFile)
FileMenu .add_separator()
FileMenu .add_command(label="Exit", command=quit)

#edit
EditMenu=Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy) 
EditMenu.add_command(label="Paste", command=paste)

#help
HelpMenu =Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="Help", menu=HelpMenu) 
HelpMenu.add_command(label="About", command=about)

Display.mainloop()