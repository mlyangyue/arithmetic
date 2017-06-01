#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
二分查找算法
用非递归和递归2中方式
"""

"""非递归二分查找"""


def binarychop(subsequeue, elem):
	"""

	非递归二分查找
	:param subsequeue 原始可迭代对象
	:param elem 查找元素
	:return 查找到返回对应的下标,没找到返回-1
	"""
	if not subsequeue:
		return -1
	left = 0
	right = len(subsequeue)
	while left <= right:
		middle = (left + right) / 2
		if middle>=len(subsequeue):
			return -1
		middle_value = subsequeue[middle]
		if middle_value == elem:
			return middle
		elif middle_value > elem:
			right = middle - 1
		else:
			left = middle + 1
	return -1


"""递归方法二分查找"""


def binarychop_recursion(subsequeue, left, right, elem):
	"""

	:param subsequeue: 原始可迭代对象
	:param left: subsequeue的第一个下标
	:param right:subsequeue的最后一个下标
	:param elem:要查找的值
	:return:查找到返回对应的下标,没找到返回-1
	"""
	if not subsequeue:
		return -1
	if left <= right:
		middle = (left + right) / 2
		if middle >= len(subsequeue):
			return -1
		middle_value = subsequeue[middle]
		if middle_value == elem:
			return middle
		elif middle_value > elem:
			return binarychop_recursion(subsequeue, left, middle - 1, elem)
		else:
			return binarychop_recursion(subsequeue, middle + 1, right, elem)
	else:
		return -1


if __name__ == "__main__":
	subsequeue = range(1, 100, 2)
	elem = 10
	# index = binarychop(subsequeue, 10) # 非递归二分查找

	index = binarychop_recursion(subsequeue, 0, len(subsequeue), 11) # 递归二分查找
	if index != -1:
		print subsequeue[index], index
	else:
		print 'elem not in subsequeue'
