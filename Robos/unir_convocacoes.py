from docxcompose.composer import Composer
from docx import Document
from pathlib import Path
import os

diretorio_arquivos = Path(__file__).parent.parent / 'ArquivosGerados/Documentos Individuais'
todos_arquivos = os.listdir(diretorio_arquivos)
arquivos = [arquivo for arquivo in todos_arquivos if arquivo.endswith('.docx')]

