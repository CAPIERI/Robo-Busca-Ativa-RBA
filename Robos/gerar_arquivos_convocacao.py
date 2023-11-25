import pandas as pd
from pathlib import Path
from docxtpl import DocxTemplate
import os

# Carregue a planilha 'alunos_para_convocacao'
dados = pd.read_excel('ArquivosGerados/alunos_para_convocacao.xlsx')

script_dir = Path(__file__).resolve().parent 

dir_modelo_convocacao = script_dir.parent / "ArquivosGerados" / "modelo_convocacao.docx"

doc = DocxTemplate(dir_modelo_convocacao)
alunos = []

# Crie uma pasta para armazenar os documentos individuais dos alunos
pasta_convocacoes_indiv = script_dir.parent / "ArquivosGerados" / "Documentos Individuais"
pasta_convocacoes_indiv.mkdir(exist_ok=True)  # Cria a pasta se ainda não existir

for _,linha in dados.iterrows():
    nome = linha['Nome']
    numero = linha['RA']
    serie = linha["Série"]

    aluno = {
        'ALUNO': nome.upper(),
        'RA': numero.upper(),
        'SERIE': serie.upper()
    }

    # Selecionar uma chave específica do dicionário (por exemplo, 'ALUNO') para compor o nome do arquivo
    nome_arquivo = f"documento_convocacao_{aluno['ALUNO']}.docx"
    
    # Renderizar e salvar o documento com o nome do aluno na pasta específica
    doc.render(aluno)
    caminho_arquivo = pasta_convocacoes_indiv / nome_arquivo
    doc.save(caminho_arquivo)

    alunos.append(aluno)
