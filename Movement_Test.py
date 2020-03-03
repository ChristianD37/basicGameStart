import pygame
from player import player       # Load in player and platform class
from platform import platform
from stages import stage
from States import Pause, GameOver, gameintro


# TO DO
#   - FIx the left and right key glitch
#   - Collision top and bottom distinction
#   - Make collision part of the player class

pygame.init()
clock = pygame.time.Clock()

winwidth = 800
winheight = 600

win = pygame.display.set_mode((winwidth, winheight)) # Set the  ,pygame.FULLSCREEN, pygame.RESIZABLE
pygame.display.set_caption("Movement Test")


def text_objects(text, font):
    textSurface = font.render(text,True,(0,0,0))
    return textSurface, textSurface.get_rect()

# FIXXX SO THAT ONLY ONE BRANCH RUNS
# Checks if a player is on top of the platform
def collision_check(player, platform):
    if (player.getY() >= platform.platY() - player.height()  and player.getY() <= platform.platY()+platform.get_h() ) and (player.getX() + player.w >= platform.x and player.getX() + player.w *.15 <= platform.x + platform.w) and platform.check_solid():
        return True
    elif (player.getY() >= platform.platY() - player.height()  and player.getY() + player.height()*.7 <= platform.platY()  ) and (player.getX() + player.w >= platform.x and player.getX() + player.w *.15 <= platform.x + platform.w) and not platform.check_solid():
        return True
    else:
        return False

#def collision_bump(player, platform):
 #   if (player.getY() <= platform.platY() + platform.get_h() and player.getY() > platform.platY() + platform.get_h()*.9  and player.getVelocity_y() > 0) and (player.getX() + player.w >= platform.x and player.getX() + player.w *.15 <= platform.x + platform.w):
  #      print("YUP")

def gameloop():
    run = True ;
    stageSelection = stage("test2")
    platforms = stageSelection.load_platforms() # initialize an empty set to contain the platforms
    players = set()

    user = player(200, 375, 20,35, (255, 0, 0), players)
    two = player(400, 515, 20,35, (0, 0, 255), players)

    # Main game loop
    while run:

        for event in pygame.event.get(): # Gets a list of all of the events that happen
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_p:
                    Pause(win,winwidth, winheight)

        keys = pygame.key.get_pressed() # Get a list of keys currently being pressed
        # Check for jump keys
        if keys[pygame.K_SPACE]:
            user.jumpkey_pressed(True)
        else:
            user.jumpkey_pressed(False)

        if keys[pygame.K_KP_ENTER]:
            two.jumpkey_pressed(True)
        else:
            two.jumpkey_pressed(False)
        #Check for down keys
        if keys[pygame.K_s]:
            user.downkey = True
        else:
            user.downkey = False

        if keys[pygame.K_DOWN]:
            two.downkey = True
        else:
            two.downkey = False

        # Player one x movement
        if keys[pygame.K_a]:
            user.left_key_pressed()

        if keys[pygame.K_d]:
            user.right_key_pressed()

        # Player two x movement
        if keys[pygame.K_LEFT]:
            two.left_key_pressed()

        if keys[pygame.K_RIGHT]:
            two.right_key_pressed()

        # Apply slight momentum forward if player releases keys while moving
        if not (keys[pygame.K_d] or keys[pygame.K_a]) and (user.getVelocity_x() > 0 or user.getVelocity_x() < 0):
            user.brake()
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and (two.getVelocity_x() > 0 or two.getVelocity_x() < 0):
            two.brake()

        user.playerCollision(two)
        two.playerCollision(user)


        for play in players:
            #Check for possible collisions
            #collision = 0
            play.reset_collision()
            for plat in platforms:
                if collision_check(play,plat):
                    play.addOffset(plat.move_rate)
                    #collision =+ 1
                    play.is_colliding()
                    curr = plat


            # Platform State
            if play.get_collision():
                if play.jumpkey and play.released:
                    #collision = False
                    play.reset_collision()
                    #play.released = False
                    play.ChangeVelocity(220) # initial jump of velocity

                # Player goes through platform or drops down
                elif play.getVelocity_y() > 0 and not curr.check_solid(): # Allow player to pass through non solid objects
                    play.gravity(-150)  # Constant gravity
                elif play.downkey and not curr.check_solid(): # Allow player to drop through non solid objects
                    #user.reset_y_velocity()
                    play.gravity(-150)
                else: # Player rests on platform
                    #bumped = False
                    # if not play.jumpkey:# Player cannot jump again until they release the space bar
                    #     play.released = True
                    #
                    # else:
                    #     play.released = False
                    play.changeY(curr.platY() - play.height()) # Set the player's y coordinate to the platform that they are currently on top of

            # Air State
            else:
                #Player lets go of spacebar while in the air
                if not play.jumpkey and play.getVelocity_y() >= 0:
                    play.ChangeVelocity(.15* play.getVelocity_y()) # make the loss of upwards momentum more gradual
                play.fastfall(play.downkey)
                play.gravity(-200)  # Constant gravity

    # FIND OUT WHY THE JUMP DELAY IS OCCURING, LIKELY WITH THE RELEASE EFFECT

        win.fill((66,144,245)) # Fill the background
        xpos = 50
        for play in players:
            play.move_x()
            play.at_limit()  # Stop the user from going off screen
            play.check_death(winheight)
            if play.outOfLives():
                GameOver(win, winwidth, winheight)
                play.RestartLives()
            play.draw_lives(win, xpos, 10)
            play.drawPlayer(win)
            xpos += 650

        # Draw all platforms
        for p in platforms:
            p.move_x()
            p.drawPlatform(win)
        pygame.display.update()
        clock.tick(60) # Run at 60 fps
#gameintro(win, winwidth, winheight)
gameloop()