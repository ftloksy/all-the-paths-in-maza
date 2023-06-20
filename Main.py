from Door import Door
from Room import Room
from MazeMap import MazeMap
from Route import Route

# The map has three rooms: mainRoom, rightRoom, and bottomRoom.
# Two doors are opened:
# * mainRightDoor: connects mainRoom and rightRoom.
# * mainBottomDoor: connects mainRoom and bottomRoom.
# The other doors are closed.
if __name__ == "__main__":
  mainRightDoor = Door(True)
  mainBottomDoor = Door(True)
  mainRoom = Room(Door(False), mainRightDoor, mainBottomDoor, Door(False), 0, 0)
  rightRoom = Room(Door(False), Door(False), Door(False), mainRightDoor, 1, 0)
  bottomRoom = Room(mainBottomDoor, Door(False), Door(False), Door(False), 0, 1)
  mazeMap = MazeMap((mainRoom, rightRoom, bottomRoom))
  myRoute = Route(mazeMap)

  # If the startRoom has any doors that have not been gone through,
  # still run the `stepInMaze` method.
  while not myRoute.isStartRoomAllDoorGoThrough():
    myRoute.stepInMaze()

  # Print out the routes information.
  n = 0
  for route in myRoute.getRoute():
    n += 1
    print("-- {} Route --".format(n))
    for room in route:
      print(room)
