import pygame

class player():
    def __init__(self, x, y, w, h, col, players):
        self.x = x ; self.y = y ;self.w = w ;self.h = h
        self.maxSpeed = 7
        self.maxfallspeed = -150
        self.xvelocity = 0
        self.yvelocity = 0
        self.xlim = 780
        self.lives = 4
        self.color = col
        players.add(self)
        self.collision = 0
        self.jumpkey = 0
        self.downkey = 0
        self.released = True


    def is_colliding(self):
        self.collision = + 1

    def get_collision(self):
        return self.collision
    def reset_collision(self):
        self.collision = 0

    def gravity(self, accel):
        self.ChangeVelocity(self.yvelocity + accel * .05)

    #def checkRelease(self):

    # Functions to change the value of the player's vertical position and velocity
    def reset_x_velocity(self):
        self.xvelocity = 0
    def jumpkey_pressed(self,bool):
        self.jumpkey = bool

    def reset_y_velocity(self):
        self.yvelocity = 0

    def ChangeVelocity(self, currvel):
        self.y = self.y - currvel * .05
        if (currvel < self.maxfallspeed):
            self.yvelocity = self.maxfallspeed
        else:
            self.yvelocity = currvel

    def RestartLives(self):
        self.lives = 4

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def height(self):
        return self.h

    def changeX(self, newX):
        self.x = newX

    def changeY(self, newY):
        self.y = newY

    def getVelocity_x(self):
        return self.xvelocity

    def getVelocity_y(self):
        return self.yvelocity

    def brake(self, currvel):
        currvel *= .35
        if (currvel < .01):
            currvel = 0
        return currvel

    def left_key_pressed(self):
        if (self.xvelocity <= 0):  # Character is currently moving left or standing still
            if (self.xvelocity < -1 * self.maxSpeed):
                self.xvelocity = -1 * self.maxSpeed
            else:
                self.xvelocity -= .20
        else:  # Character was previously moving right, lower momentum
            self.xvelocity -= .75
        #self.move_x()

    def right_key_pressed(self):
        if (self.xvelocity >= 0):  # Charcter is currently moving right or standing still
            if (self.xvelocity > self.maxSpeed):
                self.xvelocity = self.maxSpeed
            else:
                self.xvelocity += .20
        else:  # Previously moving left, lower momentum
            self.xvelocity += .75
       # self.move_x()


    def move_x(self):
        self.x += self.xvelocity

    def brake(self):
        self.xvelocity *= .35
        if (self.xvelocity < .01):
            self.xvelocity = 0

    def at_limit(self):
        if (self.x >= self.xlim):
            self.x = self.xlim
            self.xvelocity = 0

    def playerCollision(self, player):
        # Check if the user's y coordinates match up
        if not ( (self.y + self.h < player.y ) or (self.y > player.y + player.h ) ):
            # Bounce the player left
            if   (self.x + self.w > player.x  ) and (self.x + self.w < player.x + player.w):
                self.xvelocity = -.3
            # Bounce the player right
            elif (self.x  > player.x ) and (self.x  < player.x + player.w):

                self.xvelocity = .3


    def drawPlayer(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))

    def check_death(self, deathzone):
        if self.y > deathzone:
            self.lives += -1
            self.reset_x_velocity()
            self.reset_y_velocity()
            self.changeY(275)
            self.changeX(390)

    def draw_lives(self, window,xpos,ypos):

        for i in range(0, self.lives):
            pygame.draw.rect(window, self.color, (xpos, ypos , 10, 10))
            xpos += 15

    def fastfall(self, down):
        if (self.yvelocity <= 0 and self.yvelocity >= -100 and down):
            self.yvelocity = self.maxfallspeed

    def outOfLives(self):
        if(self.lives <= 0):
            return True
        return False
    def addOffset(self, off):
        self.x += off




