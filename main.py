import os

def criar_estrutura_projeto():
    # Criar pastas
    os.makedirs('chat_gpt/app/modules')
    os.makedirs('chat_gpt/app/utils')
    os.makedirs('chat_gpt/tests')

    # Criar README.md
    with open('chat_gpt/README.md', 'w') as file:
        file.write("# Meu Projeto\n\nDescrição do projeto...")

    # Criar requirements.txt
    with open('chat_gpt/requirements.txt', 'w') as file:
        file.write("")

    # Criar setup.py
    with open('chat_gpt/setup.py', 'w') as file:
        file.write('''from setuptools import setup, find_packages

setup(
    name='chat_gpt_teste',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    # Add more information as needed
)
''')

if __name__ == "__main__":
    criar_estrutura_projeto()