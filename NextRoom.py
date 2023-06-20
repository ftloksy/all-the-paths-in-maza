class NextRoom:
  def __init__(self, roomLocation, door):
    self.roomLocation = roomLocation
    self.passDoor = door
  
  def getNextRoomLocation(self):
    return self.roomLocation
  
  def getPassDoor(self):
    return self.passDoor