class Solution(object):
	def findMedianSortedArrays(self,A,B):
		'''
			type num1,num2 List[int]
			rtype float
		'''
		l = len(A)+len(B)
		return self.getKth(A,B,l//2) if l%2 == 1 else (self.getKth(A,B,l//2-1)+self.getKth(A,B,l//2))/2.0

	def getKth(self,A,B,k):
		if len(A)>len(B):
			A,B = B,A
		if not A:
			return B[k]
		if k == len(A)+len(B)-1:
			return max()








public double findMedianSortedArrays(int[] A,int[] B)