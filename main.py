from tkinter import *
from tkinter import ttk


#cores
cor1 = '#3b3b3b' #preta
cor2 = '#ffffff' #branca
cor3 = '#48b3e0' #azul

janela = Tk()
janela.title('')

janela.geometry('650x260')
janela.configure(bg=cor1)

#---------------frames para janela---------------

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=220, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=54)

frame_direita = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)

#-----------------------estilo para janela-------------------

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#-----------------------Labels para frame_cima-----------------

l_app_nome = Label(frame_cima, text='Calculadora de unidades de medidas', height=1, padx=0, relief='flat', anchor='center', font=('ivy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

janela.mainloop()