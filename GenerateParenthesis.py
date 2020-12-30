class Solution:
    """
    DP: 0 = []
        1 = ["()"]
        2 = ["(())", "()()"]
        3 = ["()(())", "(())()", "((()))", "(()())", "()()()"]
    """
    # Put new set of parenthesis:
    #   On either side of the parenthesis block
    #   Outside each set of parenthesis

    def generateParenthesis_dp(self, n):
        dp = [set(), set()]
        dp[0].add("()")

        for _ in range(2, n+1):
            for comb in dp[0]:
                # Append outer parenthesis
                dp[1].add(comb + "()")
                dp[1].add("()" + comb)

                # Append inner parenthesis
                lr = 0
                for i in range(0, len(comb)-1):
                    if comb[i] != "(": continue
                    lr -= 1
                    for j in range(i+1, len(comb)):
                        if comb[j] == "(": lr -= 1
                        if comb[j] == ")": lr += 1
                        if lr == 0: dp[1].add(comb[:i] + "(" + comb[i:j] + ")" + comb[j:])

            dp[0], dp[1] = dp[1], set()

        return sorted(list(dp[0]))

    def generateParenthesis_dp2(self, n):
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                #dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        dp[i] += ['(' + x + ')' + y]
        return dp[n]

    def generateParenthesis_backtrack(self, n):
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:        backtrack(s+'(', left+1, right)
            if right < left:    backtrack(s+')', left, right+1)

        ans = []
        backtrack()
        return ans

s = Solution()
print(s.generateParenthesis_dp2(4))
