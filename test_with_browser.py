from selenium import webdriver
import unittest

class TestWithBrowser(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()


	def test_with_browser(self):
		"""
		Test with a browser to check simple addition operation.
		"""
		browser = self.browser
		browser.get("http://calcatraz.com/calculator/api?c=2%2B5")
		value = browser.find_element_by_xpath("/html/body").text
		print "Answer from browser: " + str(value)

	def test_negative_browser_test(self):
		"""
		Test with a browser to check a negative condition.
		"""
		browser = self.browser
		browser.get("http://calcatraz.com/calculator/api?c=ab2%2B5qa")
		value = browser.find_element_by_xpath("/html/body").text
		# Prints the value shown in the browser page.
		print "Answer from browser: " + value
		
	
	def tearDown(self):
		self.browser.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)