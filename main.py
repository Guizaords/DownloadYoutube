from pytube import Playlist, YouTube


def import_list(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        print(f"download do vídeo {video.title}")
        video.streams.get_highest_resolution().download()


def import_video(url):

    video = YouTube(url)
    print(f"download do vídeo {video.title}")
    video.streams.get_highest_resolution().download()
    print("Download concluído")


if __name__ == '__main__':
    url = input("insira a url do video ou da playlist a ser baixada\n")
    if "playslist" in url:
        import_list(url)
    else:
        import_video(url)


