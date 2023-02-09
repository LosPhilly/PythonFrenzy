import pygame

pygame.init()
pygame.mixer.init()

# Load the music file
music_file = "dubstep.mp3"
pygame.mixer.music.load(music_file)

# Play the music
pygame.mixer.music.play()

# Wait for the song to finish
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Quit pygame
pygame.quit()
