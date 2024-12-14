import pygame
pygame.init()

w_width = 500
w_height = 500
screen = pygame.display.set_mode((w_width,w_height))
pygame.display.set_caption("Moving and animating sprites")

#creating object
x = 50
y = 435
width = 64
height = 64
vel = 5

clock = pygame.time.Clock()

#jump variables
is_jump = False
jump_count = 10

bg_img = pygame.image.load("images/bg_img.jpeg")
bg_img = pygame.transform.scale(bg_img, (w_width, w_height))

#character
left = False
right = False
walkCount = 0

walkRight = [pygame.image.load(f'soldier/{i}.png') for i in range(1, 10)]
walkLeft = [pygame.image.load(f'soldier/L{i}.png') for i in range(1, 10)]
char = pygame.image.load('soldier/standing.png')

def DrawInGameloop():
    screen.blit(bg_img, (0,0))
    clock.tick(25)

    global walkCount
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount +=1

    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    
    else:
        screen.blit(char, (x,y))

    pygame.display.flip()

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < w_width-width:
        x += vel
        right = True
        left = False

    else:
        left = False
        right = False
        walkCount = 0

    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
    else:
        if is_jump:
            if jump_count >=-10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                y -= (jump_count ** 2) * neg * 0.5
                jump_count -= 1
            else:
                jump_count = 10
                is_jump = False

    DrawInGameloop()