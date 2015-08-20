import unittest
import requests


class TestMiscOperations(unittest.TestCase):

	def setUp(self):
		self.base_url = "https://www.calcatraz.com/calculator/api?c=12%2B3"

	def tearDown(self):
		pass

	def test_page_encoding(self):
		"""
		Check the page encoding.
		"""
		link = self.base_url
		trial = requests.get(link)
		print trial.encoding

	def test_check_http_status_code(self):
		"""
		Check HTTP status code for page.
		"""
		link = self.base_url
		trial = requests.get(link)
		print "HTTP Response Code: "
		print trial.status_code


if __name__ == "__main__":
	unittest.main(verbosity=2)
