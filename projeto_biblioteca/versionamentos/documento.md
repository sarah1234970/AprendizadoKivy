# Sistema de Biblioteca Educacional

## Descrição
Este é um sistema simples de biblioteca educacional desenvolvido em Python usando o framework Kivy para interface gráfica e SQLite para armazenamento de dados. O sistema permite login, cadastro de usuários, empréstimo de livros (CRUD básico) e visualização do perfil do usuário.

## Versão Atual
**v1.0.0** - Versão inicial

## Funcionalidades
- Tela de login e cadastro de usuário
- Lista de livros disponíveis
- Funções de empréstimo e devolução de livros
- Visualização do perfil do usuário e seus empréstimos

## Estrutura do Banco de Dados
O sistema utiliza três tabelas principais:

1. **usuarios**: Armazena informações dos usuários
   - id (chave primária)
   - nome
   - email (único)
   - senha

2. **livros**: Armazena informações dos livros
   - id (chave primária)
   - titulo
   - autor
   - status (disponivel ou emprestado)

3. **emprestimos**: Armazena registros de empréstimos
   - id (chave primária)
   - usuario_id (chave estrangeira para usuarios)
   - livro_id (chave estrangeira para livros)
   - data_emprestimo
   - data_devolucao

## Requisitos
- Python 3.7 ou superior
- Kivy 2.1.0
- SQLite (incluído por padrão no Python)

## Instalação
1. Clone ou baixe o repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Execução
Para executar o sistema, rode o arquivo principal:
```
python main.py
```

## Estrutura do Projeto
- `main.py`: Arquivo principal da aplicação
- `database.py`: Módulo de gerenciamento do banco de dados SQLite
- `screens.py`: Módulo contendo as telas da aplicação
- `library.db`: Arquivo do banco de dados SQLite (gerado automaticamente)

## Desenvolvimento
Este projeto foi criado para fins educacionais, demonstrando:
- Uso do padrão MVC (Model-View-Controller)
- Manipulação de banco de dados com SQLite
- Interface gráfica com Kivy
- Gerenciamento de telas com ScreenManager

## Próximas Versões
O sistema será evoluído através das seguintes versões:
- v1.1.0: Corretiva - Correção de erros
- v1.2.0: Adaptativa - Ajustes na estrutura do banco de dados
- v1.3.0: Perfectiva - Melhorias na aparência e desempenho
- v1.4.0: Evolutiva - Adição de novos recursos

## Licença
Este projeto é destinado apenas para fins educacionais.
