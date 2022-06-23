class Start_kit:
    # 0 = empty
    # 1 = floor
    # 2 = spikes
    # 3 = wall
    # 4 = ?
    # 5 = ceiling
    # 7 = platform
    # 8 = goal
    # 6 = coin
    # 9 = block

    def __init__(self):
        self.tile_map = [[0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 6],
                         [0, 0, 0, 0, 0, 6],
                         [0, 0, 0, 0, 9, 0],
                         [0, 7, 0, 9, 9, 9],
                         [1, 1, 1, 1, 1, 1],
                         ]
        self.neutral_list = [0, 0, 0, 0, 0, 0]

        self.connector_index_l = -1
        self.connector_index_r = 4
