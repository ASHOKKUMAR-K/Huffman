# Test functions goes here
import unittest

from huffman import encode, decode

class TestHuffman(unittest.TestCase):
	# write all your tests here
	# function name should be prefixed with 'test'
	def test_encode_decode_1(self):
		assert self.assertEqual("ASDFGHJKJHGFDERTYUJNBVCFDRGHBVCSDFJMN", decode(encode("ASDFGHJKJHGFDERTYUJNBVCFDRGHBVCSDFJMN")))
	
	
	def test_encode_decode_2(self):
		assert self.assertEqual("ASDFGHJKJHGFDE sjbkcdvc dbvh! DRGHBVCSDFJMN", decode(encode("ASDFGHJKJHGFDE sjbkcdvc dbvh! DRGHBVCSDFJMN")))


if __name__ == '__main__':
	unittest.main()
