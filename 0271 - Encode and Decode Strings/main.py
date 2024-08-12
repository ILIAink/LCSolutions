from typing import List


class Solution:
   def encode(self, strs: List[str]) -> str:
       res = ""
       for s in strs:
            res += f"{len(s)}#{s}"
       return res

   def decode(self, s: str) -> List[str]:
       res = []
       i = 0

       while i < len(s):
            j = i

            while (s[j] != "#"):
                j += 1
            # The number will be from i (the beginning) until before we hit j (the # sign)
            length = int(s[i:j])  # the length of the next word

            i = j + 1  # adjust i so it begins at the next work
            j = i + length  # adjust j so it is at the start of the new word
            res.append(s[i:j])
            i = j

       return res
