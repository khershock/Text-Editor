from tkinter import *
import tkinter.filedialog
import os 
import tkinter.messagebox

file_name = None

PROGRAM_NAME = "Korys Text Editor"

root = Tk()
root.geometry('450x450')
root.title(PROGRAM_NAME)


# Adding Cut, Copy, Paste, and Undo using Text Widget built-in Functionality

def cut():
    main_text.event_generate("<<Cut>>")
    return "break"

def copy():
    main_text.event_generate("<<Copy>>")
    return "break"

def paste():
    main_text.event_generate("<<Paste>>")
    return "break"

def undo():
    main_text.event_generate("<<Undo>>")
    return "break"

# Select all function implementaion

def select_all(event=None):
    main_text.tag_add('sel', '1.0', 'end')
    return "break"

# All Implementations for the file menu

def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension='.txt',
                                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        main_text.delete(1.0, END)
        with open(file_name) as _file:
            main_text.insert(1.0, _file.read())

def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    main_text.delete(1.0, END)

def write_file(file_name):
    try:
        content = main_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        tkinter.messagebox.showwarning("Save", "Could not save the file.")

def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension='.txt',
                                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"

def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_file(file_name)
    return "break"

# About, Help, and Exit messages

def about_message(event=None):
    tkinter.messagebox.showinfo("About", PROGRAM_NAME + "\nCreated by: Kory Hershock")

def help_message(event=None):
    tkinter.messagebox.showinfo("Help", "\n Email: Khershockhh@gmail.com\n Phone: (269)-274-5695")

def exit(event=None):
    if tkinter.messagebox.askokcancel("Exit", "Are you sure you want to quit?"):
        root.destroy()

menu_bar = Menu(root) # menu begins

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", accelerator="Ctrl+N", command=new_file)
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save)
file_menu.add_command(label="Save As", accelerator="Shift+Ctrl+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Quit", accelerator="Ctrl+Q", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=undo)
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=about_message)
about_menu.add_command(label="Help", command=help_message)
menu_bar.add_cascade(label="About", menu=about_menu)

root.config(menu=menu_bar) # menu ends

# Implementing Main text box with scrollbar on right side
main_text = Text(root, wrap='word', undo=1)
main_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(main_text)
main_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=main_text.yview)
scroll_bar.pack(side='right', fill='y')

# Binding the Select All function to Control-A and Command-A(for Mac users)
main_text.bind('<Control-A>', select_all)
main_text.bind('<Control-a>', select_all)
main_text.bind('<Command-A>', select_all)
main_text.bind('<Command-a>', select_all)

# Binding the New File function to Control-N and Command-N(for Mac users)
main_text.bind('<Control-N>', new_file)
main_text.bind('<Control-n>', new_file)
main_text.bind('<Command-N>', new_file)
main_text.bind('<Command-n>', new_file)

# Binding the Open File function to Control-O and Command-O(for Mac users)
main_text.bind('<Control-O>', open_file)
main_text.bind('<Control-o>', open_file)
main_text.bind('<Command-O>', open_file)
main_text.bind('<Command-o>', open_file)

# Binding the save function to Control-S and Command-S(for Mac users)
main_text.bind('<Control-S>', save)
main_text.bind('<Control-s>', save)
main_text.bind('<Command-S>', save)
main_text.bind('<Command-s>', save)

root.protocol("WM_DELETE_WINDOW", exit)
root.mainloop()