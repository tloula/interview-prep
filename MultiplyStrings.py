class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        for i in range(len(num2)-1, -1, -1):
            carry, build = 0, []
            for j in range(len(num1)-1, -1, -1):
                prod = int(num1[j]) * int(num2[i])
                build = [(prod + carry) % 10] + build
                carry = (prod + carry) // 10
            if carry: build = [carry] + build
            product += int("".join(list(map(str, build + [0] * (len(num2) - 1 - i)))))
        return str(product)

s = Solution()
nums = ["123456789", "987654321"]

res = int(s.multiply(nums[0], nums[1]))
ans = int(nums[0]) * int(nums[1])

print("RES:", res)
print("ANS:", ans)
print("MATCH:", ans == res)
