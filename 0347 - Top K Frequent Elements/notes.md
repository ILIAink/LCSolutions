[Problem Description](https://leetcode.com/problems/top-k-frequent-elements/description/)

We are going to use bucket sort.

- The index will refer to the count (how often it appears)
- The value at that index will be which numbers are at that count

Plan:

- Use a hashmap to count the frequency of each number
- Have a frequency array
- Then iterate through the hashmap and map the number to the frequency (index)
  - For example if `1` appears 3 times
  - Then at `freq[3] = 1`
- Will will go through the `freq` array in reverse order to populate out `res` array, and once we get `k` values we stop the loop and return it.
