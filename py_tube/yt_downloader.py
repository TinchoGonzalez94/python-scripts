## Necesita instalar pytube
## pip install pytube
## desde consola: python -c "from yt_downloader import yt_download; yt_download('https://www.youtube.com/watch?v=EMlM6QTzJo0','.')"
from pytube import YouTube

def yt_download(link,path="."):
    ytob=YouTube(link)
    ytob= ytob.streams.get_highest_resolution()
    try:
        ytob.download(path)
    except:
        print("There has been an error")
    print("Descarga exitosa en "+path)
