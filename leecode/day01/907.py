"""
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。

示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
示例 2：

输入：arr = [11,81,94,43,3]
输出：444


提示：

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""


class Solution:
    def sumSubarrayMins(self, arr: list):
        n = len(arr)
        mod = 10 ** 9 + 7
        stack = []
        left, right = [0] * n, [0] * n

        # 计算每个元素左边第一个小于它的元素的位置
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # 清空栈
        stack = []

        # 计算每个元素右边第一个小于它的元素的位置
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # 计算每个元素作为最小值时的子数组数量
        result = 0
        for i in range(n):
            result = (result + arr[i] * (i - left[i]) * (right[i] - i)) % mod

        return result


if __name__ == '__main__':
    so = Solution()
    print(so.sumSubarrayMins([1, 2, 3]))
