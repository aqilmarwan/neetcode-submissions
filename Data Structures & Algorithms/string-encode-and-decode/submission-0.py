class Solution:

    def encode(self, strs: list[str]) -> str:
        # Join each string with its length and a delimiter `#` as prefix
        encoded_string = ''.join(f'{len(s)}#{s}' for s in strs)
        return encoded_string

    def decode(self, s: str) -> list[str]:
        i = 0
        decoded = []
        
        # Process the encoded string
        while i < len(s):
            # Find the position of the delimiter to get the length
            j = s.find('#', i)
            length = int(s[i:j])  # Extract the length
            i = j + 1  # Move past the `#` character
            decoded.append(s[i:i + length])  # Extract the string of the given length
            i += length  # Move the index to the next encoded part
        
        return decoded
