from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # i will iterate through the encoded string
        # j will iterate through each individual string
        while (i < len(s)):
            j = i
            while (s[j] != "#"):
                j += 1

            # length will be from the start to before the "#" symbol
            length = int(s[i:j])

            i = j + 1  # place i at the start of the str
            j = i + length  # place j at the start of the next str
            res.append(s[i:j])

            i = j  # repeat the process
        return res
