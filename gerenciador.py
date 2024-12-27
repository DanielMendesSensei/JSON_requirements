from JSON_requirements import export_dependencies, convert_json_to_txt, read_requirements

# Exporta dependências instaladas para um arquivo JSON
# export_dependencies("requirements.json")

# Lê dependências de um JSON e cria um arquivo requirements.txt
#convert_json_to_txt("requirements.json", "requirements.txt")

# Lê dependências JSON e instala no ambiente do projeto
read_requirements("requirements.json")