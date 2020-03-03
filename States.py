import pygame

def text_objects(text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

def Pause(display, dwidth, dheight):
        paused = True
        text = pygame.font.SysFont("calibri", 115)
        TextSurf, TextRect = text_objects("PAUSED", text)
        TextRect.center = ((dwidth / 2), (dheight / 2))
        display.blit(TextSurf, TextRect)
        while paused:
            pygame.display.update()
            for event in pygame.event.get():  # Gets a list of all of the events that happen
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_p:
                        return

def GameOver(display,dwidth,dheight):
    text = pygame.font.SysFont("calibri", 115)
    TextSurf, TextRect = text_objects("GAME OVER", text)
    TextRect.center = ((dwidth / 2), (dheight / 2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    pygame.time.wait(2000)


def gameintro(display,dwidth,dheight):
    intro = True
    while intro:
        for event in pygame.event.get(): # Gets a list of all of the events that happen
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((255,255,255))
        largeText = pygame.font.Font("freesansbold.ttf", 100)
        TextSurf, TextRect = text_objects("Movement Test", largeText)
        TextRect.center = ((dwidth / 2), (dheight / 2))
        display.blit(TextSurf, TextRect)
        pygame.display.update()


#def fullScreen():

