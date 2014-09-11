import pygame
pygame.init()

class Enemywalking1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.STANDING = 0
        self.MOVING = 1 
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.frame = 0
        self.delay = 3
        self.pause = 0
        self.state = self.STANDING
        pygame.mixer.init()
    def update(self):
        if self.state == self.STANDING:
            self.image = self.imageStand
        else:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.mooImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.mooImages[self.frame]

    def loadImages(self):
        self.imageStand = pygame.image.load("images/firedragon fliegt s0000.bmp")
        self.imageStand = self.imageStand.convert()
        transColor = self.imageStand.get_at((1, 1))
        self.imageStand.set_colorkey(transColor)

        self.mooImages = []
        for i in range(7):
            imgName = "images/firedragon fliegt s0001.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
            imgName = "images/firedragon fliegt s0002.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
            imgName = "images/firedragon fliegt s0003.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
            imgName = "images/firedragon fliegt s0004.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
            imgName = "images/firedragon fliegt s0005.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
            imgName = "images/firedragon fliegt s0006.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
            imgName = "images/firedragon fliegt s0007.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
            imgName = "images/firedragon fliegt s0008.bmp"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)
screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

enemywalking = Enemywalking1()
allSprites = pygame.sprite.Group(enemywalking)

clock = pygame.time.Clock()
keepGoing = True

while keepGoing:
    clock.tick(30)
    enemywalking.state = enemywalking.MOVING
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)
    
    pygame.display.flip()
