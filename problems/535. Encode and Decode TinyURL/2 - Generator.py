from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


class Codec:
    mapping = ascii_lowercase + ascii_uppercase + digits

    def __init__(self):
        self.url_to_tiny = {}
        self.tiny_to_url = {}

    def encode(self, long_url: str) -> str:
        while long_url not in self.url_to_tiny:
            code = "".join([choice(Codec.mapping) for _ in range(6)])
            if code not in self.url_to_tiny:
                self.url_to_tiny[long_url] = code
                self.tiny_to_url[code] = long_url
        return self.url_to_tiny[long_url]

    def decode(self, short_url: str) -> str:
        return self.tiny_to_url[short_url]
