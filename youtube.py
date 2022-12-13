from pytube import YouTube
import moviepy.editor
import os
import requests




def start():
    #downloading videos from youtube
    link = input('Enter your link: ')
    try:
        yt = YouTube(link) #video link
        stream = yt.streams.get_by_itag(22) #choose by tag which format we want to download.
        stream.download(filename='video.mp4')  # uploading video.
    except:
        print('Invalid url')
        return start()

    #Convert video to audio file
    video = moviepy.editor.VideoFileClip('video.mp4') #select the video to create its audio
    audio = video.audio
    audio.write_audiofile('my_audio.mp3') #record audio from the video into the audio file my_audio.mp3
    video.close()
    audio.close()

    #deleting the video
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'video.mp4')
    os.remove(path)
start()



