from NextRoom import NextRoom
from Helper import isItemInArray

# I move more logic inside this class.
# Because when you are walking inside a maza,
# Everything you don't know and
# You need to recover in the maza.
class Route:
  def __init__(self, map):
    self.startRoom = (0, 0)
    self.map = map
    self.routesPool = []
    self.startRouteDoors = []
    self.route = []
    self.step = 0

  def setRoomArrived(self, x, y):
    self.map.getRoom(x, y).setArrived()

  def isAllRoomArrived(self):
    return self.map.isAllRoomArrived()

  def getCurrentRoom(self):
    return self.route[-1]

  def startRoute(self):
    self.route = []
    self.step = 0
    self.routesPool.append(self.route)
    for r in self.map.rooms:
      r.clearArrived()
    self.currentRoom = self.map.getRoom(
      self.startRoom[0], self.startRoom[1])
    self.route.append(self.map.getRoom(
      self.startRoom[0], self.startRoom[1]))
    self.setRoomArrived(
      self.startRoom[0], self.startRoom[1])
    while not self.isAllRoomArrived():
      self.nextRooms = self.canGoToRooms()
      self.goToNextRoom()
      self.step += 1

  def canGoToRooms(self):
    nowRoom = self.getCurrentRoom()
    rooms = []
    x = nowRoom.getX()
    y = nowRoom.getY()
    if nowRoom.getTopDoor().isDoorOpen():
      rooms.append(NextRoom((x, y - 1), nowRoom.getTopDoor()))
    if nowRoom.getBottomDoor().isDoorOpen():
      rooms.append(NextRoom((x, y + 1), nowRoom.getBottomDoor()))
    if nowRoom.getLeftDoor().isDoorOpen():
      rooms.append(NextRoom((x - 1, y), nowRoom.getLeftDoor()))
    if nowRoom.getRightDoor().isDoorOpen():
      rooms.append(NextRoom((x + 1, y), nowRoom.getRightDoor()))
    return rooms

  def goToNextRoom(self):
    lessGoThrough = 9999
    for r in self.nextRooms:
      doorThrough = r.getPassDoor().getGoThrough()
      if doorThrough < lessGoThrough:
        lessGoThrough = doorThrough
    for r in self.nextRooms:
      door = r.getPassDoor()
      if door.getGoThrough() == lessGoThrough:
        location = r.getNextRoomLocation()
        x = location[0]
        y = location[1]
        self.NextRoom = self.map.getRoom(x, y)
        self.goThroughDoor = door
        break

    self.NextRoom.setArrived()
    self.goThroughDoor.passedDoor()
    self.route.append(self.NextRoom)
    if self.step == 0:
      self.startRouteDoors.append(self.goThroughDoor)

  def getRoute(self):
    return self.routesPool

  def isStartRoomAllDoorGoThrough(self):
    r = self.map.getRoom(self.startRoom[0], self.startRoom[1])

    topDoor = r.getTopDoor()
    isTopDoorOpen = topDoor.isDoorOpen()
    bottomDoor = r.getBottomDoor()
    isBottomDoorOpen = bottomDoor.isDoorOpen()
    leftDoor = r.getLeftDoor()
    isLeftDoorOpen = leftDoor.isDoorOpen()
    rightDoor = r.getRightDoor()
    isRightDoorOpen = rightDoor.isDoorOpen()

    if isTopDoorOpen:
      if not isItemInArray(self.startRouteDoors, topDoor):
        return False
    if isBottomDoorOpen:
      if not isItemInArray(self.startRouteDoors, bottomDoor):
        return False
    if isLeftDoorOpen:
      if not isItemInArray(self.startRouteDoors, leftDoor):
        return False
    if isRightDoorOpen:
      if not isItemInArray(self.startRouteDoors, rightDoor):
        return False

    return True