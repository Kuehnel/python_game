class End_kit:

    # 0 = empty
    # 1 = block
    # 2 = saw
    # 3 = wall left
    # 4 = wall right
    # 5 = ceiling
    # 6 = coin
    # 9 = connector
    # 8 = goal

    def __init__(self):
        self.tile_map = [[0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 3, 8, 0],
                         [1, 1, 1, 1, 1, 1],
                         ]
        self.neutral_list = [0, 0, 0, 0, 0, 0]

        self.connector_index_l = 1
        self.connector_index_r = -1


