import pygame, sys
from pygame.locals import QUIT
import map
import math
#aaaa

def calcColor(distance, max_distance):
    # Assuming distance is in the range [0, max_distance]
    # You may need to adjust this range based on your specific case.

    # Calculate the darkness factor based on the distance
    darkness_factor = distance / max_distance

    # Make sure the darkness factor is within the range [0, 1]
    darkness_factor = max(0.0, min(darkness_factor, 1.0))

    # Calculate the RGB values using the darkness factor
    r = 0
    g = int(255 * (1 - darkness_factor))
    b = 0

    return (r,g,b)

def DetermineHeight(angle, d, SCREENWIDTH, SCREENHEIGHT):
    # Convert angle from degrees to radians
    angle_rad = math.radians(angle)
    
    angle_rad *= -1

    d = d-renderDist

    # Calculate the coordinates of Point A
    x1 = SCREENWIDTH / 2 + d * math.cos(angle_rad)
    y1 = SCREENHEIGHT / 2 + d * math.sin(angle_rad)
    
    # Calculate the coordinates of Point B
    x2 = SCREENWIDTH / 2 - d * math.cos(angle_rad)
    y2 = SCREENHEIGHT / 2 - d * math.sin(angle_rad)
    
    return (x1, y1), (x2, y2)

def castray(startpos, dir, max_dist):
    lastpos = (0,0)
    current_pos = startpos
    step= 1
    poses = []
    for _ in range(0, max_dist, step):
        current_pos = current_pos[0] + step * math.cos(math.radians(dir)), current_pos[1] - step * math.sin(math.radians(dir))
        for i in squares:
            if i.colliderect((current_pos[0],current_pos[1], 1,1)):
                try:
                  lastpos = poses[len(poses)-1]
                except IndexError:
                  PlayerChar.pos = (100,100)
                return lastpos, _
            poses.append(current_pos)
        
    lastpos = poses[len(poses)-1]
    return lastpos, max_dist

def point_in_front_of_player(player_x, player_y, player_rotation, distance):
    theta = math.radians(player_rotation)

    # Calculate the x and y components of the direction vector
    direction_x = math.cos(theta)
    direction_y = math.sin(theta)

    # Calculate the coordinates of the point in front of the player
    point_x = player_x + distance * direction_x
    point_y = player_y - distance * direction_y

    return (point_x, point_y)

class player():
  def __init__(self,size,  startpos= (30,30)):
    self.startpos = startpos
    self.pos = startpos
    self.img = pygame.image.load("D:\Python Projects\\3d Gen TEst\PLAYER (1).png")
    self.img = pygame.transform.scale(self.img, (size,size))
    self.imgrect = self.img.get_rect(center = self.pos)
    self.rot_img = self.img
  def rotate(self,dir):
    self.rot_img = pygame.transform.rotate(self.img, dir)
    
  def draw(self):
    DISPLAYSURF.blit(self.rot_img, self.pos)
  def move(self):
    self.pos = point_in_front_of_player(self.pos[0], self.pos[1], playerRot, 3)
class world():
  def __init__(self,squareSize,SquareColor, Solid=False):
    self.squaresSize = squareSize
    self.squaresColor = SquareColor
    self.solid = Solid
    self.map = map.getMap()
  def DrawMap(self):
    for i in range(0,len(self.map)):
      for j in range(0,len(self.map[i])):
        if self.map[j][i]:
          pygame.draw.rect(DISPLAYSURF, self.squaresColor, (i*self.squaresSize, j*self.squaresSize, self.squaresSize, self.squaresSize))
pygame.init()
clk = pygame.time.Clock()
squares = []
DISPLAYSURF = pygame.display.set_mode((400, 300), pygame.RESIZABLE)
pygame.display.set_caption('Hello World!')
worldmap = world(25, (155,155,155))
PlayerChar = player(10)
playerRot = 0
height = 0
FOV = 60
halfFov = 30
linewidth = 5
renderDist = 100
fovVsScnx = DISPLAYSURF.get_width()/FOV
fovVsScny = DISPLAYSURF.get_height()/FOV
forwardDown = False
leftDown = False
rightDown = False
drawMap = False
hitwall = False
rays = []
for i in range(0,len(worldmap.map)):
      for j in range(0,len(worldmap.map[i])):
        if worldmap.map[j][i]:
           squares.append(pygame.rect.Rect(i*worldmap.squaresSize, j*worldmap.squaresSize, worldmap.squaresSize, worldmap.squaresSize))

while True:
    
    DISPLAYSURF.fill((0,0,255))
    pygame.display.set_caption(f"3d Rendered Maze. FPS: {int(clk.get_fps())}")
    for i in range((halfFov-FOV), FOV):
      pos, dist = castray(PlayerChar.pos, playerRot+i , renderDist)
      #pygame.draw.line(DISPLAYSURF, (0,255,0), PlayerChar.pos,pos )
      (x1,y1), (x2,y2) = DetermineHeight(90,dist, DISPLAYSURF.get_width(),DISPLAYSURF.get_height())
      pygame.draw.line(DISPLAYSURF, calcColor(dist, renderDist), (x1+i*linewidth,y1+fovVsScny), (x2+i*linewidth,y2+fovVsScny), int(linewidth))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            leftDown = True

          if event.key == pygame.K_RIGHT:
            rightDown = True
          if event.key == pygame.K_UP:
            forwardDown = True
          if event.key == pygame.K_m:
            drawMap = not drawMap
            
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
            leftDown = False

          if event.key == pygame.K_RIGHT:
            rightDown = False
          if event.key == pygame.K_UP:
            forwardDown = False
    if forwardDown and not drawMap:
      PlayerChar.move()
    if leftDown and not drawMap:
      playerRot -= 10
      PlayerChar.rotate(playerRot)
    if rightDown and not drawMap: 
      playerRot += 10
      PlayerChar.rotate(playerRot) 
    if drawMap:
      worldmap.DrawMap()
      PlayerChar.draw()
    clk.tick(30)
    pygame.display.flip()