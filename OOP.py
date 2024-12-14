import pygame
pygame.init()

w_width = 500
w_height = 500
screen = pygame.display.set_mode((w_width,w_height))
pygame.display.set_caption("Moving and animating sprites")


clock = pygame.time.Clock()
bg_img = pygame.image.load("images/bg_img.jpeg")
bg_img = pygame.transform.scale(bg_img, (w_width, w_height))
walkRight = [pygame.image.load(f'soldier/{i}.png') for i in range(1, 10)]
walkLeft = [pygame.image.load(f'soldier/L{i}.png') for i in range(1, 10)]
char = pygame.image.load('soldier/standing.png')

class player():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1

        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        
        else:
            screen.blit(char, (self.x,self.y))

def DrawInGameloop():
    screen.blit(bg_img, (0,0))
    clock.tick(25)
    soldier.draw(screen)
    pygame.display.flip()

soldier = player(50, 435, 64, 64)
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and soldier.x>0:
        soldier.x -= soldier.vel
        soldier.left = True
        soldier.right = False

    elif keys[pygame.K_RIGHT] and soldier.x < w_width-soldier.width:
        soldier.x += soldier.vel
        soldier.right = True
        soldier.left = False

    else:
        soldier.left = False
        soldier.right = False
        soldier.walkCount = 0

    if not(soldier.is_jump):
        if keys[pygame.K_SPACE]:
            soldier.is_jump = True
            soldier.right = False
            soldier.left = False
    else:
        if soldier.is_jump:
            if soldier.jump_count >=-10:
                neg = 1
                if soldier.jump_count < 0:
                    neg = -1
                soldier.y -= (soldier.jump_count ** 2) * neg * 0.5
                soldier.jump_count -= 1
            else:
                soldier.jump_count = 10
                soldier.is_jump = False

    DrawInGameloop()