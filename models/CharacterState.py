from enum import Enum


class CharacterState(Enum):
    IDLE = 1
    RUN = 2
    JUMP = 3
    DAMAGED = 4
    ATTACK = 5
