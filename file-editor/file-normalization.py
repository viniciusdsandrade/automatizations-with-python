import os
import unicodedata
import re
import tkinter as tk
from tkinter import filedialog, messagebox


def remover_acentos(texto):
    """
    Remove acentos e caracteres especiais de uma string.
    """
    nfkd = unicodedata.normalize('NFKD', texto)
    apenas_caracteres = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return apenas_caracteres


def normalizar_nome(nome):
    """
    Normaliza o nome do arquivo:
    - Converte para minúsculas
    - Remove acentos
    - Substitui espaços e caracteres não permitidos por hífens
    """
    nome_sem_ext, extensao = os.path.splitext(nome)

    # Remove acentos
    nome_sem_ext = remover_acentos(nome_sem_ext)

    # Converte para minúsculas
    nome_sem_ext = nome_sem_ext.lower()

    # Substitui espaços e caracteres não permitidos por hífens
    nome_sem_ext = re.sub(r'[^a-z0-9]+', '-', nome_sem_ext)

    # Remove hífens extras no início e fim
    nome_sem_ext = nome_sem_ext.strip('-')

    # Reconstroi o nome com a extensão original em minúsculas
    nome_normalizado = f"{nome_sem_ext}{extensao.lower()}"

    return nome_normalizado


def selecionar_arquivo():
    """
    Abre uma janela para seleção de arquivo e retorna o caminho do arquivo selecionado.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo para normalizar",
        filetypes=[
            ("Arquivos TXT", "*.txt"),
            ("Arquivos PDF", "*.pdf"),
            ("Arquivos Word", "*.docx"),
            ("Imagens", "*.jpeg *.jpg *.png *.gif *.bmp *.tiff"),
            ("Vídeos", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv *.webm")
        ]
    )
    return arquivo


def renomear_arquivo(caminho):
    """
    Renomeia o arquivo no caminho especificado.
    """
    diretorio, nome = os.path.split(caminho)
    novo_nome = normalizar_nome(nome)
    novo_caminho = os.path.join(diretorio, novo_nome)

    if novo_nome == nome:
        messagebox.showinfo("Informação", "O nome do arquivo já está normalizado.")
        return

    if os.path.exists(novo_caminho):
        messagebox.showerror("Erro", f"Não foi possível renomear.\nJá existe um arquivo chamado '{novo_nome}'.")
        return

    try:
        os.rename(caminho, novo_caminho)
        messagebox.showinfo("Sucesso", f"Arquivo renomeado para '{novo_nome}'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao renomear o arquivo:\n{e}")


def main():
    arquivo = selecionar_arquivo()
    if arquivo:
        renomear_arquivo(arquivo)
    else:
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")


if __name__ == "__main__":
    main()
