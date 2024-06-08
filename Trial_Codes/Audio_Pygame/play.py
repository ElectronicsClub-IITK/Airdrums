import pygame
import os
import threading
def play_drum_sound(drum_type, sound_level):
    base_path = "samples\\%s" %(drum_type)  #path of the folder which contains the audio file
    file_name = f"{drum_type}{sound_level}.wav"   #the name of the audio file
    file_path = os.path.join(base_path, file_name)
    print(file_path)
    if os.path.exists(file_path):  #check if the file exists
        pygame.mixer.init()
        sound=pygame.mixer.Sound(file_path)
        sound.play()
    else:
        print("File not found")
        
#making a function which uses multithreading to run multiple audio files together    
def play_sound_thread(drum_type, sound_level):  
    sound_thread = threading.Thread(target=play_drum_sound, args=(drum_type, sound_level))
    sound_thread.start()

if __name__ == "__main__":
    pygame.init()  # Initialize pygame
    while True:  #keeps taking input unless we enter "exit"
        drum_type = input("Enter the type of drum (or 'exit' to quit): ")
        if drum_type.lower() == 'exit':
            break
        sound_level = input("Enter the sound level (0-7): ")
        if sound_level.isdigit() and 0 <= int(sound_level) <= 7:
            play_sound_thread(drum_type, sound_level)  #plays the required audio file
        else:
            print("Invalid sound level. Please enter a number between 0 and 7.")
