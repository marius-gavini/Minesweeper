class Tile():
    def __init__(self, is_mine:bool, state:int=-1):
        self.state = state
        self.is_mine = is_mine

    def check_tiles_value(self, coordinate: tuple):
        y, x = coordinate
        targeted_tile = board[y][x]

        if targeted_tile.is_mine == True:
            targeted_tile.state = -2
            return 
            
        mine_number = 0
        height = len(board)
        width = len(board[0])

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue

                ny, nx = y + dy, x + dx

                if 0 <= ny < height and 0 <= nx < width:
                    if board[ny][nx].is_mine:
                        mine_number += 1


        self.set_tile_state(targeted_tile, mine_number)
    
    def set_tile_state(self, tile, state):
        tile.state = state


board = [
    # Ligne 1
    [ Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(True), Tile(False) ],
  
    # Ligne 2
    [ Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False),
      Tile(True), Tile(False), Tile(False) ],

    # Ligne 3
    [ Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False) ],

    # Ligne 4
    [ Tile(False), Tile(True), Tile(True),
      Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False) ],

    # Ligne 5
    [ Tile(True), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False) ],

    # Ligne 6
    [ Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(True),
      Tile(False), Tile(False), Tile(False) ],

    # Ligne 7
    [ Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False),
      Tile(True), Tile(False), Tile(False) ],

    # Ligne 8
    [ Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(False),
      Tile(False), Tile(False), Tile(True) ],

    # Ligne 9
    [ Tile(True), Tile(False), Tile(False),
      Tile(False), Tile(True), Tile(False),
      Tile(False), Tile(False), Tile(False) ]
]

# while True:

#     y = int(input("enter y coordinate (1 - 9): "))
#     x = int(input("enter x coordinate (1 - 9): "))

#     board[y-1][x-1].check_tiles_value((y-1, x-1))
#     print(board[y-1][x-1].state)

#     r = input("Continue ? (y/n)").lower()

#     if r == "y":
#         continue
#     else:
#         break
