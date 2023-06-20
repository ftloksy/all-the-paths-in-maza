# In the maze, there are many doors.
# Each door can be opened or closed.
# When the program walks through a door,
# the door's counter is incremented.
class Door:
  def __init__(self, doorOpen):
    self.isOpen = doorOpen
    self.goThrough = 0

  def isDoorOpen(self):
    return self.isOpen

  def getGoThrough(self):
    return self.goThrough

  def passedDoor(self):
    self.goThrough += 1