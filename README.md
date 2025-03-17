<img src="/public/img/Logo.png" alt="Exemplo de imagem" width="500">

# 📖 README / Leia-me

## ❇️ Last Update / Última Atualização

Version 1.0.3 -> fix: Library Name

## 🧾 Description / Descrição

**English:**  
**JSON_requirements** is a Python library that simplifies dependency management in projects. It allows you to export installed dependencies into a JSON file and convert JSON dependency files into the `requirements.txt` format used by `pip`.

**Português:**  
**JSON_requirements** é uma biblioteca Python que simplifica o gerenciamento de dependências em projetos. Com ela, você pode exportar as dependências instaladas no ambiente para um arquivo JSON e converter arquivos JSON de dependências para o formato `requirements.txt`, usado pelo `pip`.

## ✨ Main Features / Recursos Principais

**English:**

- **Export Dependencies:** Generates a JSON file with all dependencies installed in the current environment.
- **Format Conversion:** Converts a JSON dependency file to a `requirements.txt` file.
- **Initialize Projects:** Reads dependencies from a JSON file and installs them automatically.

**Português:**

- **Exportar Dependências:** Gera um arquivo JSON com todas as dependências instaladas no ambiente atual.
- **Converter Formato:** Converte um arquivo JSON de dependências para um arquivo `requirements.txt`.
- **Inicializar Projetos:** Lê dependências de um arquivo JSON e as instala automaticamente.

## 📥 Installation / Instalação

**English:**  
To install the library locally:

```bash
pip install .
```

Or install it with:

```bash
pip install json-requirements
```

**Português:**
Para instalar a biblioteca localmente:

```bash
pip install .
```

Você também pode instalá-la com:

```bash
pip install json-requirements
```

## 💻 Usage / Uso

### 📤 Export Dependencies to JSON / Exportar Dependências para JSON

**English:**
Export the installed dependencies in the current environment to a JSON file:

```python
from json_requirements import export_dependencies

# Export dependencies to a file named requirements.json
export_dependencies("requirements.json")
```

This will generate a `requirements.json` file in the following format:

```json
{
  "flask": "2.2.3",
  "requests": "2.28.1",
  "numpy": "1.24.1"
}
```

**Português:**
Para exportar as dependências instaladas no ambiente atual para um arquivo JSON:

```python
from json_requirements import export_dependencies

# Exporta dependências para um arquivo chamado requirements.json
export_dependencies("requirements.json")
```

Isso gerará um arquivo `requirements.json` com o seguinte formato:

```json
{
  "flask": "2.2.3",
  "requests": "2.28.1",
  "numpy": "1.24.1"
}
```

### 🔄 Convert JSON to requirements.txt / Converter JSON para `requirements.txt`

**English:**
Convert a JSON file to the `requirements.txt`format:

```python
from json_requirements import convert_json_to_txt

# Convert requirements.json to requirements.txt
convert_json_to_txt("requirements.json", "requirements.txt")
```

This will create a `requirements.txt` file with the following content:

```
flask==2.2.3
requests==2.28.1
numpy==1.24.1
```

**Português:**
Para converter um arquivo JSON para o formato `requirements.txt`:

```python
from json_requirements import convert_json_to_txt

# Converte requirements.json para requirements.txt
convert_json_to_txt("requirements.json", "requirements.txt")
```

Isso criará um arquivo `requirements.txt` com o seguinte conteúdo:

```
flask==2.2.3
requests==2.28.1
numpy==1.24.1
```

### ✅ Initialize Projects / Inicializar Projetos

**English:**
Use the `read_requirements` function to automatically initialize projects from a JSON file:

```python
from json_requirements import read_requirements

# Initialize the project by reading dependencies from requirements.json
read_requirements("requirements.json")
```

This function performs the following steps:

1. Checks if the JSON file exists.
2. Converts the JSON file into a r`requirements.txt` file.
3. Installs the dependencies listed in `requirements.txt` using `pip`.

Example command:

```bash
python -c "from json_requirements import read_requirements; read_requirements('requirements.json')"
```

**Português:**

Você pode usar a função `read_requirements` para inicializar projetos automaticamente a partir de um arquivo JSON:

```python
from json_requirements import read_requirements

# Inicializa o projeto lendo as dependências de requirements.json
read_requirements("requirements.json")
```

Essa função executa os seguintes passos:

1. Verifica se o arquivo JSON existe.
2. Converte o arquivo JSON em um arquivo `requirements.txt`.
3. Instala as dependências listadas no `requirements.txt` usando `pip`.

Exemplo de uso:

```bash
python -c "from json_requirements import read_requirements; read_requirements('requirements.json')"
```

## 🧪 Tests / Testes

**English:**
The library includes tests to validate its features. To run the tests:

```bash
   python -m unittest discover -s tests
```

Expected output example:

```
..
----------------------------------------------------------------------
Ran 3 tests in 0.178s

OK
```

**Português:**

A biblioteca inclui testes para validar suas funcionalidades. Para rodar os testes:

```bash
python -m unittest discover -s tests
```

Exemplo de saída esperada:

```
..
----------------------------------------------------------------------
Ran 3 tests in 0.178s

OK
```

## 🙌 Contribution / Contribuição

**English:**
Contributions are welcome! To contribute:

1 .Fork this repository.

2. Create a branch for your feature or bug fix:

   ```bash
   git checkout -b minha-nova-feature
   ```

3. Make your changes and submit a pull request.

**Português:**
Contribuições são bem-vindas! Para contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção de bug:

   ```bash
   git checkout -b minha-nova-feature
   ```

3. Faça suas alterações e envie um pull request.

## 📜 License / Licença

**English:**
This project is licensed under the [MIT License](LICENSE).

**Português:**
Este projeto está licenciado sob a [Licença MIT](LICENSE).
