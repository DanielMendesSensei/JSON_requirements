import subprocess
import os
import json

def export_dependencies(output_file: str = "requirements.json"):
    """
    Exporta as dependências do ambiente atual para um arquivo JSON.

    :param output_file: Nome do arquivo JSON a ser gerado.
    """
    try:
        # Executa o comando pip freeze
        result = subprocess.run(["pip", "freeze"], capture_output=True, text=True, check=True)

        # Processa as dependências
        dependencies = {}
        for line in result.stdout.splitlines():
            if "==" in line:
                package, version = line.split("==")
                dependencies[package] = version

        # Salva em um arquivo JSON
        with open(output_file, "w") as f:
            json.dump(dependencies, f, indent=4)

        print(f"Dependências exportadas para {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o pip freeze: {e}")

def convert_json_to_txt(input_file: str = "requirements.json", output_file: str = "requirements.txt"):
    """
    Lê um arquivo JSON de dependências e converte para um arquivo requirements.txt.
    
    :param input_file: Nome do arquivo JSON a ser lido.
    :param output_file: Nome do arquivo requirements.txt a ser gerado.
    """
    try:
        # Carrega o arquivo JSON
        with open(input_file, "r") as f:
            dependencies = json.load(f)

        # Gera o arquivo requirements.txt
        with open(output_file, "w") as f:
            for package, version in dependencies.items():
                f.write(f"{package}=={version}\n")

        print(f"Arquivo {output_file} gerado com sucesso.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao processar o arquivo {input_file}: {e}")

def read_requirements(dependencies_file="requirements.json"):
    """
    Inicializa um novo projeto instalando dependências de um arquivo JSON.
    """
    if not os.path.exists(dependencies_file):
        print(f"Arquivo {dependencies_file} não encontrado.")
        return

    print(f"Lendo dependências de {dependencies_file}...")
    temp_requirements = "temp_requirements.txt"

    # Converte JSON para requirements.txt
    convert_json_to_txt(dependencies_file, temp_requirements)

    # Instala dependências do requirements.txt
    print(f"Instalando dependências listadas em {dependencies_file}...")
    os.system(f"pip install -r {temp_requirements}")

    # Remove o arquivo temporário
    os.remove(temp_requirements)
    print("Dependências lidas e instaladas com sucesso!")