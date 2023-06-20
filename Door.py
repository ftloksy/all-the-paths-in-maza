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