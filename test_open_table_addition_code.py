import unittest
import os
import requests
import json

class TestCalcAPI(unittest.TestCase):

	def setUp(self):
		self.base_url = "https://www.calcatraz.com/calculator/api?"


	def tearDown(self):
		pass


	def test_add_check(self):
		"""
		Test to check addition of two positive small numbers.
		"""
		link = self.base_url
		add_api = "c=2%2B6"
		link += add_api
		trial = requests.get(link)
		print "\nAnswer from link: " + str(trial.json())
		self.assertEqual(trial.json(), 8)
		print "Test Passed."


	def test_add_both_negative_numbers(self):
		"""
		Test to check addition of two negative numbers.
		"""
		link = self.base_url
		add_api = "c=-2%2B-5"
		link += add_api
		trial = requests.get(link)
		try:
			trial.json()
		except Exception as e:
			print "No answer available from the requested URL..."
			print "Exception Caught:"
			print e
		finally:
			print "\nAnswer from link: " + str(trial.json())
			self.assertEqual(trial.json(), -7)


	def test_add_first_negative_number(self):
		"""
		Test to add two numbers. First number is negative and
		second number is positive.
		"""
		link = self.base_url
		add_api = "c=-2%2B5"
		link += add_api
		trial = requests.get(link)
		try:
			trial.json()
		except Exception as e:
			print "No answer available from the requested URL..."
			print "Exception Caught:"
			print e
		finally:
			print "\nAnswer from link: " + str(trial.json())
			self.assertEqual(trial.json(), 3)


	def test_add_second_negative_number(self):
		"""
		Test to add two numbers. First number is positive and
		second number is negative.
		"""
		link = self.base_url
		add_api = "c=9%2B-5"
		link += add_api
		trial = requests.get(link)
		try:
			trial.json()
		except Exception as e:
			print "No answer available from the requested URL..."
			print "Exception Caught:"
			print e
		finally:
			print "\nAnswer from link: " + str(trial.json())
			self.assertEqual(trial.json(), 4)


	def test_add_all_zeroes(self):
		"""
		Test add two zeroes to check result.
		"""
		link = self.base_url
		add_api = "c=0%2B0"
		link += add_api
		trial = requests.get(link)
		try:
			trial.json()
		except Exception as e:
			print "No answer available from the requested URL..."
			print "Exception Caught:"
			print e
		finally:
			print "\nAnswer from link: " + str(trial.json())
			self.assertEqual(trial.json(), 0)	


	def test_add_with_second_num_as_zero(self):
		"""
		Test to add a number with zero as the second number.
		"""
		link = self.base_url
		add_api = "c=7%2B0"
		link += add_api
		trial = requests.get(link)
		try:
			trial.json()
		except Exception as e:
			print "No answer available from the requested URL..."
			print "Exception Caught:"
			print e
		finally:
			print "\nAnswer from link: " + str(trial.json())
			self.assertEqual(trial.json(), 7)	


	def test_add_first_num_as_zero(self):
		"""
		Test to add a number with zero as the first number.
		"""
		link = self.base_url
		add_api = "c=0%2B1"
		link += add_api
		trial = requests.get(link)
		try:
			trial.json()
		except Exception as e:
			print "No answer available from the requested URL..."
			print "Exception Caught:"
			print e
		finally:
			print "\nAnswer from link: " + str(trial.json())
			self.assertEqual(trial.json(), 7)	


	def test_add_big_numbers(self):
		"""
		Test to check addition of big numbers work as expected.
		"""
		link = self.base_url
		add_api = "c=999999999%2B1"
		link += add_api
		trial = requests.get(link)
		print "\nAnswer from link: " + str(trial.json())
		self.assertEqual(trial.json(), 1.00000E+9)
		print "Test Passed."


	def test_blanks(self):
		"""
		Test to check addition when passing blanks in place of numbers.
		"""
		link = self.base_url
		add_api = "c=%2B"
		link += add_api
		trial = requests.get(link)
		match = re.search(r'c=(.*)%2B(.*)', add_api)
		first_value = match.group(1)
		second_value = match.group(2)
		if (len(first_value) == 0) and (len(second_value) == 0):
			print "Empty Values. Cannot add."
			print "Test Failed."
		

	def test_leave_first_field_blank(self):
		"""
		Test to check addition leaving the first field blank.
		"""	
		link = self.base_url
		add_api = "c=%2B7"
		link += add_api
		trial = requests.get(link)
		print "\n Answer from the link: " + str(trial.json())
		self.assertEqual(trial.json(), 7)
		print "Shows only the second number. Need the first number to calculate addition."
		raise AssertionError


	def test_leave_second_field_blank(self):
		"""
		Test to check addition leaving the second field blank.
		"""	
		link = self.base_url
		add_api = "c=9%2B0"
		link += add_api
		trial = requests.get(link)
		print "\n Answer from the link: " + str(trial.json())
		self.assertEqual(trial.json(), 9)
		print "Shows only the second number. Need the second number to calculate addition."
		raise AssertionError


	def test_add_special_characters(self):
		"""
		Test case to pass special characters for addition.
		"""
		link = self.base_url
		add_api = "c=$$$%2B###"
		match = re.search(r'c=(.*)%2B(.*)', add_api)
		first_value = match.group(1)
		second_value = match.group(2)
		self.assertTrue(first_value.isdigit() and second_value.isdigit(), msg = \
			'Cannot add special characters!')
		print "Test Failed"


	def test_add_alphabets(self):
		"""
		Test case to pass alphabets for addition.
		"""
		link = self.base_url
		add_api = "c=foo%2Bbar"
		match = re.search(r'c=(.*)%2B(.*)', add_api)
		first_value = match.group(1)
		second_value = match.group(2)
		self.assertTrue(first_value.isdigit() and second_value.isdigit(), msg = \
			'Cannot add aphabets characters!')
		print "Test Failed"

	def test_change_addition_operation(self):
		"""
		Test to change the addition operator in URL
		to something else.
		"""
		trial = requests.get("https://www.calcatraz.com/api?c=5%3B7")
		print trial.json()

if __name__ == "__main__":
	unittest.main(verbosity=2)