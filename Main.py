from Door import Door
from Room import Room
from MazaMap import MazaMap
from Route import Route

# top, right, bottom, left. 
if __name__ == "__main__":
  mainRightDoor = Door(True)
  mainBottomDoor = Door(True)
  mainRoom = Room(Door(False), mainRightDoor, mainBottomDoor, Door(False), 0, 0)
  rightRoom = Room(Door(False), Door(False), Door(False), mainRightDoor, 1, 0)
  bottomRoom = Room(mainBottomDoor, Door(False), Door(False), Door(False), 0, 1)
  mazaMap = MazaMap((mainRoom, rightRoom, bottomRoom))
  myRoute = Route(mazaMap)

  while not myRoute.isStartRoomAllDoorGoThrough():
    myRoute.startRoute()

  n = 0
  for route in myRoute.getRoute():
    n += 1
    print("-- {} Route --".format(n))
    for room in route:
      print(room)
