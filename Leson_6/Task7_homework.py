#Создайте программу для игры в "Крестики-нолики".

from turtle import color
import pygame

def check_win(mas, mean):
    zero = 0
    for row in mas:
        zero += row.count(0)
        if row.count(mean) == 3:
            return mean
    for col in range(3):
        if mas[0][col] == mean and mas[1][col] == mean and mas[2][col] == mean:
            return mean
    if mas[0][0] == mean and mas[1][1] == mean and mas[2][2] == mean: 
                return mean
    if mas[0][2] == mean and mas[1][1] == mean and mas[2][0] == mean:
                return mean
    if zero == 0:
        return 'Draw'
    return False

pygame.init()
size_block = 150
margin = 10
width = height = (size_block*3) + (margin*2) # формула размеров игрового поля

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики Hолики: Пробел для перезапуска игры')

black =(0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
step = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
            if mas[row][col] == 0:
                if step%2 ==0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                step += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            step = 0
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col*size_block + (col +1)+ margin
                y = row*size_block + (row +1)+ margin
                pygame.draw.rect(screen, color, (x,y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x+10, y+10), (x+size_block-10, y+size_block-10), 4)
                    pygame.draw.line(screen, white, (x+size_block-10, y+10), (x+10, y+size_block-10), 4)
                elif color == green:
                    pygame.draw.circle(screen, white, (x+size_block//2, y+size_block//2), size_block//2-10, 4)
   
    if (step-1)%2 == 0: # выйграли крестики?
       game_over = check_win(mas, 'x')
    else: # выйграли нолики?
       game_over = check_win(mas, 'o')
    
    if game_over:
        screen.fill(black)
        front = pygame.font.SysFont('Tahoma', 280)
        text1 = front.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text1, [text_x, text_y-30])

    pygame.display.update()