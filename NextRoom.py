# The NextRoom class is used to record
# the room's location (x, y) on the map.
# The `getPassDoor` method will go 
# through the door ( self.passDoor ) 
# and to the next room.
class NextRoom:
  def __init__(self, roomLocation, door):
    self.roomLocation = roomLocation
    self.passDoor = door
  
  def getNextRoomLocation(self):
    return self.roomLocation
  
  def getPassDoor(self):
    return self.passDoor