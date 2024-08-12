[Problem Description (Premium)](https://leetcode.com/problems/encode-and-decode-strings/description/)


We need to find a delimiter that would work with any unicode character, for instance, the delimiter of `#` alone would not be enough, because what if a word begins with `#`?

For example:
- *Given List*: `["meow", "Per#ianCat"]`
If the delimiter is `#`, our string will be "meow#Per#ianCat". This is not good because the result will be the following:
- *Output*: `["meow","Per", "ianCat"]`

The solution is to have a delimiter that is both a special character and also the length of each word.
For example:
- *Given List*: `["meow", "Per#ianCat"]`
If the delimiter is the length of each string, followed by a `#` symbol, then we can see where each word begins.
- *Encoded String*: `"4#meow10#Per#ianCat"`

**Decoding the string would be easy**:
- We get the length of the next word using the number and seeing where the `#` symbol appears. 
- Then we use that length to go to the next word and repeat the process


