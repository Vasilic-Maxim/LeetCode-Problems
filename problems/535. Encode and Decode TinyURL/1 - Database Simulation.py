class Codec:
    """
    This solution emulates the database that will return the
    if the specific url is assigned to. Juste because the
    number can get pretty big we can make even shorter by
    translating it to base 62 string. The 62 number represents:
    ASCII lower + upper case letters + numbers.
    """

    def __init__(self):
        self.urls = []

    def encode(self, long_url: str) -> str:
        self.urls.append(long_url)
        return "http://tinyurl.com/" + str(len(self.urls) - 1)

    def decode(self, short_url: str) -> str:
        return self.urls[int(short_url.split("/")[-1])]
