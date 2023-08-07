import tkinter
from tkinter import messagebox

count = 0

msg_box = messagebox.showwarning("SE FUDEU PARÇA!", "VOCÊ FOI HACKEADO")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("ATENÇÃO!", "PARA SER DESHACKEADO PRECISO QUE ME RESPONDA UMA PERGUNTA...")

if msg_box == 'ok':
    msg_box = messagebox.askquestion("VOCÊ É GAY OU SE FAZ?", "CONFIRMA ISSO?")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("VOCÊ É GAY OU SE FAZ?", "CONFIRMA ISSO?")
    if (count ==3):
        msg_box = messagebox.showerror("PQ NAO ASSUME LOGO? :( ", "RUM, É MELHOR!")
        break

if msg_box == 'ok':
    msg_box = messagebox.askquestion("VOCÊ É GAY OU SE FAZ?", "CONFIRMA ISSO?")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("ASSUME BRUNAO, VOCÊ É GAY OU SE FAZ?", " CONFIRMA ISSO?")
    if (count ==3):
        msg_box = messagebox.showerror("EU GUARDO SEGREDO POW ", "VOCÊ É GAY OU SE FAZ?")
        break



if msg_box == 'yes':
    msg_box = messagebox.showinfo("EU GUARDO SEGREDO!", "SEMPRE SOUBE KK !")
