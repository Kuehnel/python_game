from enum import Enum


# class that represents character state
class CharacterState(Enum):
    IDLE = 1
    RUN = 2
    JUMP = 3
    DAMAGED = 4
    ATTACK = 5
