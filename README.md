<img src="/public/img/Logo.png" alt="Exemplo de imagem" width="500">

## ❇️Last Update

Versão 1.0.0 -> build: Release!

## 🧾Descrição

**JSON_requirements** é uma biblioteca Python que simplifica o gerenciamento de dependências em projetos. Com ela, você pode exportar as dependências instaladas no ambiente para um arquivo JSON e converter arquivos JSON de dependências para o formato `requirements.txt`, usado pelo `pip`.

## ✨Recursos Principais

- **Exportar dependências**: Gera um arquivo JSON com todas as dependências instaladas no ambiente atual.
- **Converter Formato**: Converte um arquivo JSON de dependências para um arquivo `requirements.txt`.
- **Inicializar Projetos**: Lê dependências de um arquivo JSON e as instala automaticamente.

## 📥Instalação

Para instalar a biblioteca localmente:

```bash
pip install .
```

Você também pode instalá-la com:

```bash
pip install json-requirements
```

## 💻Uso

### 📤Exportar Dependências para JSON

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

### 🔄Converter JSON para `requirements.txt`

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

### ✅Inicializar Projetos

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

## 🧪Testes

A biblioteca inclui testes para validar suas funcionalidades. Para rodar os testes:

1. Execute os testes:

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

## 🙌Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção de bug:

   ```bash
   git checkout -b minha-nova-feature
   ```

3. Faça suas alterações e envie um pull request.

## 📜Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
