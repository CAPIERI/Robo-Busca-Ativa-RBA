from docxtpl import DocxTemplate
from pathlib import Path
import datetime

ano_atual = datetime.datetime.today()

# Obtém o diretório do script
script_path = Path(__file__).resolve().parent

# Obtém o caminho absoluto para o arquivo
document_path = script_path.parent / "BasesDeDados" / "CONVOCACAO_PARA_COMPENSAR_FALTAS.docx"

# Imprime o caminho para verificar se está correto
print(f"Caminho do arquivo: {document_path}")

# Agora você pode usar document_path para abrir o arquivo

novo_modelo = DocxTemplate(document_path)

context = {
    "REGIAO": "jojo",
    "DEPARTAMENTO": "okpk",
    "RUA": "okpkp",
    "NUMERO": "klplp",
    "JARDIM": "",
    "CIDADE": "",
    "ESTADO": "",
    "CEP": "",
    "TELEFONE": "",
    "EMAIL": ""
    # "ANO": ano_atual.strftime("%Y")
}
novo_modelo.render(context)
novo_modelo.save("Convocacao.docx")