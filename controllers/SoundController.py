from pygame import mixer


def play_music(file_path, channel_id):
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(file_path)

    # Setting the volume
    mixer.music.set_volume(0.5)

    # Start playing the song
    mixer.Channel(channel_id).play(mixer.Sound(file_path))


# MUSIC

def play_main_theme():
    play_music("sounds/music/main_theme.mp3", 0)


def game_over_theme():
    play_music("sounds/music/game_over.wav", 0)


# SFX

def damage_sound():
    play_music("sounds/sfx/damage.mp3", 1)


def jump_sound():
    play_music("sounds/sfx/jump.mp3", 1)


def collect_coin_sound():
    play_music("sounds/sfx/collect_coin.mp3", 1)


def navigation_sound():
    play_music("sounds/sfx/navigation.mp3", 1)
