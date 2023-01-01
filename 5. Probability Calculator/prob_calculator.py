import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **colors):
    self.hat = colors
    self.contents = []

    for color, numberOfBalls in colors.items():
      self.contents += [color] * numberOfBalls
    
  
  def draw(self, numberOfBallsToDraw):
    
    toReturn = []

    if len(self.contents) < numberOfBallsToDraw:
      toReturn = self.contents.copy()
      self.contents = []
      return toReturn
    
    while numberOfBallsToDraw > 0:
      randomIndex = random.randint(0, len(self.contents) - 1)
      toReturn.append(self.contents[randomIndex])
      self.contents.pop(randomIndex)

      numberOfBallsToDraw -= 1
    
    return toReturn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  #number of succesful assertions
  M = 0

  expected_ball_contents = []
  for color, numberOfBalls in expected_balls.items():
      expected_ball_contents += [color] * numberOfBalls
  
  expected_ball_contents = sorted(expected_ball_contents)
  
  for i in range(num_experiments):
    hatCopy = copy.deepcopy(hat)

    draw = sorted(hatCopy.draw(num_balls_drawn))
    originalLen = len(draw)

    for ball in expected_ball_contents:
      if ball not in draw:
        break
      
      draw.pop(draw.index(ball))

    if len(draw) == (originalLen - len(expected_ball_contents)):
      M += 1

  return M/num_experiments