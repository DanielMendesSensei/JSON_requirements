from setuptools import setup, find_packages
from pathlib import Path

long_description = Path("README.md").read_text()

setup(
    name="JSON_requirements",
    version="1.0.2",
    description="Uma biblioteca para gerenciar dependências python em formato JSON",
    author="Daniel Mendes",
    author_email="senseidanielmendes@gmail.com",
    url="https://github.com/DanielMendesSensei/JSON_requirements",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
