from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.core.window import Window

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def bounce_paddle(self, paddle):
        if self.collide_widget(paddle):
            vx, vy = self.velocity
            offset = (self.center_y - paddle.center_y) / (paddle.height / 2)
            bounce_vx = -1 * vx
            bounce_vy = vy + offset
            # Mantém a aceleração da bola
            self.velocity = Vector(bounce_vx, bounce_vy) * 1.1


class PongPaddle(Widget):
    score = NumericProperty(0)

    def move_up(self, dt):
        # CORREÇÃO: Atribuição da nova posição
        self.y = self.y + 10 if self.top < self.parent.height else self.y

    def move_down(self, dt):
        self.y = self.y - 10 if self.y > 0 else self.y

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.bounce_paddle(self)


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    # speed_player1 e speed_player2 não são mais necessários se não houver AI
    # speed_player1 = NumericProperty(5)
    # speed_player2 = NumericProperty(5)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self._keyboard_closed, self)
        # CORREÇÃO: Usando self.keyboard (sem underscore)
        self.keyboard.bind(on_key_down=self._on_keyboard_down)
        self.keyboard.bind(on_key_up=self._on_keyboard_up)
        self.pressed_keys = set()

    def _keyboard_closed(self):
        # CORREÇÃO: Usando self.keyboard (sem underscore)
        self.keyboard.unbind(on_key_down=self._on_keyboard_down)
        self.keyboard.unbind(on_key_up=self._on_keyboard_up)
        self.keyboard = None

    # CORREÇÃO: Adicionando 'text' e 'modifiers' e corrigindo a lógica
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(keycode[1]) # Adiciona a tecla ao conjunto
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] in self.pressed_keys:
            self.pressed_keys.remove(keycode[1]) # Remove a tecla do conjunto
        return True

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        # Usando randint para um ângulo inicial aleatório
        self.ball.velocity = Vector(vel).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # Bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # Bounce off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Score points
        if self.ball.x < self.x:
            self.player2.score += 1
            # Serve a bola para a direita (player2 marcou)
            self.serve_ball(vel=(4, 0))
        # Usar elif aqui para que apenas uma condição de pontuação seja processada
        elif self.ball.x > self.width:
            self.player1.score += 1
            # Serve a bola para a esquerda (player1 marcou)
            self.serve_ball(vel=(-4, 0))

        # Movendo as raquetes baseado nas teclas pressionadas
        if 'w' in self.pressed_keys:
            self.player1.move_up(dt)
        if 's' in self.pressed_keys:
            self.player1.move_down(dt)
        if 'up' in self.pressed_keys:  # Tecla seta para cima
            self.player2.move_up(dt)
        if 'down' in self.pressed_keys: # Tecla seta para baixo
            self.player2.move_down(dt)

        # REMOVIDO: Blocos de movimento automático (AI) para evitar conflito com o teclado
        # if self.ball.center_y > self.player1.center_y:
        #     self.player1.center_y += self.speed_player1
        # elif self.ball.center_y < self.player1.center_y:
        #     self.player1.center_y -= self.speed_player1
        #
        # if self.ball.center_y > self.player2.center_y:
        #     self.player2.center_y += self.speed_player2
        # elif self.ball.center_y < self.player2.center_y:
        #     self.player2.center_y -= self.speed_player2

    def on_touch_move(self, touch):
        # Mantenha esta função se quiser que o toque ainda funcione
        # Ou comente/remova se quiser apenas controle de teclado
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 120.0)
        return game


if __name__ == '__main__':
    PongApp().run()