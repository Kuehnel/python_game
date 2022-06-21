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
        self.tile_map = [[5, 5, 5, 5, 5, 5],
                         [3, 0, 0, 0, 0, 4],
                         [9, 6, 0, 0, 0, 9],
                         [1, 1, 2, 2, 2, 1],
                         ]
        self.neutral_list = [0, 0, 0, 0, 0, 0]

        self.connector_index_l = 2
        self.connector_index_r = 1
