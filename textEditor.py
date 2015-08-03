from Tkinter import *

root = Tk()

screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

root.title("Text Editor")
root.focus_set()
root.geometry("800x600")
root.configure(background="light blue")

app = Frame(root, background="light blue")
app.grid()

scrollbar = Scrollbar(app)
scrollbar.pack(side=RIGHT, fill=Y)

txtPaper = Text(app, wrap="word", yscrollcommand=scrollbar.set, bg="white")
scrollbar.config(command=txtPaper.yview)

txtFileName = Entry(app)

def new():
    txtPaper.delete('1.0', END)

def save():
    f = open(txtFileName.get()+".txt", 'w')
    a = txtPaper.get("1.0",END)
    f.write(a)
    f.close()

btnNew = Button(app, text="NEW", command=new, bg="white")
btnSave = Button(app, text="SAVE", command=save, bg="white")
lblFileName = Label(app, text="File Name: ", bg="light blue")


def select_all(event):
    txtPaper.tag_add(SEL, "1.0", END)
    txtPaper.mark_set(INSERT, "1.0")
    txtPaper.see(INSERT)
    return 'break'

txtPaper.bind("<Control-Key-a>", select_all)
txtPaper.bind("<Control-Key-A>", select_all)

btnNew.pack(side="top")
btnSave.pack(side="top")
lblFileName.pack()
txtFileName.pack()
txtPaper.pack(side="bottom")

root.mainloop()
