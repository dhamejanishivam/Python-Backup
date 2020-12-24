from pytube import YouTube

def downloader(url):
    get_video = YouTube(url)
    get_stream = get_video.streams.first()
    get_stream.download("D:\Downloads")


if __name__ == "__main__":
    downloader(input("Enter url of the video \n"))

