import os
from pytube import YouTube, Playlist

def convert_playlist_to_mp4(playlist_url, output_dir):
    FULL_PATH = os.path.abspath(".")
    PLAYLIST_URL = input("Enter the playlist link: ")

    playlist = Playlist(PLAYLIST_URL)

    path = os.path.join(FULL_PATH, playlist.title)

    if not os.path.isdir(path):
        os.mkdir(path)

    for url in playlist:
        try:
            video = YouTube(url)
            print(f"Downloading {video.title}")

            # check if the file already exists before downloading again
            video_path = os.path.join(path, f"{video.title}.mp4")

            if os.path.isfile(video_path):
                print("Video already exists. Skipping...")
                continue
                
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=path)
            print("Download completed")

        except Exception as e:
            print(f"An error occurred while downloading the video: {e}")