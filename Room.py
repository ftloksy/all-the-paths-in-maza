from Door import Door

# Each room has four doors: top, right, bottom, and left.
# Each room has a recorder to record
# hasArrived: the program has walked through the room.
# The x and y coordinates of the room are its location on the map.
class Room:
  def __init__(self, 
      topDoor, 
      rightDoor,
      bottomDoor,
      leftDoor,
      xLocation,
      yLocation):
    self.topDoor = topDoor
    self.rightDoor = rightDoor
    self.bottomDoor = bottomDoor
    self.leftDoor = leftDoor
    self.x = xLocation
    self.y = yLocation
    self.hasArrived = False
  def setArrived(self):
    self.hasArrived = True
  def clearArrived(self):
    self.hasArrived = False
  def getTopDoor(self):
    return self.topDoor
  def getLeftDoor(self):
    return self.leftDoor
  def getRightDoor(self):
    return self.rightDoor
  def getBottomDoor(self):
    return self.bottomDoor
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def isHasArrived(self):
    return self.hasArrived

  def __str__(self):
    rString = "( {}, {} )".format(self.x, self.y)
    return rString