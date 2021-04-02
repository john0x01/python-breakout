import pygame, random
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BACK_COLOR = (0, 0, 0)

SPEED = 5
fps = 30

player_pos = [WIDTH / 2, 500]
player_len = 100
player_height = 10

ball_size = 15
ball_pos = [random.randint(0, 790), 50]

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('jogo3')

clock = pygame.time.Clock()


def falling_ball(ball_pos):

	x_pos = (random.randint(0, 799), 50)
	y_pos = 0
	ball_pos.append([x_pos, y_pos])

def update_ball(ball_pos):

	if ball_pos[1] >= 0 and ball_pos[1] < HEIGHT:
		ball_pos[1] = ball_pos[1] + SPEED


def colision(ball_pos, player_pos):
	b_x = ball_pos[0]
	b_y = ball_pos[1]

	p_x = player_pos[0]
	p_y = player_pos[1]

	if (b_x > p_x and b_x < (p_x + player_len)) or (p_x >= b_x and p_x < (b_x + ball_size)):
		if (b_y > p_y and b_y < (p_y + player_height)) or (p_y >= b_y and p_y < (b_y + ball_size)):
			return True
		return False



def fim_de_jogo(ball_pos):

	if ball_pos[1] == 600:
		return True
	return False



game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT and x != 0:
				x = x - 50
			elif event.key == pygame.K_RIGHT and x != 700:
				x = x + 50

			player_pos = [x, y]


	screen.fill((BACK_COLOR))

	falling_ball(ball_pos)
	update_ball(ball_pos)
	

	if colision(ball_pos, player_pos):
		ball_pos = [random.randint(0, 799), 50]
		score = score + 1

	if score < 5:
		fps = 30

	elif 10 > score >= 5:
		fps = 32

	elif 13 > score >= 10:
		fps = 35

	elif 16 > score >= 13:
		fps = 40

	elif 20 > score >= 16:
		fps = 42

	elif score >= 25:
		fps = 45

	if fim_de_jogo(ball_pos):
		game_over = True
		break



	text = "Pontuação: {}".format(score)
	label = font.render(text, 1, YELLOW)
	screen.blit(label, (10, 10))


	pygame.draw.rect(screen, WHITE,(player_pos[0], player_pos[1], player_len, player_height))
	pygame.draw.rect(screen, WHITE,(ball_pos[0], ball_pos[1], ball_size, ball_size))

	clock.tick((fps))

	pygame.display.update()

