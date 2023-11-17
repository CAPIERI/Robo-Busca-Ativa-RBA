from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
def selecionar_diretorio_padrao():
    diretorio_selecionado = filedialog.askdirectory()
    print("Diretório selecionado:", diretorio_selecionado)

def selecionar_diretorio_saida():
    diretorio_selecionado_saida = filedialog.askdirectory()
    print("Diretório selecionado:", diretorio_selecionado_saida)

def janela_convocacao():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Amarano\OneDrive\Familia\_Caio\Negocios\Sistemas\Robo-Busca-Ativa-RBA\Robos\GUI\build\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("809x512")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 512,
        width = 809,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        16.0,
        12.0,
        anchor="nw",
        text="CONVOCAÇÃO",
        fill="#000000",
        font=("Inter Bold", 64 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_criar_modelo_convocacao = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=janela_convocacao,
        relief="flat"
    )
    button_criar_modelo_convocacao.place(
        x=16.0,
        y=130.0,
        width=334.680908203125,
        height=54.737518310546875
    )

    canvas.create_text(
        16.0,
        224.125,
        anchor="nw",
        text="Diretório onde estão os arquivos: ",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        16.0,
        291.2336730957031,
        anchor="nw",
        text="Diretório onde deseja guardar os arquivos criados: ",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=selecionar_diretorio_padrao,
        relief="flat"
    )
    button_2.place(
        x=297.75,
        y=218.0,
        width=205.79998779296875,
        height=30.625
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=selecionar_diretorio_saida,
        relief="flat"
    )
    button_3.place(
        x=425.1500244140625,
        y=285.375,
        width=205.79998779296875,
        height=30.625
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=38.0,
        y=413.0,
        width=199.0,
        height=68.87939453125
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=304.0,
        y=444.0,
        width=125.0,
        height=38.28515625
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=450.0,
        y=444.0,
        width=125.0,
        height=38.28515625
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=597.0,
        y=444.0,
        width=152.0,
        height=38.28515625
    )

    canvas.create_text(
        254.0,
        458.0,
        anchor="nw",
        text="Ou",
        fill="#363636",
        font=("Inter Bold", 20 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Amarano\OneDrive\Familia\_Caio\Negocios\Sistemas\Robo-Busca-Ativa-RBA\Robos\GUI\build\build\assets\frame1")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("809x512")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 512,
        width = 809,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        34.0,
        98.0,
        anchor="nw",
        text="Por favor, preencha de acordo com sua unidade",
        fill="#000000",
        font=("Inter Bold", 32 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=610.855224609375,
        y=426.71820068359375,
        width=165.144775390625,
        height=57.16119384765625
    )

    canvas.create_text(
        33.0,
        15.0,
        anchor="nw",
        text="MODELO DE CONVOCAÇÃO",
        fill="#000000",
        font=("Inter Bold", 54 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        153.5,
        196.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=33.0,
        y=182.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        34.0,
        155.0,
        anchor="nw",
        text="Diretoria:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        153.5,
        265.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=33.0,
        y=251.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        34.0,
        223.54168701171875,
        anchor="nw",
        text="Nome da escola:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        153.5,
        334.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=33.0,
        y=320.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        34.0,
        292.0833435058594,
        anchor="nw",
        text="Rua do endereço",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        153.5,
        403.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=33.0,
        y=389.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        34.0,
        360.625,
        anchor="nw",
        text="Número do Endereço",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        153.5,
        472.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=33.0,
        y=458.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        34.0,
        429.1666259765625,
        anchor="nw",
        text="Bairro:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        442.5,
        196.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=322.0,
        y=182.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        321.875,
        155.0,
        anchor="nw",
        text="Cidade:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        442.5,
        265.0,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=322.0,
        y=251.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        321.875,
        223.54168701171875,
        anchor="nw",
        text="Estado:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        442.5,
        334.0,
        image=entry_image_8
    )
    entry_8 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=322.0,
        y=320.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        321.875,
        292.0833435058594,
        anchor="nw",
        text="CEP:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        442.5,
        403.0,
        image=entry_image_9
    )
    entry_9 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=322.0,
        y=389.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        321.875,
        360.625,
        anchor="nw",
        text="Telefone institucional:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        442.5,
        472.0,
        image=entry_image_10
    )
    entry_10 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=322.0,
        y=458.0,
        width=241.0,
        height=26.0
    )

    canvas.create_text(
        321.875,
        429.1666259765625,
        anchor="nw",
        text="Email institucional:",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

janela_convocacao()