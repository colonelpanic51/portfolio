from pytube import YouTube
import os

def Download(url):

    vid = YouTube(url)
    vid = vid.streams.get_audio_only()

    try:
        out_file = vid.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except:
        print("Error: download unsuccessful")
        Program()


def Program():

    url = input("Enter a valid YouTube url (or 'x' to exit): ")
    prev = url

    try:
        Download(url)
        print("Download successful!")
        Program()
    except:
        if url == 'x' or url == prev:
            quit()
        else:
            print("Error: invalid url")
            print(url)
            Program()

Program()