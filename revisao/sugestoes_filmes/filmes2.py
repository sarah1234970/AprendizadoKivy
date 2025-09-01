# Importação dos módulos do Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
import random  # Para sortear filmes aleatoriamente


class FilmesApp(App):
    def build(self):
        # Layout principal vertical, com espaçamento e padding
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Campo de entrada de nome do usuário
        self.nome_input = TextInput(
            hint_text="Digite seu nome",  # Texto de dica
            multiline=False,               # Não permite múltiplas linhas
            size_hint=(1, 0.1)             # Ocupar toda a largura e altura proporcional 0.1
        )

        # Variável para armazenar o gênero selecionado
        self.genero_escolhido = None

        # Layout horizontal para os botões de gênero
        botoes_genero = BoxLayout(size_hint=(1, 0.15), spacing=10)
        for genero in ["Ação", "Comédia", "Terror", "Drama", "Animação"]:
            # Cada ToggleButton representa um gênero
            botao = ToggleButton(
                text=genero,
                group="genero"  # Apenas um botão do grupo pode estar ativo
            )
            # Conecta o clique do botão à função que salva o gênero selecionado
            botao.bind(on_press=self.selecionar_genero)
            botoes_genero.add_widget(botao)

        # Layout horizontal para os botões principais: Sugerir Filme e Limpar
        botoes = BoxLayout(size_hint=(1, 0.15), spacing=10)

        # Botão "Sugerir Filme"
        botao_sugerir = Button(
            text="🎬 Sugerir Filme",
            background_color=(0.2, 0.6, 0.8, 1)  # Azul claro
        )
        botao_sugerir.bind(on_press=self.sugerir_filme)  # Conecta a função de sugestão

        # Botão "Limpar"
        botao_limpar = Button(
            text="🧹 Limpar",
            background_color=(0.8, 0.3, 0.3, 1)  # Vermelho
        )
        botao_limpar.bind(on_press=self.limpar)  # Conecta a função de limpar

        # Adiciona os botões ao layout horizontal
        botoes.add_widget(botao_sugerir)
        botoes.add_widget(botao_limpar)

        # Label para exibir mensagens ao usuário
        self.mensagem_label = Label(
            text="[b]Digite seu nome e escolha um gênero[/b]",  # Texto inicial
            markup=True,                                      # Permite negrito, itálico e cores
            size_hint=(1, 0.2),                               # Ocupa largura total e altura proporcional 0.2
            halign="center",                                  # Alinha horizontalmente ao centro
            valign="middle"                                   # Alinha verticalmente ao meio
        )
        # Faz o texto se ajustar ao tamanho do Label
        self.mensagem_label.bind(size=self.mensagem_label.setter("text_size"))

        # Adiciona os widgets ao layout principal
        layout.add_widget(self.nome_input)
        layout.add_widget(botoes_genero)
        layout.add_widget(botoes)
        layout.add_widget(self.mensagem_label)

        return layout

    # Função chamada quando um ToggleButton de gênero é clicado
    def selecionar_genero(self, instance):
        self.genero_escolhido = instance.text  # Salva o gênero selecionado

    # Função chamada quando o botão "Sugerir Filme" é clicado
    def sugerir_filme(self, instance):
        # Dicionário com filmes por gênero, incluindo ano
        filmes = {
            "Comédia": ["As Branquelas (2004)", "Todo Mundo em Pânico (2000)", "Garotas Malvadas (2004)"],
            "Terror": ["Invocação do Mal (2013)", "It: A Coisa (2017)", "A Hora do Pesadelo (1984)"],
            "Ação": ["Velozes e Furiosos (2001)", "Missão Impossível (1996)", "Vingadores: Ultimato (2019)"],
            "Drama": ["À Procura da Felicidade (2006)", "Clube da Luta (1999)", "O Menino do Pijama Listrado (2008)"],
            "Animação": ["Procurando Nemo (2003)", "Divertida Mente (2015)", "Shrek (2001)"]
        }

        nome = self.nome_input.text.strip()  # Remove espaços em branco do nome
        genero = self.genero_escolhido       # Obtém o gênero selecionado

        # Validações
        if not nome:
            # Usuário não digitou nome
            self.mensagem_label.text = "[color=ff0000]Por favor, digite seu nome.[/color]"
        elif not genero:
            # Usuário não selecionou gênero
            self.mensagem_label.text = "[color=ff0000]Por favor, escolha um gênero.[/color]"
        else:
            # Sorteia um filme aleatoriamente do gênero escolhido
            filme = random.choice(filmes[genero])
            # Exibe a mensagem final com nome, gênero e filme
            self.mensagem_label.text = f"Olá, [b]{nome}[/b]! Sua sugestão de filme de [b]{genero}[/b] é: [i]{filme}[/i]."

    # Função chamada quando o botão "Limpar" é clicado
    def limpar(self, instance):
        self.nome_input.text = ""           # Limpa o campo de nome
        self.genero_escolhido = None        # Reseta o gênero selecionado
        self.mensagem_label.text = "[b]Digite seu nome e escolha um gênero[/b]"  # Mensagem inicial


# Executa o app
if __name__ == "__main__":
    FilmesApp().run()
