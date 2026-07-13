

def add(x:int, y:int) -> int:
    """Returns sum of two numbers

    Args:
        x (int): first argument
        y (int): second argument

    Returns:
        int: sum of x, y
    """
    return x + y

class Testable:

    def test(self):
        return "tested"

        
class WebPage(Testable):
    pass



if __name__ == "__main__":
    home = WebPage()
    home.test()