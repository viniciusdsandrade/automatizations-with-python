import os


def criar_pastas(caminho_base, numero_inicial, numero_final):
    # Verifica se o diretório base existe, se não, cria-o
    if not os.path.exists(caminho_base):
        os.makedirs(caminho_base)

    # Cria as pastas dentro do intervalo especificado
    for i in range(numero_inicial, numero_final + 1):
        nome_pasta = f"[{i}]"
        caminho_completo = os.path.join(caminho_base, nome_pasta)

        try:
            os.makedirs(caminho_completo)
            print(f"Pasta '{nome_pasta}' criada com sucesso!")
        except FileExistsError:
            print(f"Pasta '{nome_pasta}' já existe.")
        except Exception as e:
            print(f"Erro ao criar a pasta '{nome_pasta}': {e}")


def main():
    caminho_base = "C:\\Users\\vinic\\OneDrive\\Área de Trabalho\\RD"
    inicio = 1
    fim = 200

    criar_pastas(caminho_base, inicio, fim)


if __name__ == "__main__":
    main()
