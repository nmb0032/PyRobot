import math
from pygame import Surface
from pygame.sprite import Sprite
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame import Vector2 as vec

class Robot(Sprite):

    def __init__(self, position: tuple, vel: tuple, acc: tuple, size=(75,25), color=(255,255,255)):
        """ Defines a Robot Sprite in the Robot Simulation
        Args:
            position (tuple): (x,y) position on screen
            vel (tuple): (x,y) velocity
            size (tuple, optional): [description]. Defaults to (75,25).
            color (tuple, optional): [description]. Defaults to (255,255,255).
        """
        super(Robot, self).__init__()
        self.surf = Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        
        #physics
        self.pos = vec(position)
        self.vel = vel
        self.acc = vec(acc)

    def go_to(self, goal):
        """Goes to a specified goal location indicated in pixels

        Args:
            goal (tuple): (x,y) destination position
        """
        #TODO: add acceleration compensation
        # Check if at destination
        if self.rect.x == goal[0] and self.rect.y == goal[1]: return
        # Calculate angle between start and goal
        angle = Robot.angle_2_points((self.rect.x, self.rect.y), goal)

        x_vel = Robot.calc_x_velocity(self.vel, angle)
        y_vel = Robot.calc_y_velocity(self.vel, angle)

        self.rect.x += x_vel
        self.rect.y += y_vel
        # calculate vector velocity
    



    def set_position(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]



            
            
    def get_max_wheel_velocity(self):
        return(self.max_velocity/self.wheel_radius)

    @staticmethod
    def calc_x_velocity(vel, angle):
        return math.cos(angle) * vel

    @staticmethod
    def calc_y_velocity(vel, angle):
        return math.sin(angle) * vel

    @staticmethod
    def angle_2_points(point1, point2, degrees=False):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]

        angle = math.atan2(dx, dy)

        if degrees:
            angle = math.degrees(angle)
        
        return angle


    


