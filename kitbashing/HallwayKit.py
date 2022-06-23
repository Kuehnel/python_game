class Hallway_kit:
    # 0 = empty
    # 1 = platform
    # 2 = saw bottom
    # 3 = wall left
    # 4 = wall right
    # 5 = ceiling
    # 6 = coin
    # 9 = connector

    def __init__(self):
        self.tile_map = [[0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 2, 3, 6, 0],
                         [1, 1, 1, 1, 1, 1],
                         ]
        self.neutral_list = [0, 0, 0, 0, 0, 0]

        self.connector_index_l = 2
        self.connector_index_r = 1
