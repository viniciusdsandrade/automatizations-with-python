import os
from datetime import datetime


def resumir_conteudo_diretorios(dir_origem, dir_destino):
    # Verifica se o diretório de destino existe, se não, cria-o
    if not os.path.exists(dir_destino):
        os.makedirs(dir_destino)

    # Obtém o nome da primeira pasta (do diretório de origem)
    nome_primeira_pasta = os.path.basename(dir_origem)

    # Obtém a data atual no formato "dd-mm-aaaa"
    data_atual = datetime.now().strftime("%d-%m-%Y")

    # Cria o nome do arquivo de resumo conforme solicitado
    nome_arquivo = f'[diretorio]-{nome_primeira_pasta}-{data_atual}.txt'
    caminho_resumo = os.path.join(dir_destino, nome_arquivo)

    # Abre o arquivo de resumo no modo escrita
    with open(caminho_resumo, 'w') as arquivo_resumo:
        # Percorre todos os diretórios de origem
        for root, dirs, files in os.walk(dir_origem):
            # Extrai o nome do diretório atual
            nome_diretorio = os.path.basename(root)
            arquivo_resumo.write(f'Diretório: {nome_diretorio}\n')

            # Se houver subdiretórios, lista seus nomes
            for subdir in dirs:
                arquivo_resumo.write(f'    Pasta: {subdir}\n')

            # Lista os arquivos no diretório atual
            for file in files:
                arquivo_resumo.write(f'    Arquivo: {file}\n')

            arquivo_resumo.write('\n')

    print(f"Resumo criado com sucesso em: {caminho_resumo}")


def main():
    dir_origem = 'C:\\Users\\vinic\\OneDrive\\Área de Trabalho\\RD'
    dir_destino = 'C:\\Users\\vinic\\OneDrive\\Área de Trabalho\\Resumo'

    resumir_conteudo_diretorios(dir_origem, dir_destino)


if __name__ == '__main__':
    main()
