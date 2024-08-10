import os


def limpar_arquivos_consecutivos(diretorio):
    """
    Remove arquivos cujo nome termina com "(1)" antes da extensão de um diretório,
    independente da extensão do arquivo.

    Args:
      diretorio: O caminho para o diretório a ser limpo.
    """
    for filename in os.listdir(diretorio):
        # Divida o nome do arquivo em base e extensão
        base, ext = os.path.splitext(filename)
        # Verifique se a base do nome termina com "(1)"
        if base.endswith("(1)"):
            arquivo_completo = os.path.join(diretorio, filename)
            os.remove(arquivo_completo)
            print(f"Arquivo removido: {arquivo_completo}")


def main():
    diretorio = "C:\\Users\\vinic\\OneDrive\\Área de Trabalho\\to-remove"
    limpar_arquivos_consecutivos(diretorio)


if __name__ == "__main__":
    main()
