from docxtpl import DocxTemplate
from pathlib import Path
import datetime

ano_atual = datetime.datetime.today()

# INTERFACE GRÀFICA
##----

def substituir_documento():
    # Obtém o diretório do script
    script_path = Path(__file__).resolve().parent
    # Obtém o caminho absoluto para o arquivo
    document_path_base_dados = script_path.parent / "BasesDeDados" / "CONVOCACAO_PARA_COMPENSAR_FALTAS.docx"

    doc = DocxTemplate(document_path_base_dados)
    # Dicionário de padrões a serem substituídos
    padroes = {
        'DIRETORIA': '',
        'NOME DA ESCOLA': '',
        'RUA': '',
        'NÚMERO DO ENDEREÇO': '',
        'BAIRRO': '',
        'CIDADE': '',
        'ESTADO': '',
        'CEP': '',
        'TELEFONE': '',
        'EMAIL': '',
        'ANO': ano_atual.strftime("%Y"),
        "ALUNO": "{{ALUNO}}",
        "RA": "{{RA}}",
        "SERIE": "{{SERIE}}"
    }

    doc.render(padroes)

    # Salve o novo documento Word
    document_path_arquivos_gerados = script_path.parent / "ArquivosGerados" / "modelo_convocacao.docx"
    doc.save(Path(__file__).parent / document_path_arquivos_gerados)

    print(f'Documento gerado e salvo em {document_path_arquivos_gerados}')

substituir_documento()