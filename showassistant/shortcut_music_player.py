import keyboard
import pygame
import yaml


def play(music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()


if __name__ == '__main__':
    with open(r'showassistant.yml') as showassistant:
        showassistant = yaml.load(showassistant)
        music_path = showassistant["music"]["path"]
        music_mapping = showassistant["music"]["mapping"]
        for shortcut, music in music_mapping.items():
            keyboard.add_hotkey(shortcut, play, [music_path + music])
        keyboard.wait()
