class MazaMap:
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