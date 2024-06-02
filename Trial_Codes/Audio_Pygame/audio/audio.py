from pygame import mixer
import threading
import time
#tone value should be in range(1,7)
#drum_name can be anything from the list [crash,hithats,hitoms,Iotoms,ride,snare]
def audio_play(drum_name,tone):
    mixer.init()
    sound="audio\\"+drum_name+"\\"+drum_name+tone+ ".wav" #sounds are present in folder called audio in working directory
    mixer.music.load(sound)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(1)
   
if __name__ == "__main__":
    while True:
        drum_names=["snare", "hitoms"]
        tone="7"
        audios = []
        for drum_name in drum_names:
            audio=threading.Thread(target=audio_play,args=(drum_name,tone))        
            audio.start()
            print(f"Active Connection : {threading.active_count()}")
            time.sleep(1)
            audios.append(audio)

        for audio in audios:
            audio.join()
        
# if __name__ == "__main__":
#     # List of drum names and tones for testing
#     drum_names = ["ride","crash"]
#     tones = ["7"]

#         # Create threads for each combination of drum name and tone
#     threads = []
#     for drum_name in drum_names:
#         for tone in tones:
#             thread = threading.Thread(target=audio_play, args=(drum_name,tone))
#             thread.start()
#             print(f"Active Connection : {threading.active_count()}")
#             threads.append(thread)
 
#     # Wait for all threads to complete
#     for thread in threads:
#         thread.join()

#     print("All sounds played.")
