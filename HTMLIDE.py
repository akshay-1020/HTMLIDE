from tkinter import *
from PIL import ImageTk, Image
import os
import webbrowser

root = Tk()
root.minsize(650, 650)
root.maxsize(650, 650)
root.title("HTML IDE")
root.configure(bg = "dark olive green")

openimg = ImageTk.PhotoImage(Image.open("open.png"))
saveimg = ImageTk.PhotoImage(Image.open("save.png"))
exitimg = ImageTk.PhotoImage(Image.open("run.png").resize((30,30)))

lblfilename = Label(root, text="File Name", bg="dark olive green", fg = "white")
lblfilename.place(relx=0.28, rely=0.03, anchor=CENTER)

ibox = Entry(root)
ibox.place(relx=0.47, rely=0.03, anchor=CENTER)

mytxt = Text(root, width=80, height=35, bg="black", fg = "white")
mytxt.place(relx=0.5, rely=0.55, anchor=CENTER)

name = ""
def openfile():
    global name
    mytxt.delete(1.0, END)
    ibox.delete(0, END)
    txtfile = filedialog.askopenfilename(title="Open Html File", filetypes=(("Text Files", "*.html"),))
    onlyname = os.path.basename(txtfile)
    onlyonlyname = onlyname.split(".")[0]
    ibox.insert(END,onlyonlyname)
    root.title(onlyonlyname)
    txtfile = open(onlyname,"r")
    para = txtfile.read()
    mytxt.insert(END,para)
    txtfile.close()

def runfile():
    global name
    webbrowser.open(name)
    
def savefile():
    iname = ibox.get()
    file = open(iname+".html", 'w')
    content = mytxt.get("1.0", END)
    print(content)
    file.write(content)
    ibox.delete(0, END)
    mytxt.delete(1.0, END)
    messagebox.showinfo("Update", "File created successfully!")
    file.close()
    
openbtn = Button(root, image=openimg, command=openfile, bg="dark olive green", fg = "white")
openbtn.place(relx=0.04, rely=0.03, anchor=CENTER)

savebtn = Button(root, image=saveimg, command=savefile, bg="dark olive green", fg = "white")
savebtn.place(relx=0.1, rely=0.03, anchor=CENTER)

closebtn = Button(root, image=exitimg, command=runfile, bg="dark olive green", fg = "white")
closebtn.place(relx=0.16, rely=0.03, anchor=CENTER)

root.mainloop()
