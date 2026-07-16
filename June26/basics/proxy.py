class RealInternet:
    def connect_to(self, website):
        print(f"successfully connected to {website}")


class SchoolNetworkProxy:
    def __init__(self):
        self.real_internet = RealInternet()
        self.blocked_websites = {"facebook.com", "instagram.com", "youtube.com"}

    def connect_to(self, website):
        if website in self.blocked_websites:
            print("access denied")
        else:
            self.real_internet.connect_to(website)


if __name__ == "__main__":
    proxy = SchoolNetworkProxy()
    proxy.connect_to("google.com")
    proxy.connect_to("facebook.com")

