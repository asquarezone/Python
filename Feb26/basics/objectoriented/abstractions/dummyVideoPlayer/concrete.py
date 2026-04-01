from base import BaseVideoFormat

class Mp4(BaseVideoFormat):
    def __init__(self, movie_name:str):
        self.movie_name = movie_name

    def play(self):
        print(f"Mp4 is playing {self.movie_name}")
    
    def stop(self):
        print("Mp4 is stopped")


class Wav(BaseVideoFormat):
    def __init__(self, movie_name:str):
        self.movie_name = movie_name

    def play(self):
        print(f"Wav is playing {self.movie_name}")
    
    def stop(self):
        print("Wav is stopped")