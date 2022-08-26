# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
import tkinter
from tkinter import StringVar
from tkinter import ttk

# Creamos una ventana
window = tkinter.Tk()               # Instancia de Tk
window.title( 'Ejericicio 2 - Tema 10' )

# Define dimensiones
window.columnconfigure( 0, weight = 1 )
window.rowconfigure( 0, weight = 3 )

default_msg = 'Selecciona una opción'

languages = ( 'JavaScript', 'PHP', 'Python', 'Ruby', 'Dart', 'Rush', 'Perl', 'Go', 'Java', 'C', 'C++' )
lista_items = StringVar( value = languages )

msg = tkinter.StringVar( value = default_msg )
print( msg.get() )

def send_answer( event ) :
    for i in listbox_languages.curselection():
        print( f' > { listbox_languages.get( i ) }' )

def selected_item( event ):
    # curselection: retorna una tupla con los items del listbox
    for i in listbox_languages.curselection():
        print( listbox_languages.get( i ) )
        msg.set( f'Has seleccionado { listbox_languages.get( i ) }!' )
    
    print( msg.get() )
    label_answer.config( text = msg.get() )     # Establece nuevo texto al Componente Label

    

# Crea Componente Label
label_question = ttk.Label( window, text = 'El lenguaje que mas te gusta es:' )
label_question.grid(
    column = 0,
    row = 0,
    sticky = tkinter.W,
    pady = 3,
)

# Crea el Componente Listbox
listbox_languages = tkinter.Listbox(
    window,
    selectbackground = 'gray',
    listvariable = lista_items,    # lista que se desea mostrar
    height = 5,    # altura
)
listbox_languages.bind(
    '<<ListboxSelect>>',
    selected_item
)
listbox_languages.grid(
    column = 0,
    row = 1,
    sticky = tkinter.W,
    pady = 2,
    padx = 5
)

# Crea Componente Label
label_answer = ttk.Label( window, text = default_msg )
label_answer.grid(
    column = 0,
    row = 2,
    sticky = tkinter.W,
    pady = 3,
)

# Crea Componente Boton
button_send = ttk.Button(
    window,
    text = 'Responder',
    # command = selected_item
)
button_send.grid(
    column = 0,
    row = 3,
    sticky = tkinter.E,
    padx = 5,
    pady = 5
)
button_send.bind(
    '<Button-1>',
    send_answer         # Callback
)

if __name__ == "__main__" :
    window.mainloop()   

############################# otro ejemplo es #######################################

import tkinter
from tkinter import ttk

# Configuración inicial de pantalla
window = tkinter.Tk()
window.columnconfigure(0, weight = 1)
window.columnconfigure(0, weight = 2)

# Creación de lista con elementos
lista = ['La Renga', 'Slothrust', 'Iron Maiden', 'Annihilator', 'Blind Guardian']
lista_items = tkinter.StringVar(value = lista)
listbox = tkinter.Listbox(window, height=100, listvariable=lista_items)

# Etiqueta (Título)
label = tkinter.Label(text='Algunas bandas de Metal y Rock!')

# Posicionamiento de elementos en pantalla
label.grid(column=0,row=0, sticky=tkinter.N)
listbox.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()

################################# Mi ejercicio ###############################

import tkinter
from tkinter import StringVar
from tkinter import ttk

# Creamos una ventana
window = tkinter.Tk()  
window.attributes('-alpha',0.8)
window.title( 'by Bones' )

# Define dimensiones
window.geometry("230x250")

#set window color
window.configure(bg='black')

default_msg = 'Seleccion de color'

colores = ( 'azul', 'violeta', 'amarillo', 'rojo', 'verde')
lista_items = StringVar( value = colores )

msg = tkinter.StringVar( value = default_msg )
print( msg.get() )

def send_answer( event ) :
    for i in listbox_colores.curselection():
        print( f' > { listbox_colores.get( i ) }' )

def selected_item( event ):
    
    # curselection: retorna una tupla con los items del listbox
    for i in listbox_colores.curselection():
        print( listbox_colores.get( i ) )
        msg.set( f'Has seleccionado { listbox_colores.get( i ) }!' )
    
    print( msg.get() )
    label_answer.config( text = msg.get() )     # Establece nuevo texto al Componente Label

    

# Crea Componente Label
label_question = ttk.Label( window, text = 'El color que más te gusta es:' )
label_question.grid(
    column = 0,
    row = 0,
    sticky = tkinter.W,
    pady = 3,
)

# Crea el Componente Listbox
listbox_colores = tkinter.Listbox(
    window,
    selectbackground = 'grey',
    listvariable = lista_items,    
    height = 5,   
)
listbox_colores.bind(
    '<<ListboxSelect>>',
    selected_item
)
listbox_colores.grid(
    column = 0,
    row = 1,
    sticky = tkinter.W,
    pady = 2,
    padx = 5
)

# Crea Componente Label
label_answer = ttk.Label( window, text = default_msg )
label_answer.grid(
    column = 0,
    row = 2,
    sticky = tkinter.W,
    pady = 3,
)

# Crea Componente Boton
button_send = ttk.Button(
    window,
    text = 'Responder',
    # command = selected_item
)
button_send.grid(
    column = 0,
    row = 3,
    sticky = tkinter.W,
    padx = 5,
    pady = 5
)
button_send.bind(
    '<Button-1>',
    send_answer         
)
# Create a Button exit
button_x = ttk.Button(window, text='Terminar',command=window.destroy)
button_x.grid(
    column = 0,
    row = 4,
    sticky = tkinter.W,
    padx = 5,
    pady = 5
)
button_x.bind(
    '<Button-1>'       
)

if __name__ == "__main__" :
    window.mainloop()   