# ####################Simplified Algorithm for "Count and Say"#####################
# 1.Base Case
    # - If \( n = 1 \), return "1" since the first term is always "1".
# 2.Recursive Step:
    # - For \( n > 1 \), calculate the previous term by calling `countAndSay(n - 1)`.
# 3.Generating Next Term:
    # - Use a helper function `count_consecutive` to process the previous term:
    #   - Initialize `result` as an empty string.
    #   - Use `count` to track consecutive digits.
    #   - Traverse the string:
    #     - If characters are the same, increase `count`.
    #     - Otherwise, append `"count + digit"` to `result` and reset `count` to 1.
    #   - After the loop, append the last group.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        previous = self.countAndSay(n - 1)
        return self.count_consecutive(previous)

    def count_consecutive(self, s: str) -> str:
        result = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                result += str(count) + s[i-1]
                count = 1
        result += str(count) + s[-1]
        return result
