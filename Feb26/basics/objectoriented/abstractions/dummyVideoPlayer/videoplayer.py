from base import BaseVideoFormat
from concrete import Mp4, Wav

class VideoPlayer:
    def __init__(self):
        pass

    def play_video(self, video_file:BaseVideoFormat):
        video_file.play()

    def stop_video(self, video_file:BaseVideoFormat):
        video_file.stop()


if __name__ == "__main__":
    rrr_movie = Mp4("RRR")
    my_player = VideoPlayer()
    my_player.play_video(rrr_movie)
    my_player.stop_video(rrr_movie)

    kgf_movie = Wav("KGF")
    my_player.play_video(kgf_movie)