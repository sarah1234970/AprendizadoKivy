# multi_telas_app/multi_telas_app/README.md

# Multi Telas App

## Descrição

O Multi Telas App é um aplicativo Kivy que permite aos usuários inserir seu nome e receber sugestões de filmes com base em gêneros selecionados. O aplicativo possui uma interface de múltiplas telas, onde os usuários podem navegar facilmente entre a tela de boas-vindas e a tela de sugestão de filmes.

## Estrutura do Projeto

```
multi_telas_app
├── screens
│   ├── boas_vindas.py         # Tela de boas-vindas
│   ├── sugestao_filmes.py     # Tela de sugestão de filmes
│   └── __init__.py            # Inicializa o pacote de telas
├── main.py                     # Ponto de entrada do aplicativo
├── assets
│   └── images                 # Imagens utilizadas no aplicativo
├── kivy_files
│   ├── boas_vindas.kv         # Layout da tela de boas-vindas
│   ├── sugestao_filmes.kv     # Layout da tela de sugestão de filmes
│   └── main.kv                # Layout principal do aplicativo
└── README.md                   # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   ```
2. Navegue até o diretório do projeto:
   ```
   cd multi_telas_app
   ```
3. Instale as dependências necessárias:
   ```
   pip install kivy
   ```

## Uso

Para executar o aplicativo, utilize o seguinte comando:

```
python main.py
```

## Funcionalidades

- Tela de Boas-Vindas: O usuário pode inserir seu nome e clicar em "Continuar" para ir para a tela de sugestão de filmes.
- Tela de Sugestão de Filmes: O aplicativo exibe uma mensagem de boas-vindas com o nome do usuário, permite selecionar um gênero de filme e sugere um filme aleatório da lista correspondente.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.