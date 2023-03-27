import tkinter as tk
from tkinter import Menu, Text
from tkinter import END, ttk
import os
from tkinter import filedialog as fd

# ---------- Callbacks --------------------
text = ''
def run_file():
    text_content = text.get("1.0", "end-1c")
    file = open('temp.py', 'w')
    file.write(text_content + "\n")
    file.close()

    os.system("start /wait cmd /k python main.py temp.py")

def open_file():
    filetypes = (('Python files', '*.py'),
                 ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    with open(filename, 'r') as file:
        data = file.read()

    text.insert("1.0", data)





# ---------- Syntax highlighter ---------------

# dictionary to hold words and colors
highlightWords = {'if': 'blue',
                  'else': 'blue',

                  '!': 'green',
                  '==': 'green',
                  '!=': 'green',
                  '>=': 'green',
                  '<=': 'green',
                  '>': 'green',
                  '<': 'green',

                  'int': 'magenta',
                  'bool': 'magenta',
                  'real': 'magenta',
                  'String': 'magenta',

                  'const': 'red',

                  'return': 'blue',
                  'print': 'blue',
                  'for': 'blue',
                  'while': 'blue',
                  'input': 'blue'

                  }

def highlighter(event):
    '''the highlight function, called when a Key-press event occurs'''
    for k,v in highlightWords.items(): # iterate over dict
        startIndex = '1.0'
        while True:
            startIndex = text.search(k, startIndex, END)
            if startIndex:
                endIndex = text.index('%s+%dc' % (startIndex, (len(k))))
                text.tag_add(k, startIndex, endIndex)
                text.tag_config(k, foreground=v)
                startIndex = endIndex
            else:
                break

# ------------------ root window ------------

root = tk.Tk()
root.title('Trabalho final de Compiladores')

# ----------------- File Menu ---------------

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(
    label='Open File',
    command=open_file
)

file_menu.add_command(
    label='Run',
    command=root.destroy
)

file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)

# --------------- Text Area -----------------

text = Text(root, height=20)
text.pack()

text.bind('<Key>', highlighter) # bind key event to highlighter()

# --------------- Button Area ---------------

run_icon = tk.PhotoImage(file='./icon_run.png')
run_button = ttk.Button(
    root,
    text='Run',
    image=run_icon,
    command=run_file
)

run_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()