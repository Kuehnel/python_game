# class that holds kits for level-building
class KitCollection:
    # 0 = empty
    # 1 = floor
    # 2 = spikes
    # 3 = wall
    # 4 = crabby
    # 5 = seashell
    # 7 = platform
    # 8 = goal
    # 6 = coin
    # 9 = block

    def __init__(self):
        self.start_kit_tile_map = [[0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 6, 0, 6],
                                   [0, 0, 0, 7, 4, 7],
                                   [0, 1, 1, 1, 1, 1],
                                   ]

        self.end_kit_tile_map = [[0, 0, 0, 0, 0, 0, 9],
                                 [0, 0, 0, 0, 0, 0, 9],
                                 [0, 0, 0, 0, 0, 8, 9],
                                 [0, 0, 0, 0, 9, 9, 9],
                                 [0, 0, 0, 9, 9, 9, 9],
                                 [0, 0, 9, 9, 9, 9, 9],
                                 [0, 9, 9, 9, 9, 9, 9],
                                 [1, 1, 1, 1, 1, 1, 1],
                                 ]

    test_1_tile_map = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 6, 4, 6, 0, 0],
                       [0, 7, 7, 7, 5, 0],
                       [1, 1, 1, 1, 1, 1],
                       ]

    test_2_tile_map = [[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 6, 0, 6, 0],
                       [0, 0, 7, 0, 7, 0, 7],
                       [0, 7, 0, 0, 0, 4, 0],
                       [1, 1, 1, 1, 1, 1, 1],
                       ]

    test_3_tile_map = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 6, 0, 0],
                       [0, 0, 0, 7, 0, 0],
                       [0, 9, 2, 2, 2, 9],
                       [1, 1, 1, 1, 1, 1],
                       ]

    test_4_tile_map = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 6, 0, 0],
                       [0, 6, 0, 7, 0, 0],
                       [0, 7, 4, 6, 2, 0],
                       [1, 1, 1, 1, 1, 1],
                       ]

    test_5_tile_map = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 6, 6, 0],
                       [0, 0, 9, 6, 6, 0],
                       [0, 9, 9, 4, 6, 6],
                       [1, 1, 1, 1, 1, 1],
                       ]

    test_6_tile_map = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [6, 5, 6, 6, 6, 5],
                       [1, 1, 1, 1, 1, 1],
                       ]

    test_7_tile_map = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 6, 0, 6, 0, 6],
                       [7, 4, 7, 4, 7, 4],
                       [1, 1, 1, 1, 1, 1],
                       ]
