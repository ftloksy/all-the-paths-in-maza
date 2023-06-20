# The MazeMap class records the map of the maze.
# The `rooms` attribute records all rooms in an array.
# The `getRoom` method takes an x and y location as input,
# and returns the room at that location.
# The `isAllRoomsArrived` method checks 
# if the program has gone through all the rooms in the maze.
class MazeMap:
  def __init__(self, rooms):
    self.rooms = rooms
  def getRoom(self, x, y):
    for r in self.rooms:
      if r.getX() == x and r.getY() == y:
        return r
  def isAllRoomArrived(self):
    for r in self.rooms:
      if not r.isHasArrived(): 
        return False
    return True 