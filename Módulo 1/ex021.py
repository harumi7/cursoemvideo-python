import pygame

musica = input('Escolha uma música: \n'
               '[1] long story short\n'
               '[2] Better than Revenge\n'
               '-> ')
if musica == '1':
    musica = 'ex021_song1.mp3'
elif musica == '2':
    musica = 'ex021_song2.mp3'
pygame.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
input()
pygame.event.wait()
