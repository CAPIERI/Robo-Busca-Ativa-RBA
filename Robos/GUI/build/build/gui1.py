from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Amarano\OneDrive\Familia\_Caio\Negocios\Sistemas\Robo-Busca-Ativa-RBA\Robos\GUI\build\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("809x512")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=512,
    width=809,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    34.0,
    98.0,
    anchor="nw",
    text="Por favor, preencha de acordo com sua unidade",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
)

diretoria_var = StringVar()
nome_escola_var = StringVar()
rua_escola_var = StringVar()
numero_escola_var = StringVar()
bairro_var = StringVar()
cidade_var = StringVar()
estado_var = StringVar()
cep_var = StringVar()
telefone_var = StringVar()
email_var = StringVar()

def criar_modelo_convocacao():
    if not all((diretoria_var.get(), nome_escola_var.get(), rua_escola_var.get(), numero_escola_var.get(),
                bairro_var.get(), cidade_var.get(), estado_var.get(), cep_var.get(), telefone_var.get(), email_var.get())):
        messagebox.showwarning("Aviso", "Por favor, preencha todas as entradas.")
        return

    # Atualiza as variáveis globais com os valores das entradas
    diretoria = diretoria_var.get()
    nome_escola = nome_escola_var.get()
    rua_escola = rua_escola_var.get()
    numero_escola = numero_escola_var.get()
    bairro = bairro_var.get()
    cidade = cidade_var.get()
    estado = estado_var.get()
    cep = cep_var.get()
    telefone = telefone_var.get()
    email = email_var.get()

    # Você pode fazer o que for necessário com essas variáveis (por exemplo, salvar em um arquivo)

    # Fecha a janela após a atualização
    window.destroy()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
botao_criar_modelo_convocacao = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=criar_modelo_convocacao,
    relief="flat"
)
botao_criar_modelo_convocacao.place(
    x=610.855224609375,
    y=426.71820068359375,
    width=165.144775390625,
    height=57.16119384765625
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    153.5,
    196.0,
    image=entry_image_1
)
textbox_diretoria = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=diretoria_var
)
textbox_diretoria.place(
    x=33.0,
    y=182.0,
    width=241.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    153.5,
    265.0,
    image=entry_image_2
)
textbox_nome_escola = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=nome_escola_var
)
textbox_nome_escola.place(
    x=33.0,
    y=251.0,
    width=241.0,
    height=26.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    153.5,
    334.0,
    image=entry_image_3
)
textbox_rua_escola = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=rua_escola_var
)
textbox_rua_escola.place(
    x=33.0,
    y=320.0,
    width=241.0,
    height=26.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    153.5,
    403.0,
    image=entry_image_4
)
textbox_numero_escola = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=numero_escola_var
)
textbox_numero_escola.place(
    x=33.0,
    y=389.0,
    width=241.0,
    height=26.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    153.5,
    472.0,
    image=entry_image_5
)
textbox_bairro = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=bairro_var
)
textbox_bairro.place(
    x=33.0,
    y=458.0,
    width=241.0,
    height=26.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    442.5,
    196.0,
    image=entry_image_6
)
textbox_cidade = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=cidade_var
)
textbox_cidade.place(
    x=322.0,
    y=182.0,
    width=241.0,
    height=26.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    442.5,
    265.0,
    image=entry_image_7
)
textbox_estado = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=estado_var
)
textbox_estado.place(
    x=322.0,
    y=251.0,
    width=241.0,
    height=26.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    442.5,
    334.0,
    image=entry_image_8
)
textbox_cep = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=cep_var
)
textbox_cep.place(
    x=322.0,
    y=320.0,
    width=241.0,
    height=26.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    442.5,
    403.0,
    image=entry_image_9
)
textbox_telefone = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=telefone_var
)
textbox_telefone.place(
    x=322.0,
    y=389.0,
    width=241.0,
    height=26.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    442.5,
    472.0,
    image=entry_image_10
)
textbox_email = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0,
    textvariable=email_var
)
textbox_email.place(
    x=322.0,
    y=458.0,
    width=241.0,
    height=26.0
)

window.resizable(False, False)
window.mainloop()
