from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Gerenciador de Senhas")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

"""LABEL"""
website_label = Label()
website_label.config(text="Website")
website_label.grid(row=1, column=0)

email_label = Label()
email_label.config(text="Email/Username")
email_label.grid(row=2, column=0)

senha_label = Label()
senha_label.config(text="Senha")
senha_label.grid(row=3, column=0)
"""ENTRY"""
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

senha_entry = Entry(width=21)
senha_entry.grid(row=3, column=1)

"""Button"""
botao_gerar_senha = Button(text="Gerar senha")
botao_gerar_senha.grid(row=3, column=2)

botao_adicionar = Button(text="Adicionar", width=36)
botao_adicionar.grid(row=4, column=1, columnspan=2)


window.mainloop()
