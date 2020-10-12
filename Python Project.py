import pygame
#define colours and set screen size
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green = (0,255,0)
size = (width,height) = (600,600)
clock = pygame.time.Clock()
ctrl = white

bxspeed,byspeed=1,1
pxspeed,pyspeed=0,0
b2xspeed,b2yspeed =1.5,1.5
#Initialize and create screen
pygame.init()
screen = pygame.display.set_mode(size)
#define dimensions for target circle and player rectangle
px,pw,ph = 300,100,5
bx,by,bc = 100, 100,red
b2x,b2y,b2c = 500,100,black
r = 25
py = height - ph
pcolor = blue

#Create font
font1 = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 25)
font3 = pygame.font.Font(None, 25)
font4 = pygame.font.Font(None, 50)
score = 0
lives = 3
level = 1



#main game loop
running = True
while running:
    if score>=5:
        level = 2
        if circle_rect2.top>575:
            lives -= 1
            b2x,b2y = 400,100
        if circle_rect2.colliderect(player_rect):
            score = score + 1

    #Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #movement
        #keydown
        if event.type==pygame.KEYDOWN:
            #left
            if event.key==pygame.K_LEFT:
                pxspeed = -1.5
            #right
            if event.key==pygame.K_RIGHT:
                pxspeed = 1.5
           

            #keyup
        if event.type==pygame.KEYUP:
            #left
            if event.key==pygame.K_LEFT:
                pxspeed = 0
            #right
            if event.key==pygame.K_RIGHT:
                pxspeed = 0
            

    #Logic
    txtImg1 = font1.render(f"Score:{score}",True,black)
    txtImg2 = font2.render(f"Lives:{lives}",True,black)
    txtImg3 = font3.render(f"Level:{level}",True,black)
    txtImg4 = font4.render("Game over",True,ctrl)
    player_rect =pygame.Rect(px,py,pw,ph)
    px=px+pxspeed
    #square of cirlce1
    circle_rect = pygame.Rect(bx-r,by-r,2*r,2*r)
    line_rect = pygame.Rect(0,30,600,4)
    circle_rect2 = pygame.Rect(b2x-r,b2y-r,2*r,2*r)
    if circle_rect.right>width or circle_rect.left<0:
        bxspeed=-bxspeed
    if circle_rect2.right>width or circle_rect2.left<0:
        b2xspeed= -b2xspeed
    if circle_rect.top>575:
        lives -= 1
        bx,by = 100,100
    if circle_rect2.top>575:
        b2x,b2y = 400,100
        
        

    #col check
    if circle_rect.colliderect(player_rect):
        byspeed=-byspeed
        score = score + 1
    if circle_rect2.colliderect(player_rect):
        b2yspeed=-b2yspeed

    if circle_rect.colliderect(line_rect):
        byspeed=-byspeed
    if circle_rect2.colliderect(line_rect):
        b2yspeed=-b2yspeed


 
    bx+=bxspeed
    by+=byspeed
    b2x+=b2xspeed
    b2y+=b2yspeed
    




    
    #boundry
    if px>width-pw: 
        px=width-pw
    if px<1:
        px=0
    if lives==0:
        byspeed=0
        bxspeed = 0
        b2yspeed=0
        b2xspeed = 0
        pyspeed=0
        pxspeed=0
        ctrl = green
    
        
        
    
    

    #Draw
    screen.fill(white)
    
    screen.blit(txtImg1,(10,10))
    screen.blit(txtImg2,(525,10))
    screen.blit(txtImg3,(270,10))
    screen.blit(txtImg4,(200,300))
    
  
    pygame.draw.rect(screen,pcolor,player_rect)
    pygame.draw.rect(screen,black,line_rect)
    pygame.draw.circle(screen,bc,circle_rect.center,r)
    pygame.draw.circle(screen,b2c,circle_rect2.center,r)
    clock.tick(128)
        

    

    
    pygame.display.flip()

pygame.quit()
