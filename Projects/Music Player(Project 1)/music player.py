import pygame
import os
 
pygame.init()


window_width, window_height = 600, 600
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)


pygame.display.set_caption("Music Player")


music_folder = "C:\\Users\TEJ\Music"


music_files = []
for file in os.listdir(music_folder):
    if file.endswith(".mp3"):
        music_files.append(os.path.join(music_folder, file))


current_index = 0


pygame.mixer.music.load(music_files[current_index])


pygame.mixer.music.play()


def play_next():
    global current_index
    current_index = (current_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_index])
    pygame.mixer.music.play()


def play_previous():
    global current_index
    current_index = (current_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_index])
    pygame.mixer.music.play()


def toggle_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (255, 80, 80)
BUTTON_HOVER_COLOR = (255, 120, 120)
BUTTON_TEXT_COLOR = (255, 255, 255)


font = pygame.font.Font("C:\\Users\TEJ\Downloads\OpenSans-Regular.ttf", 24)


next_button_img = pygame.image.load("C:\\Users\TEJ\Downloads\do2.png")
previous_button_img = pygame.image.load("C:\\Users\TEJ\Downloads\downlo2.png")
pause_button_img = pygame.image.load("C:\\Users\TEJ\Downloads\download (1).jpg")
play_button_img = pygame.image.load("C:\\Users\TEJ\Downloads\download.jpg")
album_cover_img = pygame.image.load("C:\\Users\TEJ\Downloads\photo-1470225620780-dba8ba36b745.jpg")


next_button_img = pygame.transform.scale(next_button_img, (50, 50))
previous_button_img = pygame.transform.scale(previous_button_img, (50, 50))
pause_button_img = pygame.transform.scale(pause_button_img, (50, 50))
play_button_img = pygame.transform.scale(play_button_img, (50, 50))
album_cover_img = pygame.transform.scale(album_cover_img, (300, 300))


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                
                play_next()
            elif event.key == pygame.K_p:
                
                play_previous()
            elif event.key == pygame.K_SPACE:
                
                toggle_pause()

        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if next_button_rect.collidepoint(mouse_pos):
                play_next()
            elif previous_button_rect.collidepoint(mouse_pos):
                play_previous()
            elif pause_button_rect.collidepoint(mouse_pos):
                toggle_pause()

    
    window.fill(BACKGROUND_COLOR)

    
    album_cover_rect = album_cover_img.get_rect(center=(window_width // 2, window_height // 2 - 50))
    window.blit(album_cover_img, album_cover_rect)

    
    next_button_rect = next_button_img.get_rect(topright=(window_width - 20, window_height - 120))
    if next_button_rect.collidepoint(pygame.mouse.get_pos()):
        window.blit(pygame.transform.scale(next_button_img, (55, 55)), next_button_rect)
    else:
        window.blit(next_button_img, next_button_rect)


    previous_button_rect = previous_button_img.get_rect(topleft=(20, window_height - 120))
    if previous_button_rect.collidepoint(pygame.mouse.get_pos()):
        window.blit(pygame.transform.scale(previous_button_img, (55, 55)), previous_button_rect)
    else:
        window.blit(previous_button_img, previous_button_rect)

    
    pause_button_rect = pause_button_img.get_rect(center=(window_width // 2, window_height - 60))
    if pause_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mixer.music.get_busy():
            window.blit(pygame.transform.scale(pause_button_img, (55, 55)), pause_button_rect)
        else:
            window.blit(pygame.transform.scale(play_button_img, (55, 55)), pause_button_rect)
    else:
        if pygame.mixer.music.get_busy():
            window.blit(pause_button_img, pause_button_rect)
        else:
            window.blit(play_button_img, pause_button_rect)

    
    current_music_text = font.render(os.path.basename(music_files[current_index]), True, TEXT_COLOR)
    current_music_text_rect = current_music_text.get_rect(midtop=(window_width // 2, album_cover_rect.bottom + 30))
    window.blit(current_music_text, current_music_text_rect)

    
    pygame.display.flip()


pygame.quit()


 