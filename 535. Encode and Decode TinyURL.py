from urllib.parse import quote, unquote

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encode = quote(longUrl, safe = ":/?=&#")
        return encode

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        decode = unquote(shortUrl)
        return decode
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
