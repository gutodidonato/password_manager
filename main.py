from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerar_senha():
    senha = criar_senha()
    senha_entry.insert(0, senha)
    
#Password Generator Project
def criar_senha():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    password_list = []
    
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
   
    senha = "".join(password_list)

    print(f"Sua senha gerada: {senha}")
    return senha


# ---------------------------- SAVE PASSWORD ------------------------------- #
def criar_arquivo_txt():
    try: 
        arquivo = open("senhas.txt", "r")
        print(arquivo.readlines())
    except FileNotFoundError:
        arquivo = open("senhas.txt", 'w+')
    saida = messagebox.askyesno(title=website_entry.get(), message=f"O email/usuario é {email_entry.get()}, a senha é {senha_entry.get()} e o site é {website_entry.get()}? ")
    if saida and (senha_entry.get() != "" or email_entry.get()!= "" or website_entry.get()!= ""):
        anotar = open("senhas.txt" , "a")
        texto = anotar_senha()
        anotar.write(f"\n {texto} \n")
        limpar_campos()
        anotar.close()
    else: 
        messagebox.askokcancel(title="Aviso", message="Por favor, preencha todas as caixas ou coloque padrões corretos")
    arquivo.close()
    
def limpar_campos():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    senha_entry.delete(0, END)
    
def anotar_senha():
    valor_email = email_entry.get()
    valor_senha = senha_entry.get()
    valor_web = website_entry.get()
    return f"website: {valor_web} | email: {valor_email} | senha: {valor_senha}"
        
        
        
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

senha_entry = Entry()
senha_entry.grid(row=3, column=1)

"""Button"""
botao_gerar_senha = Button(text="Gerar senha", command=gerar_senha)
botao_gerar_senha.grid(row=3, column=2)

botao_adicionar = Button(text="Adicionar", width=36, command=criar_arquivo_txt)
botao_adicionar.grid(row=4, column=1, columnspan=2)


window.mainloop()
