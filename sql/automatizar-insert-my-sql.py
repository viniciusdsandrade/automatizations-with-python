import mysql.connector
import os

# Configurações de conexão com o banco de dados
config = {
    'user': 'root',  # Substitua com o seu usuário do MySQL
    'password': 'GhostSthong567890@',  # Substitua com a sua senha do MySQL
    'port': 3306,  # Substitua com a porta do MySQL (3306 é o padrão)
    'database': 'db_test_python_script',  # Substitua com o nome do seu banco de dados
}

# Caminhos para os scripts SQL
vini_path_desktop = r"C:\Users\Pichau\Desktop\automatizations-with-python\sql\db_test_python_script.sql"
vini_path_notebook = r"C:\Users\vinic\OneDrive\Área de Trabalho\automatizations-with-python\sql\db_test_python_script_seed.sql"


# Função para inicializar o banco de dados
def init_database():
    # Verifica se o arquivo de flag existe
    flag_file_path = "C:/Users/vinic/OneDrive/Área de Trabalho/automatizations-with-python/sql/.data_initialized"
    if not os.path.exists(flag_file_path):
        try:
            # Escolha o caminho correto do script SQL
            sql_script_path = vini_path_notebook
            with open(sql_script_path, 'r', encoding='utf-8') as file:
                sql_script = file.read()

            # Conecta ao banco de dados
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()

            # Divide o script SQL em comandos individuais e executa cada um
            sql_commands = sql_script.split(';')
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

            # Confirma as mudanças no banco de dados
            connection.commit()

            # Cria o arquivo de flag após a execução bem-sucedida
            with open(flag_file_path, 'w') as flag_file:
                flag_file.write("Banco de dados inicializado.")
            print("Arquivo de flag criado: banco de dados inicializado.")

        except Exception as e:
            print(f"Erro ao executar o script SQL: {e}")

        finally:
            cursor.close()
            connection.close()
    else:
        print("Banco de dados já inicializado. Pulando execução do script SQL.")


# Chama a função para inicializar o banco de dados
if __name__ == "__main__":
    init_database()
