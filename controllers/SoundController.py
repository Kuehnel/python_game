from pygame import mixer


def play_music(file_path):
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(file_path)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()


def play_main_theme():
    play_music("sounds/music/main_theme.mp3")


def game_over_theme():
    play_music("sounds/music/game_over.wav")
