class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __repr__(self) -> str:
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, newWidth):
    self.width = newWidth
  
  def set_height(self, newHeight):
    self.height = newHeight
  
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)
  
  def get_picture(self):
    
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    picture = ("*" * self.width for line in range(self.height))

    return "\n".join(picture) + "\n"
  
  def get_amount_inside(self, otherShape):
    if self.width < otherShape.width or self.height < otherShape.height:
      return 0
    
    #determining the solution based in the Area should work for rectangles shapes
    return (self.get_area() // otherShape.get_area())



class Square(Rectangle):
  
  def __init__(self, side):
    self.set_width(side)
  
  def __repr__(self) -> str:
    return f"Square(side={self.width})"
  
  def set_width(self, newWidth):
    self.width = newWidth
    self.height = newWidth
  
  def set_height(self, newHeight):
    self.set_width(newHeight)

  def set_side(self, newSide):
    self.set_width(newSide)