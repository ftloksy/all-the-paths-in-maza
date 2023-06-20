from NextRoom import NextRoom
from Helper import isItemInArray

# I moved more logic into the class.
# Because when you are walking inside a maze,
# everything is unknown to you and
# you need to recover in the maze.
#
# # The `start_room` attribute is a x, y location.
# It records all routes that start in this room.
# In the maze, there may be more than one way to go through all rooms.
# The `routesPool` attribute records all the ways.
# The `startRouteDoors` attribute is an array.
# It records the first doors of all ways.
# The `Route` attribute is an array.
# It will record the rooms that the program has gone through, 
# and store them in the route.
# The `step` attribute will be updated 
# when the program goes through a room.
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

  # Run the method before finding every new route.
  def stepInMaze(self):
    self.route = []
    self.step = 0
    self.routesPool.append(self.route)
    x = self.startRoom[0]
    y = self.startRoom[1]
    for r in self.map.rooms:
      r.clearArrived()
    self.currentRoom = self.map.getRoom( x, y)
    self.route.append(self.currentRoom) 
    self.setRoomArrived( x, y )
    # Every route must go through all rooms.
    while not self.isAllRoomArrived():
      self.nextRooms = self.canGoToRooms()
      self.goToNextRoom()
      self.step += 1

  def canGoToRooms(self):
    """Finds the rooms that can be gone through.

    attribute:
      rooms: An array of rooms.
      nowRoom: is program corrent Room / stand on Room.

    Returns:
      A list of rooms ( NextRoom ) that can be gone through.
    """

  # If the rooms had opened doors, but the doors didn't connect any rooms,
  # it will have a bug.
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
    """Chooses a room to go to and goes through the door.

    Attribute:
      rooms: A list of rooms.

    Action:
      The room that was gone through.
    """

    # Finds the room's door with the least number of go-through times.
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

  # Check if all doors in the startRoom have been gone through.
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