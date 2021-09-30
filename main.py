from tkinter import *
from tkinter import ttk
from tkinter import font


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

l_app_nome = Label(frame_cima, text='Calculadora de unidades de medidas', height=1, padx=0, relief='flat', anchor='center', font=('ivy 13 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

#-----------------------configurando frame_esquerda-------------------

b_0 = Button(frame_esquerda, text='Massa', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

b_1 = Button(frame_esquerda, text='Tempo', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

b_2 = Button(frame_esquerda, text='Comprimento', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

b_3 = Button(frame_esquerda, text='Àrea', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

b_4 = Button(frame_esquerda, text='Quantidade', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

b_5 = Button(frame_esquerda, text='Velocidade', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

b_6 = Button(frame_esquerda, text='Temperatura', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_6.grid(row=3, column=0, sticky=NSEW, pady=5, padx=5)

b_7 = Button(frame_esquerda, text='Energia', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_7.grid(row=3, column=1, sticky=NSEW, pady=5, padx=5)

b_8 = Button(frame_esquerda, text='Pressão', width=10, height=2, relief='flat', overrelief='solid', anchor='nw', font=('ivy 10 bold'), bg=cor3, fg=cor2)
b_8.grid(row=3, column=2, sticky=NSEW, pady=5, padx=5)

janela.mainloop()