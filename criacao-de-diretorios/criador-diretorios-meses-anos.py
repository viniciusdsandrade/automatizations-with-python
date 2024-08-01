import os
import calendar


def criar_diretorios_meses_anos(caminho_base, ano):
    # Verifica se o diretório base existe, se não, cria-o
    if not os.path.exists(caminho_base):
        os.makedirs(caminho_base)

    # Cria as pastas para cada mês com a máscara especificada
    for mes in range(1, 13):
        nome_mes = calendar.month_name[mes].lower()
        nome_pasta = f"[{ano}]-{mes:02d}-{nome_mes}"
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
    ano = 2022

    criar_diretorios_meses_anos(caminho_base, ano)


if __name__ == "__main__":
    main()
