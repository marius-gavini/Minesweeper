def reveal_tiles(board_pos):
    #define numbers under direction
    for dy in range(-1, 2):
        for dx in range(-1,2):
            if dy == 0 and dx == 0:
                continue
            else:
                result = board.check_tile_value((dy, dx))
            if result == 0:
                focus_tile = reveal_tiles((board_pos))
            else:
                return board