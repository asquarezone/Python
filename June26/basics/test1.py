
class Testable:

    def test(self):
        return "tested"

        
class WebPage(Testable):
    pass



if __name__ == "__main__":
    home = WebPage()
    home.test()