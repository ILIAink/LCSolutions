[Problem Description](https://leetcode.com/problems/valid-sudoku/description/)


### Thoughts before looking at solution
Since each row, column, and 3x3 square can not have any repetitions, it would make sense to just use a hashset for every single row, column, and 3x3 square. This would be easy to do for the column and row, but it's not as intuitive for the 3x3 square. *How would the keys be structured?*


### After looking at solution
There is a trick when it comes to storing the keys for the 3x3 squares.
Since we have a 9x9 board, and each square is 3x3, we can simply take the current row, and the current col and divide it by 3. Then we can use that value as a key. So essentially, the key for the squares would be structured like this `squares[(r//3, c//3)]`
Here are some examples:
- board[0][1]
    - 0 / 3 = 0
    - 1 / 3 = 0
    - **Key = (0, 0)**
- board[0][8]
    - 0 / 3 = 0
    - 8 / 3 = 2
    - **Key = (0, 2)**
- board[3][1]
    - 3 / 3 = 1
    - 1 / 3 = 0
    - **Key = (1, 0)**

The way this works, there would be a unique key for every single square.