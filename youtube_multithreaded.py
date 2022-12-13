from pytube import YouTube
import moviepy.editor
import os
import threading
import time

# multithreaded downloading and converting
def start(link,i):
    #downloading videos from youtube
    yt = YouTube(link)
    stream = yt.streams.get_by_itag(22)
    stream.download(filename=f'video{i}.mp4')
    #convert video to audio file
    video = moviepy.editor.VideoFileClip(f'video{i}.mp4')
    audio = video.audio
    audio.write_audiofile(f'audio{i}.mp3',logger=None)
    video.close()
    audio.close()
    #deleting the video
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'video{i}.mp4')
    os.remove(path)
i = 1
while True:
    link = input('Enter link or click ENTER to stop: ')
    if link == "":
        while threading.active_count() != 1:
            time.sleep(10)
        break
    t1 = threading.Thread(target=start,args=(link,i))
    t1.start()
    time.sleep(1)
    i += 1