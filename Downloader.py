from pytube import YouTube
import os

def Download(link, type):
    if not os.path.exists("results"):
        os.makedirs("results")

    yObject = YouTube(link)
    if type == "MP4":
        yObject = yObject.streams.get_highest_resolution()
        try:
            yObject.download("./results")
        except:
            print("An error has occurred")
        print("Download completed successfully!")
    elif type == "MP3":
        yObject = yObject.streams.filter(only_audio=True).first()
        try:
            outFile = yObject.download("./results")
            base, ext = os.path.splitext(outFile)
            newFile = base + ".mp3"
            os.rename(outFile, newFile)
        except:
            print("An error has occured")
        print("Download completed!")


link = input("Enter the youtube URL you wish to download: ")
type = input("Would you like to download as an MP3 or an MP4? ")
Download(link, type)