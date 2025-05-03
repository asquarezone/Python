"""This module has necessary base classes
"""
from abc import abstractmethod, ABC

class BaseCalculator(ABC):
    
    @abstractmethod
    def calculate(self):
        """This method will perform calculations and respond 
        with a result
        """