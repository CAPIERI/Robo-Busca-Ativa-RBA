from pathlib import Path
from docxtpl import DocxTemplate
import pandas as pd
import subprocess
import datetime
import os
import subprocess

ano_atual = datetime.datetime.today()
# Carregue a planilha 'dados_filtrados_agregados'
dados = pd.read_excel('ArquivosGerados/dados_filtrados_com_RA_e_Nome_e_Série.xlsx')

#abre o modelo de convocação word
modelo = Path(__file__).parent / "BasesDeDados/CONVOCACAO_PARA_COMPENSAR_FALTAS.docx"
doc = DocxTemplate(modelo)

# Itere sobre os dados da planilha
for i, linha in dados.iterrows():
    nome = linha['Nome']
    numero = linha['RA']
    serie = linha['Série']

    context = {
        "ALUNO": f"{nome}",
        "NUMERO": f"{numero}",
        "SERIE": f"{serie}"
    }
doc.render(context)
doc.save(Path(__file__).parent / "teste.docx")