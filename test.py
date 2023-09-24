import unittest
from solution import *
import random
import string


def correct_fib(n):
	"""correct implementation for this test"""
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return correct_fib(n-1) + correct_fib(n-2)

def correct_palindrome(string):
	new_str = ""
	for i in string:
		if i.isalnum():
			new_str += (i)
	return new_str.lower()[::-1] == new_str.lower()

def random_num(n):
	return random.choice([i for i in range(n+1)])

def random_str(n):
	ans = ""
	for i in range(n):
		ans += random.choice(string.ascii_letters)
	return ans


#correct Function for Reverse of a number
def reverse_number(n):
	reversed_num = 0
	while n != 0:
		digit = n % 10
		reversed_num = reversed_num * 10 + digit
		n //= 10
	return reversed_num

# Check whether an year is a leap year of not.
def leap_years(n):
	year = 2000
	if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
		return True;
	else:
		return False;

# find an element in a sorted array

def findelement(arr, n):
	l = 0
	r = len(arr)
	while l <= r:
		mid = l + (r - l) // 2
		if(arr[mid] == n):
			return mid
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return -1
# sum of digit
def sumdigit(n):
	sum = 0
	for digit in str(n): 
		sum += int(digit)      
	return sum

#factorial original
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))

class NthFib(unittest.TestCase):
	def test_1(self):
		"""Test for fib when n = 2"""
		assert 1 == nth_fib(2)
	def test_2(self):
		"""Test for fib when n = 6"""
		assert 5 == nth_fib(6)
	def test_3(self):
		num = random_num(15)
		"""random test 1, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_4(self):
		num = random_num(15)
		"""random test 2, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_5(self):
		num = random_num(15)
		"""random test 3, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_6(self):
		num = random_num(15)
		"""random test 4, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)
	def test_7(self):
		num = random_num(15)
		"""random test 5, expected {num}, actual {nth_fib(num)}"""
		assert correct_fib(num) == nth_fib(num)


class PalindromeChecker(unittest.TestCase):
	def test_2(self):
		"""palindrome("eye") should return true."""
		assert palindrome("eye") == True

	def test_3(self):
		"""palindrome("_eye") should return true."""
		assert palindrome("_eye") == True

	def test_4(self):
		"""palindrome("race car") should return true."""
		assert palindrome("race car") == True

	def test_5(self):
		"""palindrome("not a palindrome") should return false."""
		assert palindrome("not a palindrome") == False

	def test_6(self):
		"""palindrome("A man, a plan, a canal. Panama") should return true."""
		assert palindrome("A man, a plan, a canal. Panama") == True

	def test_7(self):
		"""palindrome("never odd or even") should return true."""
		assert palindrome("never odd or even") == True

	def test_8(self):
		"""palindrome("nope") should return false."""
		assert palindrome("nope") == False

	def test_9(self):
		"""palindrome("almostomla") should return false."""
		assert palindrome("almostomla") == False

	def test_10(self):
		"""palindrome("My age is 0, 0 si ega ym.") should return true."""
		assert palindrome("My age is 0, 0 si ega ym.") == True


class Reverse_Number(unittest.TestCase):
	def test_1(self):
		assert 8808 == reverse(8808)
	def test_2(self):
		"""palindrome("eye") should return true."""
		assert reverse_number(8088) == reverse(8808) 

	def test_3(self):
		"""palindrome("_eye") should return true."""
		assert reverse_number(8088) == reverse(8808)

	def test_4(self):
		"""palindrome("race car") should return true."""
		assert reverse_number(80885) == reverse(58808)

	def test_5(self):
		"""palindrome("not a palindrome") should return false."""
		assert reverse_number(13212) == reverse(21231)

	def test_6(self):
		"""palindrome("A man, a plan, a canal. Panama") should return true."""
		assert reverse_number(92709) == reverse(90729)

	def test_7(self):
		"""palindrome("never odd or even") should return true."""
		assert reverse_number(85627) == reverse(72658)

	def test_8(self):
		"""palindrome("nope") should return false."""
		assert reverse_number(19892) == reverse(29891)

	def test_9(self):
		"""palindrome("almostomla") should return false."""
		assert reverse_number(100001) == reverse(100001)

	def test_10(self):
		"""palindrome("My age is 0, 0 si ega ym.") should return true."""
		assert reverse_number(76002) == reverse(20067)
	

class Leap(unittest.TestCase):
	def test_1(self):
		assert leap_year(1233) == False
	def test_2(self):
		assert leap_year(2022) == False

	def test_3(self):
		assert leap_year(1996) == True

	def test_4(self):
		assert leap_year(2000) == leap_years(2000)

	def test_5(self):
		assert leap_year(1900) == leap_years(1900)

	def test_6(self):
		assert leap_year(0) == leap_years(0)

	def test_7(self):
		assert leap_year(100) == leap_years(100)

	def test_8(self):
		assert leap_year(88) == leap_years(88)

	def test_9(self):
		assert leap_year(1200) == leap_years(1200)

	def test_10(self):
		assert leap_year(88) == leap_years(88)


class Sorted_Array(unittest.TestCase):
	def test_1(self):
		assert findele([1, 2, 3, 4, 5,6], 4) == findelement([1, 2, 3, 4, 5,6], 4)
	def test_2(self):
		assert findele([11, 23, 28, 39, 53, 91, 78], 10) == findelement([11, 23, 28, 39, 53, 91, 78], 10)

	def test_3(self):
		assert findele([10, 29, 32, 77, 87, 101, 212, 309, 728], 309) == findelement([10, 29, 32, 77, 87, 101, 212, 309, 728], 309)

	def test_4(self):
		assert findele([10, 23, 29, 72, 98, 111, 112, 302, 782], 10) == findelement([10, 23, 29, 72, 98, 111, 112, 302, 782], 10)

	def test_5(self):
		assert findele([-2, -3, -1, 2, 8, 1011, 2122912, 3313092, 4437282], -1) == findelement([-2, -3, -1, 2, 8, 1011, 2122912, 3313092, 4437282], -1)

	def test_6(self):
		assert findele([0, 2, 10, 82, 197, 787, 1290, 13092, 17282], 10) == findelement([0, 2, 10, 82, 197, 787, 1290, 13092, 17282], 10)

	def test_7(self):
		assert findele([90, 1293, 3832, 5772, 9387, 143011, 4342912, 1443092, 1247282], 1293) == findelement([90, 1293, 3832, 5772, 9387, 143011, 4342912, 1443092, 1247282], 1293)

	def test_8(self):
		assert findele([1, 1293, 4832, 5772, 9987, 91011, 92912, 93092, 97282], 97282) == findelement([1, 1293, 4832, 5772, 9987, 91011, 92912, 93092, 97282], 97282)

	def test_9(self):
		assert findele([129, 821, 832, 972, 487, 3211, 5912, 27092, 72282], 1323) == findelement([129, 821, 832, 972, 487, 3211, 5912, 27092, 72282], 1323)

	def test_10(self):
		assert findele([192, 228, 302, 875, 901, 933, 1890, 3092, 7282], 1092) == findelement([192, 228, 302, 875, 901, 933, 1890, 3092, 7282], 1092)


class oddEven(unittest.TestCase):
	def test_1(self):
		assert parity(10) == True
	def test_2(self):
		assert parity(25644310) == True
	def test_3(self):
		assert parity(33224111) == False
	def test_4(self):
		assert parity(12422119) == False
	def test_5(self):
		assert parity(10988332) == True
	def test_6(self):
		assert parity(33223310) == True
	def test_7(self):
		assert parity(-123456789) == False
	def test_8(self):
		assert parity(-123942123) == False
	def test_9(self):
		assert parity(0) == True
	def test_10(self):
		assert parity(1) == False

#sum_digit
class Addition(unittest.TestCase):
	def test_1(self):
		assert sum_digit(1233) == sumdigit(1233)
	def test_2(self):
		assert sum_digit(2022) == sumdigit(2022)

	def test_3(self):
		assert sum_digit(1996) != sumdigit(1995)

	def test_4(self):
		assert sum_digit(2000) == 2

	def test_5(self):
		assert sum_digit(1900) == 10

	def test_6(self):
		assert sum_digit(0) == 0

	def test_7(self):
		assert sum_digit(100) == 1

	def test_8(self):
		assert sum_digit(88) == 16

	def test_9(self):
		assert sum_digit(1200) == 3

	def test_10(self):
		assert sum_digit(88) == 16
	

class Factorial(unittest.TestCase):
	def test_1(self):
		assert factorial(5) == facto(5)
	def test_2(self):
		assert factorial(2) == facto(2)

	def test_3(self):
		assert factorial(16) != facto(15)

	def test_4(self):
		assert facto(8) == factorial(8)

	def test_5(self):
		assert facto(9) == factorial(9)

	def test_6(self):
		assert facto(0) == 1

	def test_7(self):
		assert facto(18) == 6402373705728000

	def test_8(self):
		assert facto(7) == 5040

	def test_9(self):
		assert facto(11) == 39916800

	def test_10(self):
		assert facto(1) == 1
	

class ArmStrong(unittest.TestCase):
	def test_1(self):
		assert armstrong(153) == True
	def test_2(self):
		assert armstrong(1) == False

	def test_3(self):
		assert armstrong(16) != True

	def test_4(self):
		assert armstrong(0) == True

	def test_5(self):
		assert armstrong(153) == True

	def test_6(self):
		assert armstrong(99) == False

	def test_7(self):
		assert armstrong(370) == True

	def test_8(self):
		assert armstrong(371) == True

	def test_9(self):
		assert armstrong(5040) == True

	def test_10(self):
		assert armstrong(9474) == True


class NumberSum(unittest.TestCase):
	def test_1(self):
		assert sum(20) == 210
	def test_2(self):
		assert sum(200) == 20100

	def test_3(self):
		assert sum(99) != 490

	def test_4(self):
		assert sum(1) == 1

	def test_5(self):
		assert sum(153) == 11781

	def test_6(self):
		assert sum(100) == 5050

	def test_7(self):
		assert sum(370) == 68635

	def test_8(self):
		assert sum(371) == 69006

	def test_9(self):
		assert sum(504) == 127260

	def test_10(self):
		assert sum(947) == 448878
#"""if __name__ == "__main__":
#	unittest.main()"""
#armstrong --> 54748