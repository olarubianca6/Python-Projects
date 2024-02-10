import pygame

pygame.init()

font = pygame.font.Font('Grand9K Pixel.ttf', 20)

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

Width = 900
Height = 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ping-Pong")

clock = pygame.time.Clock()
FPS = 30


def display_score(text, score, x, y, color):
    text = font.render(text+str(score), True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)

    screen.blit(text, text_rect)
    return


class Player:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.obj_rect = pygame.Rect(posx, posy, width, height)
        self.obj = pygame.draw.rect(screen, self.color, self.obj_rect)

    def display(self):
        self.obj = pygame.draw.rect(screen, self.color, self.obj_rect)

    def update(self, ydir):
        self.posy = self.posy + self.speed*ydir

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= Height:
            self.posy = Height-self.height

        self.obj_rect = (self.posx, self.posy, self.width, self.height)

    def get_rect(self):
        return self.obj_rect


class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color,
                                       (self.posx, self.posy),
                                       self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = self.ball = pygame.draw.circle(screen, self.color,
                                       (self.posx, self.posy),
                                       self.radius)

    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac

        if self.posy <= 0 or self.posy >= Height:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= Width and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = Width//2
        self.posy = Height//2
        self.xFac *= -1
        self.firstTime = 1

    def hit(self):
        self.xFac *= -1

    def get_rect(self):
        return self.ball


def main():
    running = True

    player1 = Player(20, 0, 10, 100, 10, green)
    player2 = Player(Width-30, 0, 10, 100, 10, green)
    ball = Ball(Width//2, Height//2, 7, 7, white)

    playerList = [player1, player2]

    player1_score, player2_score = 0, 0
    player1_yFac, player2_yFac = 0, 0

    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2_yFac = -1
                if event.key == pygame.K_DOWN:
                    player2_yFac = 1
                if event.key == pygame.K_w:
                    player1_yFac = -1
                if event.key == pygame.K_s:
                    player1_yFac = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2_yFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1_yFac = 0

        for player in playerList:
            if pygame.Rect.colliderect(ball.get_rect(), player.get_rect()):
                ball.hit()

        player1.update(player1_yFac)
        player2.update(player2_yFac)
        point = ball.update()

        if point == -1:
            player1_score += 1
        elif point == 1:
            player2_score +=1

        if point:
            ball.reset()

        player1.display()
        player2.display()
        ball.display()

        display_score("Player 1: ", player1_score, 100, 20, white)
        display_score("Player 2: ", player2_score, Width-100, 20, white)

        pygame.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()