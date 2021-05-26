''' ----------------第三题--------------------
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


'''
滑动窗口方案：
以abcabcbb为例，a,b,c分别进入list，当遍历第四个字符a时，由于list里已经有了a，所以滑动窗口得到目前最长子串abc
并把滑动窗口重新滑到第四个字符a，并用max俩记录当前最长子串长度为3
'''
from collections import OrderedDict
import sys

class Solution(object):
	#  执行用时：72 ms
	#  内存消耗：12.8 MB
    def lengthOfLongestSubstring(self, s):
        count = 0
        max = 0
        l1 = list()
        for t in s:
            
            if t not in l1:
            	print('%s not in str '%t)
            	l1.append(t)
            	count+=1
            	print('add %s into l1 %s '%(t,l1))
            else:
            	print('%s in str '%t)
                #l1 = l1[l1.index(t)+1:]
            	del l1[0:l1.index(t)+1]
            	print('pop %s in  l1 %s '%(t,l1))
            	l1.append(t)
                #print(l1)
            	if count > max:
            		max = count
            	count = len(l1)
                #print('count',count)
        return (max if max > count else count)

    '''
    执行用时 : 40 ms, 在所有 Python 提交中击败了96.52%的用户
    内存消耗 :13 MB, 在所有 Python 提交中击败了6.06%的用户
    用dict作为滑动窗口，key为字符，value为字符在串中的位置，dict的查找比list的查找缩短一半的时间
    '''
    def lengthOfLongestSubstringByDic(self, s):
        subLen = 0
        start = 0
        end = -1

        l1 = {}
        for index,t in enumerate(s):
           	# l1[t] < star 是针对abba的情况
           	# 第二个b进入时，滑动窗口的头尾指针都指向 第二个b，此时字典里b的value从1更新为2
           	# a:0 的item还在字典里，虽然它已经不在滑动窗口范围里了
           	# 当第二个a进入时，会拿key值去字典里匹配，因为此时滑动窗口内只有b:2, 所以我们期望第二个a是一个没有出现的新值
           	# 但实际，字典里存在的a:0，所以会被匹配出来，因为添加一个判断l1[t] < start，如果匹配出来的值小于start，那么
           	# 这个键值就已经退出了滑动窗口。这种情况下认为第二个a是一个新的key，直接添加到字典里
            if t not in l1 or l1[t] < start:
            	print('%s not in str '%t)
            	l1[t] = index
            	end+=1

            	print('add %s into l1 %s, start=%d, end=%d ,sublen=%d'%(t,l1,start,end,subLen))
            else:
            	print('%s in str '%t)
            	if index == l1[t]+1:
            		#print('index= %s, start=%d, end=%d '%(index,start,end))
            		#print('end-index+1 = %d'%(end-index+1))
            		l1[t] = index
            		print('add %s into l1 %s, start=%d, end=%d '%(t,l1,start,end))
            		subLen = max(subLen, end-start+1)
            		start =index
            		end = index
            		print('find match in sub end, subLen=%d, start=%d,end=%d,sublen=%d'%(subLen,start,end,subLen))
            	else :

            		subLen = max(subLen, end-start+1)
            		start = l1[t]+1
            		end = index
            		l1[t] = index
            		print('add %s into l1 %s, start=%d, end=%d '%(t,l1,start,end))
            		print('find match in head or body, subLen=%d, start=%d,end=%d'%(subLen,start,end))
        print ("sys.getsizeof(l1):", sys.getsizeof(l1))
        return max(subLen, end-start+1)


s1 = Solution()
print(s1.lengthOfLongestSubstringByDic('abba'))
print ("sys.getsizeof(s1):", sys.getsizeof(s1))
# abcabcbb bbbbb pwwkew



'''  ----------------第四题--------------------
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''

class Solution4(object):
	def longestPalindrome(self, s):
		maxLen = 0
		print('find longest str in %s'%s)
		for index, t in enumerate(s):
			print('                s[%d]: %s'%(index,t))
			if index == 0:
				continue
			elif index == len(s)-1:
				break

			for i in range(index):
				print(i)
				count = 0
				if index-(i+1) <=0 or index+(i+1)>len(s)-1:
					break

				print('s[%d]=%s, s[%d]=%s'%(index-(i+1),s[index-(i+1)], index+(i+1), s[index+(i+1)]))
				if s[index-(i+1)] == s[index+(i+1)]:
					count+=1
					print("length +1 ")
				else:
					maxLen = max(maxLen, count)
					print("match for %s complete: %d"%(t,maxLen))

			maxLen = max(maxLen, count)
			print('maxLen for %s : %d'%(t,maxLen))

		return maxLen


s1 = Solution4()
print('************** %d'%s1.longestPalindrome('babad'))



'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
L   C   I   R
E T O E S I I G
E   D   H   N


示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

'''

'''
0   4   8
1 3 5 7 9
2   6   10

0     6      12
1   5 7   11 13
2 4   8 10   14
3     9      15

'''

class solution5:

	'''
	0     6      12
	1   5 7   11 13
	2 4   8 10   14
	3     9      15

	0 1 2 3 4 5组成一个不断重复地v，即singleV 
	singleV = n + n -2 , 行数为3时，singleV=4；行数为4时，singleV=6

	第0行 0/6/12,第一个为0，其余= singleV*j-0 (j=1,2,3...)，如果 singleV*j 大于输入串地长度则结束
	第1行 1/5/7/11/13，第一个为1， 其余=singleV*j-1/singleV*j+1 （j=1,2,3...） 如果大于输入串地长度则结束
	第2行 2/4/8/10/14，第一个为2， 其余=singleV*j-2/singleV*j+2 （j=1,2,3...） 如果大于输入串地长度则结束
	...
	第k行,第一个为k-1， 其余=singleV*j-k/singleV*j+k （j=1,2,3...） 如果大于输入串地长度则结束
	...
	第numRows-1行,第一个为numRows-1， 其余=singleV*j-(numRows-1)/singleV*j+(numRows-1)（j=1,2,3...） 如果大于输入串地长度则结束

	这一步得到地就是输入字符串的下标，
	'''
	def convert(self, s, numRows):
		lenght = len(s)

		singleV = 2*numRows-2
		if singleV == 0 or lenght == 0 :
			return s

		print("length=%d,singleV=%d"%(lenght,singleV))

		output = ''

		for i in range(numRows):
			#每行的第一个，0/1/2/3...
			#最后一行的首位不处理，放到下面for里处理
			if i < numRows-1 and i < lenght-1:
				print()
				output += s[i]
				print('i=%d, output=%s'%(i,output))


			for j in range(lenght*2//singleV):
				print(lenght*2//singleV)
				indexL = singleV*(j+1)-i
				indexR = singleV*(j+1)+i
				print('(j+1)=%d, indexL=%s,indexR=%s'%((j+1),indexL,indexR))
				if i != numRows-1:
					if indexL <= lenght-1:
						output += s[indexL]
						print('+indexL(%s)'%s[indexL])
					
					if indexR <= lenght-1 and indexR != indexL:
						output += s[indexR]
						print('+indexR(%s)'%s[indexR])
				else:
					if (j+1)%2 == 1: #最后一行
						if indexL <= lenght-1:
							output += s[indexL]
							print('last row \n+indexL(%s)'%s[indexL])
						if indexR <= lenght-1 and indexR != indexL:
							output += s[indexR]
							print('+indexR(%s)'%s[indexR])

			print('output=%s'%(output))

		return output

	def convert1(self,s,numRows):
		'''
		L     D     R
		E   O E   I I
		E C   I H   N
		T     S     G

		定义一个三维数组output[3],用来存储三行的字符
		out[0] = LDR
		out[1] = EOEII
		out[2] = ECIHN
		out[3] = TSG
		
		对LEETCODEISHIRING遍历，第一个L，放入out[0],第二个E 放入out[1], 第三个E 放入out[2],第4个E 放入out[3],
		处理第五个字符则反向存到out[2]

		out[0]->out[1]->out[2]->out[3]->out[2]->out[1]->out[0]->out[1]->out[2]->
		
		当前处理第一行和最后一行时，step=-step
		'''

		#index用来指定当前字符输出到哪一行的list
		index,flag = 0,1
		out = ['' for i in range(numRows)]
		if numRows == 1:
			return s

		for c in s:

			#把当前字符加到out[0/1/2/3]里去
			out[index] += c
			#指向下一个输出list,out[]
			index += flag
			if index==0 or index==numRows-1:
				flag = -flag
		str = ''.join(out)
		return str

s5 = solution5()
print('************** %s'%s5.convert1('ab',1))


'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0
1534236469

'''
class solution6:
	def reverse(self,x):
		out = str(abs(x))[-1::-1]
		if x < 0:
			out = '-'+out

		rv = int(out)
		if rv > 2**31 -1 or rv < -2**31:
			return 0

		return rv

	def reverse1(self,x):
		flag = 1 if x >0 else 0
		x = abs(x)
		out = 0
		v = 0
		while x > 10:
			v = x % 10
			x = x / 10
			out = out*10 + v

			print('v=%d, x=%d, out=%d'%(v,x,out))

		out = int(out*10 + x)
		print('x=%d, out=%d'%(x,out))
		if flag == 0:
			out = 0 - out

		if out > 2**31 -1 or out < -2**31:
			return 0
		return out

			

s6 = solution6()
print('solution6************** %s'%s6.reverse1(1534236469))