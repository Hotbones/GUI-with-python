# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción
#  que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.
import tkinter
from tkinter import CENTER, Frame, StringVar
from tkinter import ttk

# Creamos una ventana
window = tkinter.Tk()               # Instancia de Tk
window.attributes('-alpha',0.8)     # Transparencia Tk
window.title( 'Tema 10 - GUI' )

default_msg = 'Selecciona una opción'

selected_language = tkinter.StringVar()
msg = tkinter.StringVar( value = default_msg )
print( selected_language.get() )
print( msg.get() )

def on_radiobutton_change( *args ) :
    msg.set( f'Has seleccionado { selected_language.get() }!' )
    print( msg.get() )

def send_answer( event ) :
    print( f' > { selected_language.get() }' )

def reset( event ) :
    selected_language.set( '' )
    msg.set( default_msg )
    label_answer.config( text = msg.get() )

def set_label_answer_text() :
    # Establece nuevo texto al Componente Label
    label_answer.config( text = msg.get() )

# Escucha por cambios en el valor de la variable
selected_language.trace_add( 'write', on_radiobutton_change )


# Crea Componente Label
label_question = ttk.Label( window, text = 'Que marca de auto te gusta más:' )
label_question.grid(
    column = 0,
    row = 0,
    sticky = tkinter.W,
    pady = 5,
)

languages = [ 'Audi', 'Volvo', 'Peugeot', 'BMW', 'Mercedez' ]
rb_options = []

for idx, language in enumerate( languages ):
    rb_options.append( 
        ttk.Radiobutton(
            window,
            text = language,
            value = language.upper(),
            variable = selected_language,
            command = set_label_answer_text
        ) 
    )
    rb_options[ idx ].grid(
        column = 0,
        row = idx + 1,
        sticky = tkinter.W,
        pady = 5,
        padx = 10
    )

#print( rb_options )

# Crea Componente Label
label_answer = ttk.Label( window, text = msg.get() )
label_answer.grid(
    column = 0,
    row = len( languages ) + 1,
    sticky = tkinter.W,
    pady = 3,
)

# Crea Componente Boton
button_send = ttk.Button( window, text = 'Enviar' )
button_send.grid(
    column = 1,
    row = len( languages ) + 2,
    sticky = tkinter.E,
    padx = 7,
    pady = 7
)
button_send.bind(
    '<Button-1>',
    send_answer         # Callback
)

# Crea Componente Boton
button_reset = ttk.Button( window, text = 'Reset' )
button_reset.grid(
    column = 1,
    row = len( languages ) + 3,
    sticky = tkinter.W,
    padx = 5,
    pady = 5
)
button_reset.bind(
    '<Button-1>',
    reset         # Callback
)

# Create a Button exit
button_x = ttk.Button(window, text='by Bones',command=window.destroy)
button_x.grid(
    column = 1,
    row = len( languages ) + 4,
    sticky = tkinter.N,
    padx = 3,
    pady = 3
)
button_x.bind(
    '<Button-1>',
    reset         
)



if __name__ == "__main__" :
    window.mainloop()   




#################################################################################

import tkinter
from tkinter import ttk

window = tkinter.Tk()

# Configuración de pantalla
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=6)

# Variable de registro de opción marcada
selected = tkinter.StringVar()

# función que desmarca la opción marcada
def reiniciar(evento):
    selected.set(None)
    t1.config(text='')

# Mostrando opción seleccionada
def mostrar():
    t1.config(text="{}".format(selected.get()))

# Elementos
# RadioButton
r1 = ttk.Radiobutton(window, text='Sí', value='Sí', command=mostrar, variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='No', command=mostrar, variable=selected)
r3 = ttk.Radiobutton(window, text='Quizá', value='Quizá', command=mostrar, variable=selected)
r4 = ttk.Radiobutton(window, text='Preguntar más tarde', value='Preguntar más tarde', command=mostrar, variable=selected)
r5 = ttk.Radiobutton(window, text='Prefiere no responder', value='Prefiere no responder', command=mostrar, variable=selected)
# Mostrador de selección
t1 = ttk.Label(window)
# Boton de Reinicio
b1 = ttk.Button(window, text='Reiniciar')
b1.bind('<Button-1>', reiniciar)

# Ubiciación de elementos en pantalla
r1.grid(column = 0, row=0, pady=5, padx=5)
r2.grid(column = 0, row=1, pady=5, padx=5)
r3.grid(column = 0, row=2, pady=5, padx=5)
r4.grid(column = 0, row=3, pady=5, padx=5)
r5.grid(column = 0, row=4, pady=5, padx=5)
t1.grid(column = 1, row=5, pady=5, padx=5)
b1.grid(column = 1, row=6, pady=7, padx=7)

window.mainloop()