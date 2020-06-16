import string


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def validIPAddress(self, address: str) -> str:
        if address.count('.') == 3 and self.validate_ipv4(address):
            return "IPv4"
        elif address.count(':') == 7 and self.validate_ipv6(address):
            return "IPv6"
        return "Neither"

    def validate_ipv4(self, address: str) -> bool:
        is_decimal = lambda s: s.isdecimal()
        in_range = lambda s: 0 <= int(s) <= 255
        lead_zeros = lambda s: len(s) == len(str(int(s)))
        is_valid = lambda s: is_decimal(s) and in_range(s) and lead_zeros(s)
        return all(map(is_valid, address.split(".")))

    def validate_ipv6(self, address: str) -> bool:
        length = lambda s: 1 <= len(s) <= 4
        hex_digits = lambda s: all(c in string.hexdigits for c in s)
        is_valid = lambda s: length(s) and hex_digits(s)
        return all(map(is_valid, address.split(":")))
