import pygame

class platform():
    def __init__(self, x, y, w, h, is_solid, platforms, move):
        self.x = x
        self.startingX = x
        self.y = y
        self.w = w
        self.h = h
        self.is_solid = is_solid
        self.move_rate = move
        platforms.add(self)

    def platdim(self):
        return self.x + self.w

    def platY(self):
        return self.y
    def get_h(self):
        return self.h
    def check_solid(self):
        return self.is_solid
    def move_x(self):
        if(self.x > self.startingX + 2* self.w):
            self.move_rate *= -1
        elif(self.x < self.startingX - 2*self.w):
            self.move_rate *= -1
        self.x += self.move_rate

    def drawPlatform(self, win):
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.w, self.h))
