class Solution:

    # expect items of format f'{str_len}#{str}' 
    # with no delimiter, as prefix len tells us how to incr string cursor

    def encode(self, strs: List[str]) -> str:
        segments = []
        for s in strs:
            segments.append(f'{len(s)}#{s}')
        return ''.join(segments)

    def decode(self, s: str) -> List[str]:
        decoded = []
        while s:
            size, s = s.split('#', 1)
            size = int(size)
            string, s = s[:size], s[size:]
            decoded.append(string)
        return decoded

