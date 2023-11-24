import customtkinter as ctk
from docxtpl import DocxTemplate
from pathlib import Path
import datetime
import os

import subprocess

def executar():
    # Obter o diretório do arquivo em execução
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Nome do arquivo a ser executado (neste caso, na mesma pasta)
    caminho_segundo_script = "execute.py"

    # Caminho completo para o segundo script
    caminho_completo = os.path.join(diretorio_atual, caminho_segundo_script)

    # Executar o segundo script
    subprocess.call(["python", caminho_completo])

def criar_modelo_convocacao():
    ano_atual = datetime.datetime.today()

    # INTERFACE GRÀFICA
    ##----

def janela_Modelo_Conv():
    def salvar_informacoes():
        global rua, numero_endereco, bairro, cidade, estado, cep, telefone, email, departamento, regiao_escola
        regiao_escola = entry_regiao_escola.get()
        departamento = entry_departamento_escola.get()
        rua = entry_rua.get()
        numero_endereco = entry_numero_endereco.get()
        bairro = entry_bairro.get()
        cidade = entry_cidade.get()
        estado = entry_estado.get()
        cep = entry_cep.get()
        telefone = entry_telefone.get()
        email = entry_email.get()

        janela_modelo_convocacao.destroy()

    janela_modelo_convocacao = ctk.CTkToplevel()
    janela_modelo_convocacao.geometry("800x500")
    janela_modelo_convocacao.title("Modelo Convocação")

    label_modelo_convocacao = ctk.CTkLabel(janela_modelo_convocacao, text="Por Favor preencha as informações da sua Escola:")
    label_modelo_convocacao.pack()

    entry_regiao_escola = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Região da Escola")
    entry_regiao_escola.pack()

    entry_departamento_escola = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Departamento da Escola")
    entry_departamento_escola.pack()

    entry_rua = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Rua")
    entry_rua.pack()

    entry_numero_endereco = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Número do Endereço")
    entry_numero_endereco.pack()

    entry_bairro = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Bairro")
    entry_bairro.pack()

    entry_cidade = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Cidade")
    entry_cidade.pack()

    entry_estado = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Estado")
    entry_estado.pack()

    entry_cep = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="CEP")
    entry_cep.pack()

    entry_telefone = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Telefone")
    entry_telefone.pack()

    entry_email = ctk.CTkEntry(janela_modelo_convocacao, placeholder_text="Email")
    entry_email.pack()

    botao_salvar = ctk.CTkButton(janela_modelo_convocacao, text="Salvar", command=salvar_informacoes)
    botao_salvar.pack()

janela_princ = ctk.CTk()
janela_princ.geometry("800x500")
janela_princ.minsize(width=800, height=500)
janela_princ.maxsize(width=800, height=500)
janela_princ.title("Busca Ativa")

label_busca_ativa = ctk.CTkLabel(janela_princ, width=40, height=40, text="Busca Ativa")
label_busca_ativa.pack()

botao_modelo_conv = ctk.CTkButton(janela_princ, text="Editar Modelo De Convocação", command=janela_Modelo_Conv)
botao_modelo_conv.pack()

botao_rodar_robo = ctk.CTkButton(janela_princ, text="Rodar", command=executar)
botao_rodar_robo.pack()

janela_princ.mainloop()
