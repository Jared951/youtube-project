import os
from pytube import YouTube, Playlist

def convert_playlist_to_mp4(playlist_url, output_dir):
    playlist = Playlist(playlist_url)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    success = True  # Initialize success status as True

    for url in playlist:
        try:
            video = YouTube(url)
            print(f"Downloading {video.title}")

            # Check if the file already exists before downloading again
            video_path = os.path.join(output_dir, f"{video.title}.mp4")

            if os.path.isfile(video_path):
                print("Video already exists. Skipping...")
                continue

            stream = video.streams.get_highest_resolution()
            stream.download(output_path=output_dir)
            print("Download completed")

        except Exception as e:
            print(f"An error occurred while downloading the video: {e}")
            success = False  # Set success status to False on error

    return success  # Return the final success status