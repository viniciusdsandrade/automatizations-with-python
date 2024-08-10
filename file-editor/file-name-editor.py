import os


def renomear_arquivos_consecutivos(diretorio):
    """
    Renomeia arquivos cujo nome termina com "(1)" antes da extensão,
    removendo o sufixo "(1)" do nome do arquivo.

    Args:
      diretorio: O caminho para o diretório onde os arquivos serão renomeados.
    """
    for filename in os.listdir(diretorio):
        # Divida o nome do arquivo em base e extensão
        base, ext = os.path.splitext(filename)
        # Verifique se a base do nome termina com "(1)"
        if base.endswith("(1)"):
            # Crie o novo nome do arquivo removendo "(1)"
            novo_nome_base = base[:-3]  # Remove "(1)"
            novo_nome = novo_nome_base + ext
            arquivo_completo_antigo = os.path.join(diretorio, filename)
            arquivo_completo_novo = os.path.join(diretorio, novo_nome)

            # Renomeie o arquivo
            os.rename(arquivo_completo_antigo, arquivo_completo_novo)
            print(f"Arquivo renomeado: {arquivo_completo_antigo} -> {arquivo_completo_novo}")


def main():
    diretorio = "C:\\Users\\vinic\\OneDrive\\Área de Trabalho\\to-remove"
    renomear_arquivos_consecutivos(diretorio)


if __name__ == "__main__":
    main()
