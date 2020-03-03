from platform import platform


class stage():
    def __init__(self, name):
        self.stageName = name

    def load_platforms(self):
        platforms = set()
        if (self.stageName == 'test'):
            base1 = platform(100, 550, 300, 50, 1, platforms,0)
            base2 = platform(400, 550, 300, 50, 1, platforms,0)
            pete = platform(550, 450, 100, 20, 0, platforms,0)
            joe = platform(150, 450, 100, 20, 0, platforms,0)
            bob = platform(350, 350, 100, 20, 0, platforms,0)
            return platforms

        elif (self.stageName == 'test2'):
            base1 = platform(100, 550, 300, 50, 1, platforms,0)
            base2 = platform(400, 550, 300, 50, 1, platforms,0)
            pete = platform(300, 425, 150, 20, 0,platforms,1.5)

            return platforms


    # def stage_movement(self):
    #     if (self.stageName == 'test2'):
    #         x_change = 3
    #         base1 = platform(100, 550, 300, 50, 1, platforms)
    #         base2 = platform(400, 550, 300, 50, 1, platforms)

