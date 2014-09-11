import pygame, random, math
pygame.init()
dragontotal = 30
dragons = []
class dragon:
    #initalizing things such as dragonmove.x and y, so I can control the coordinates, and giving the dragons a speed in x and y directions.
    def __init__(dragonmove, x, y):
        dragonmove.x = x
        dragonmove.y = y
        dragonmove.speedx=7
        dragonmove.speedy=7
    def dragonActivity(dragonmove, dragons):    
        # Gets the dragons closer to form a flock
        xcord = 0
        ycord = 0
        #credit goes to http://code.activestate.com/recipes/576959-boids-20-for-python-31/
        for dragon in dragons:    
            xcord += (dragonmove.x - dragon.x)#credit here
            ycord += (dragonmove.y - dragon.y)#credit here
        #end credit
        xcord /= dragontotal
        ycord /= dragontotal
        dragonmove.speedx -= (xcord / 80) 
        dragonmove.speedy -= (ycord / 80)
        xcord=0
        ycord=0
        #Actually using spacing to keep the dragons apart
        #Credit goes to http://bpaste.net/raw/25109/
        for dragon in dragons:
            if  dragonmove.spacing(dragon) < 10:#credit here
                xcord = (dragonmove.x - dragon.x)#credit here
                ycord = (dragonmove.y - dragon.y)#credit here      
                if xcord >= 0: xcord = 3 - xcord#credit here
                else: xcord = -3 - xcord#credit here
                if ycord >= 0: ycord = 3 - ycord#credit here
                else: ycord = -3 - ycord#credit here
        #end credit
        dragonmove.speedx -= xcord / 5
        dragonmove.speedy -= ycord / 5
        #Helps to space out the dragons a bit from each other
    def spacing(dragonmove, dragon):
        xcord = dragonmove.x - dragon.x
        ycord = dragonmove.y - dragon.y
        #I tried creating a feature that would allow you to increase or decrease distance but I am still having trouble with it. I tried to make it so that if you press i
        #you would increase how close dragons get to each other, and if you press d you would decrease how close dragons got to each other
        #for event in pygame.event.get():
            #if event.type== pygame.QUIT:
                #return none
                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_i:
                        #xcord *=100
                        #ycord *=100
                    #if event.key == pygame.K_d:
                        #xcord /=50
                        #ycord/=50
        return math.sqrt(xcord * xcord + ycord * ycord)
    #This code makes sure that the speed never gets too high even if you change the speed values.
    def dragonmove(dragonmove):
        #credit goes to http://www.vpython.org/contents/contributed/boids.py
        if abs(dragonmove.speedx) > 7 or abs(dragonmove.speedy) > 7:#credit here
            reconfig = 7 / max(abs(dragonmove.speedx), abs(dragonmove.speedy))#credit here
            dragonmove.speedx *= reconfig#credit here
            dragonmove.speedy *= reconfig#credit here
            #end credit
        dragonmove.x += dragonmove.speedx
        dragonmove.y += dragonmove.speedy
screenres = width, height = 1024, 1024
screen = pygame.display.set_mode(screenres)
dragonimg = pygame.image.load("images/firedragon fliegt s0000.png")
# this code creates dragons in random places across the screen.
for i in range(dragontotal):
    dragons.append(dragon(random.randint(0, width), random.randint(0, height)))   
while range(dragontotal)!=0:
    #credit goes to http://code.activestate.com/recipes/576959-boids-20-for-python-31/
    for dragon in dragons:
        groupdragons = []#credit here
        for newdragon in dragons:#credit here
            if newdragon == dragon: continue#credit here
            spacing = dragon.spacing(newdragon)#credit here
            groupdragons.append(newdragon)#credit here
        #end credit
        dragon.dragonActivity(groupdragons)    
        dragon.dragonmove()
        # created an invisable border so that if the dragons get too close to the edge of the screen they will be pushed back.
        # Credit goes to http://bpaste.net/raw/25109/
        if dragon.x < 15 and dragon.speedx < 0:#credit here
            dragon.speedx = -dragon.speedx *2
        if dragon.x > width - 15 and dragon.speedx > 0:#credit here
            dragon.speedx = -dragon.speedx *2
        if dragon.y < 15 and dragon.speedy < 0:#credit here
            dragon.speedy = -dragon.speedy *2
        if dragon.y > height - 15 and dragon.speedy > 0:#credit here
            dragon.speedy = -dragon.speedy *2
        #end credit
    color = 255, 0, 0
    screen.fill(color)
    dragonshape = dragonimg.get_rect()
    for dragon in dragons:
        dragonShape = pygame.Rect(dragonshape)
        dragonShape.x = dragon.x
        dragonShape.y = dragon.y
        screen.blit(dragonimg, dragonShape)
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    clock.tick(100)
