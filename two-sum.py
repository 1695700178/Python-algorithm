##
# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，
# 并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
from typing import List


# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
# 提示：
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案
# #
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        """
        global i, j, n
        n = len(nums)
        m_list = []
        for i in range(n):
            for j in range(i, n):
                if i != j and nums[i] + nums[j] == target:
                    m_list.append(i)
                    m_list.append(j)
                    break
        return m_list


problem1 = Solution()
m_list = problem1.twoSum([2, 7, 11, 15], 9)
print(m_list)
