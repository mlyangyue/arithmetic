#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
二叉查找树
"""

# 二叉树节点类
class Node(object):

	def __init__(self, value):
		"""

		:param value: 节点的值
		"""
		self.value = value
		self.left = None
		self.right = None

def insert(root,value):
	"""
	为二叉查找数插入值
	:param root: 节点对象
	:param value: 要插入节点对象的值
	:return: 返回节点对象
	"""
	if root is None:
		root = Node(value=value)
	else:
		if value < root.value:
			root.left = insert(root.left,value)
		elif value > root.value:
			root.right = insert(root.right,value)
	return root

def query(root,value):
	"""
	查找值
	:param root:节点对象
	:param value: 查找的值
	:return: 找到返回1 没有返回None
	"""
	if root is None:
		return
	if root.value is value:
		return 1
	if root.value < value:
		return query(root.right, value)
	else:
		return query(root.left, value)

def findmin(root):
	"""
	查找最小节点
	:param root:
	:return: 找到节点对象
	"""
	if root.left:
		return findmin(root)
	else:
		return None

def delnum(root,value):
	"""

	:param root:
	:param value:
	:return:
	"""
	if root is None:
		return
	if root.value > value:
		root = delnum(root.right, value)
	elif root.value < value:
		root = delnum(root.left, value)
	else:
		if root.left and root.right: #左右子树都不为空,当前指针的值为原指针中最小的节点
			'''
			查找右子树最左下节点s
			将节点s的数据域替换到要删除的节点

			'''
			tmp = findmin(root.right)
			root.value = tmp.value
			root.right = delnum(root.right,value)
		else:
			if root.left is None:  # 左子树为None,当前指针指向原来的右子树
				root = root.right
			elif root.right is None:  # 右子树为None,当前指针指向原来的左子树
				root = root.left
			else:
				pass
	return root



if __name__ == '__main__':

	root = Node(10)
	root = insert(root,9)
	root = insert(root,3)
	root = insert(root,8)
	root = insert(root,7)
	root = insert(root,11)
