from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

root = Tk()
menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(root, type="normal",tearoff=False)
fontMenu = Menu(root,tearoff=False)
ff_menu=Menu(root,tearoff=False,)
menu_bar.add_cascade(
    label="File",
    menu=file_menu
)
menu_bar.add_cascade(
    label='Font',
    menu=fontMenu
)

font_size = IntVar()
font_size.set(11)

font_family=StringVar()
font_family.set("times new roman")

filename = StringVar()
filename.set("")

root.title(" Text Editor ")
root.resizable(False, False)
root.geometry('1000x1000')

canvas = scrolledtext.ScrolledText(root,height=36,width=123,font=(font_family.get(),font_size.get()))
opened = False


# open and save file
# FILE
def openf():
    global opened
    global f
    try:
        f = filedialog.askopenfile(defaultextension='txt').name
        with open(f, 'r') as file:
            txt = file.read()
            canvas.delete("0.0", END)
            canvas.insert("1.0", txt)
        opened = True
        filename.set(f.split('/')[-1])
        print(filename.get())
        root.title(f"{filename.get()}")

    except Exception as e:
        print("ERROR OPENING")
        print(e)
        messagebox.showerror(title="ERROR OPENING FILE",message=f"{e}")


def new():
    global opened
    if messagebox.askokcancel(title="Warning",message="Do you want to save current file?"):
        save()
    opened=False
    canvas.replace('0.0',END,"")


def save_as():
    global opened
    file = filedialog.asksaveasfile(defaultextension='.txt')
    with open(file.name, 'w') as fn:
        fn.write(canvas.get('1.0', END))
    if not opened:
        filename.set(file.name.split('/')[-1])
        root.title(f"{filename.get()}")
    opened = True


def save():
    try:
        if opened and len(canvas.get('1.0', END).replace(" ", '')) != 0:
            with open(f, 'w') as file:
                file.write(canvas.get('1.0', END))
        elif not opened:
            save_as()

    except Exception as e:
        print("Problem Saving")

# font adjustment
# FONT
def inc():
    global font_size
    if font_size.get() < 50:
        font_size.set(font_size.get() + 2)
    canvas['font']=(font_family.get(),font_size.get())

def dec():
    global font_size
    if font_size.get() > 5:
        font_size.set(font_size.get() - 2)
    canvas['font'] = (font_family.get(), font_size.get())
def fontfamily(ff):
    global font_family
    font_family.set(ff)
    canvas['font'] = (font_family.get(), font_size.get())

# Adjusting Widgets
canvas.grid(row=1, column=0, columnspan=3, rowspan=5)
file_menu.add_command(
    label='New',
    command=new
)
file_menu.add_command(
    label='Open',
    command=openf
)
file_menu.add_command(
    label='Save',
    command=save
)
file_menu.add_command(
    label='Save As',
    command=save_as
)
fontMenu.add_command(
    label='++',
    command=inc
)
fontMenu.add_command(
    label='--',
    command=dec
)
fontMenu.add_cascade(
    label=' Font Family',
    menu = ff_menu
)

ff_menu.add_command(label='arial',command=lambda : fontfamily('arial'))
ff_menu.add_command(label='comfortaa',command=lambda : fontfamily('comfortaa'))
ff_menu.add_command(label='comic sans ms',command=lambda : fontfamily('comic sans ms'))
ff_menu.add_command(label='courier new',command=lambda : fontfamily('courier new'))
ff_menu.add_command(label='georgia',command=lambda : fontfamily('georgia'))
ff_menu.add_command(label='impact',command=lambda : fontfamily('impact'))
ff_menu.add_command(label='lexend',command=lambda : fontfamily('lexend'))
ff_menu.add_command(label='times new roman',command=lambda : fontfamily('times new roman'))

root.mainloop()
