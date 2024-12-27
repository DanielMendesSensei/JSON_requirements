import unittest
import os
import json
from unittest.mock import patch
from JSON_requirements.manager import export_dependencies, convert_json_to_txt, read_requirements

class TestDependencyManager(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente para os testes, criando arquivos temporários.
        """
        self.test_export_file = "test_requirements.json"
        self.test_import_file = "test_requirements.txt"
        self.sample_dependencies = {
            "flask": "2.2.3",
            "requests": "2.28.1",
            "numpy": "1.24.1"
        }

        # Cria um arquivo JSON de exemplo para importação
        with open(self.test_export_file, "w") as f:
            json.dump(self.sample_dependencies, f, indent=4)

    def tearDown(self):
        """
        Remove os arquivos temporários criados durante os testes.
        """
        for file in [self.test_export_file, self.test_import_file]:
            if os.path.exists(file):
                os.remove(file)

    @patch('subprocess.run')  # Mock do subprocess.run
    def test_export_dependencies(self, mock_run):
        """
        Testa se as dependências são exportadas corretamente para um arquivo JSON.
        """
        # Simula a saída do comando pip freeze
        mock_freeze_output = "flask==2.2.3\nrequests==2.28.1\nnumpy==1.24.1"
        mock_run.return_value.stdout = mock_freeze_output
        
        # Chama a função que deve usar subprocess.run
        export_dependencies(self.test_export_file)

        # Verifica se o arquivo JSON foi criado
        self.assertTrue(os.path.exists(self.test_export_file), "O arquivo JSON não foi criado.")

        with open(self.test_export_file, "r") as f:
            dependencies = json.load(f)
        
        # Verifica se o conteúdo do arquivo é um dicionário
        self.assertIsInstance(dependencies, dict, "As dependências exportadas não são um dicionário.")
        self.assertGreater(len(dependencies), 0, "Nenhuma dependência foi exportada.")
        self.assertEqual(dependencies, self.sample_dependencies, "As dependências exportadas não estão corretas.")

    @patch('subprocess.run')  # Mock do subprocess.run
    def test_convert_json_to_txt(self, mock_run):
        """
        Testa se um arquivo JSON de dependências é convertido corretamente para um requirements.txt.
        """
        # Simula a saída do comando pip freeze
        mock_freeze_output = "flask==2.2.3\nrequests==2.28.1\nnumpy==1.24.1"
        mock_run.return_value.stdout = mock_freeze_output
        
        # Chama a função para converter o JSON para txt
        convert_json_to_txt(self.test_export_file, self.test_import_file)

        # Verifica se o arquivo requirements.txt foi criado
        self.assertTrue(os.path.exists(self.test_import_file), "O arquivo requirements.txt não foi criado.")

        with open(self.test_import_file, "r") as f:
            lines = f.readlines()
        
        # Verifica se o número de linhas corresponde ao número de dependências
        self.assertEqual(len(lines), len(self.sample_dependencies), "Número de dependências no arquivo não corresponde.")
        for line in lines:
            package, version = line.strip().split("==")
            self.assertEqual(self.sample_dependencies[package], version, f"Versão de {package} não corresponde.")

    @patch('subprocess.run')  # Mock do subprocess.run
    def test_read_requirements(self, mock_run):
        """
        Testa a leitura de um arquivo requirements.json e inicializa o projeto com base no requirements.json.
        """
        # Simula a saída do comando pip freeze
        mock_freeze_output = "flask==2.2.3\nrequests==2.28.1\nnumpy==1.24.1"
        mock_run.return_value.stdout = mock_freeze_output
        
        # Chama a função que deve ler o arquivo requirements.json
        read_requirements(self.test_export_file)

        # Verifica se o arquivo requirements.json foi lido corretamente
        self.assertTrue(os.path.exists(self.test_export_file), "O arquivo requirements.json não existe.")
        
        # Abre o arquivo requirements.json e verifica se as dependências são as esperadas
        with open(self.test_export_file, 'r') as f:
            try:
                data = json.load(f)  # Tenta carregar o conteúdo do arquivo JSON
                # Verifica se o conteúdo corresponde ao esperado
                self.assertEqual(data, self.sample_dependencies, "O arquivo requirements.json não contém as dependências corretas.")
            except json.JSONDecodeError:
                self.fail("O arquivo requirements.json não está em formato JSON válido.")

if __name__ == "__main__":
    unittest.main()
