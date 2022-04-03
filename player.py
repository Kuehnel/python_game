class Player:
    x = 300
    y = 300
    velocity = 5
    width = 30
    height = 50

    jump_state = -16

    dash_state = -16
    dash_speed = 20

    line_of_sight = 1

    grounded = False
    next_y = 0
    next_x = 0

