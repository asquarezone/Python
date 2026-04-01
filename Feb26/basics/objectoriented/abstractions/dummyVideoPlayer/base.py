"""
This module will have base implementations
"""

from abc import abstractmethod


class BaseVideoFormat():
    """This is base video Format
    """

    # decorator
    @abstractmethod
    def play(self):
        """Play the video
        """
    
    @abstractmethod
    def stop(self):
        """Stop the video
        """
