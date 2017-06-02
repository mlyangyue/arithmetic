#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
旋转数组查找,有序，本能想到用二分查找
思路:
获取数组元素的分割点,时间复杂度为O(log(n))
比较待查找元素与第一个元素，如果待查找元素大于等于第一个元素，表明待查找元素在前半段有序数组中；如果不是这待查找元素在后半段数组中
判断待查找元素所在的有序数组以后,用二分查找找出元素位置
"""

def search_v1(array, elem):

	if not array:
		return -1
	left = 0
	right = len(array) - 1
	while left <= right:
		middle = left + (right - left)/2
		if array[middle] == elem:
			return middle
		elif array[middle] >= array[left]:
			if array[left] <= elem and array[middle] >= elem: # 左边有序在左边找
				right = middle - 1
			else:
				left = middle + 1
		else:
			if array[right] >= elem and array[middle] <= elem: # 又边有序在右边找
				left = middle + 1
			else:
				right = middle - 1
	return -1




if __name__ == "__main__":
	subsequeue = [11,1,2,3,4,5,6,7,8,9]
	elem = 9
	index = search_v1(subsequeue, elem)
	if index != -1:
		print subsequeue[index], index
	else:
		print 'elem not in subsequeue'

