#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
二分查找算法
用非递归和递归2中方式
二分查找算法,用递归和非递归2种方式实现,如果理解递归思想,使用递归代码更简洁,思路更清晰
思想:
首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；
否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。
重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
优缺点
优点是比较次数少，查找速度快，平均性能好；
其缺点是要求待查表为有序表，且插入删除困难。
因此，折半查找方法适用于不经常变动而查找频繁的有序列表

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
	right = len(subsequeue)-1
	while left <= right:
		middle = left + (right-left) / 2
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
		middle = left + (right - left) / 2
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
	elem = 11
	# index = binarychop(subsequeue, elem) # 非递归二分查找

	index = binarychop_recursion(subsequeue, 0, len(subsequeue)-1, elem) # 递归二分查找
	if index != -1:
		print subsequeue[index], index
	else:
		print 'elem not in subsequeue'
