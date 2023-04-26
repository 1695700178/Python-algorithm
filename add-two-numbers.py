##
# 给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
# 并且每个节点只能存储一位数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0开头。
# 示例1
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
# 提示：
# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零
# #
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #  添加一个值为0的头节点
        head = ListNode()
        current = head
        carry = 0
        #  遍历l1和l2的所有节点
        while l1 or l2:
            new_node = ListNode()
            #  如果当前节点不为空，则取其值，否则设为0
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            #  计算两数之和以及进位
            curr_sum = num1 + num2 + carry
            if curr_sum > 9:
                new_node.val = curr_sum - 10
                carry = 1
            else:
                new_node.val = curr_sum
                carry = 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current.next = new_node
            current = current.next

            #  如果最后还有进位，则添加一个值为1的节点
        if carry:
            new_node.next = ListNode(1)
        #  返回头节点的下一个节点
        return head.next


problem2 = Solution()
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
# l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

m_list = problem2.addTwoNumbers(l1, l4)
print(m_list.val)
print(m_list.next.val)
print(m_list.next.next.val)
# print(m_list.next.next.next.val)
##
# head = ListNode()
# current = head
# while l1，l2都不为空：
# 	//创建节点
# 	new_node = ListNode()
# 	//赋值
# 	sum = l1.val+l2.val+carry;
# 	if sum>9:
# 		new_node.val = sum - 10
# 		carry = 1
# 	else:
# 		new_node.val = sum
# 		carry = 0
# 	//节点移动
# 	if l1:
# 		l1 = l1.next
# 	if l2:
# 		l2 = l2.next
# 	//节点添加到链表中
# 	current.next = new_node
# 	current = current.next
# //如果最后进位
# if carry:
# 	current.next = ListNode(1)
#
# return head.next
# #
