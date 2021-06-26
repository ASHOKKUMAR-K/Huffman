#!/usr/local/bin/python3
import sys
import argparse
# import shutil
import json

class Node:
    def __init__(self, character=None, frequency=None):
        self.left = None
        self.right = None
        self.char = character
        self.freq = frequency
        
    def __str__(self):
        return "{} : {}".format(self.char, self.freq)
    
def get_char_codes(node, char_codes, code):
    if node.left is None and node.right is None:
        char_codes[node.char] = code
    if node.left is not None:
        get_char_codes(node.left, char_codes, code+"0")
    if node.right is not None:
        get_char_codes(node.right, char_codes, code+"1")
        
def create_huffman_tree(nodes):
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq, reverse=True)
        first_least_node = nodes[-1]
        second_least_node = nodes[-2]
        nodes.pop()
        nodes.pop()
        new_node = Node(frequency=first_least_node.freq + second_least_node.freq)
        new_node.left = first_least_node
        new_node.right = second_least_node
        nodes.append(new_node)
    return nodes[0]


def encode(input_file, output_file):
	print("encoding ", input_file, output_file)
	# write code here
	with open("story.txt", "r") as in_file:
		input_string = "".join(in_file.readlines())
	chars_freq = {}

	for char in input_string:
		try:
			chars_freq[char] += 1
		except:
			chars_freq[char] = 1

	nodes = [Node(char, freq) for char, freq in chars_freq.items()]

	root = create_huffman_tree(nodes)

	char_codes = {}

	get_char_codes(root, char_codes, "")
	# print(char_codes)

	encoded_input = ""
	for char in input_string:
		encoded_input += char_codes[char]
	
	with open(output_file, "w+") as out:
		out.write(encoded_input)
	with open("huffman_tree_codes.json", "w") as code_file:
		code_chars = {code:char for char, code in char_codes.items()}
		json.dump(code_chars, code_file)

def decode(input_file, output_file):
	print("decoding ", input_file, output_file)
	# write code here
	with open("huffman_tree_codes.json", "r") as code_file:
		code_chars = json.load(code_file)
	with open(input_file, "r") as in_file:
		encoded_input = in_file.read()
	
	decoded_string = ""
	key = ""
	for bit in encoded_input:
		key += bit
		try:
			decoded_string += code_chars[key]
			key = ""
		except:
			continue
	
	print(decoded_string)
 
	with open(output_file, "w") as out:
		out.write(decoded_string)


def get_options(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Huffman compression.")
	groups = parser.add_mutually_exclusive_group(required=True)
	groups.add_argument("-e", type=str, help="Encode files")
	groups.add_argument("-d", type=str, help="Decode files")
	parser.add_argument("-o", type=str, help="Write encoded/decoded file", required=True)
	options = parser.parse_args()
	return options


if __name__ == "__main__":
	options = get_options()
	if options.e is not None:
		encode(options.e, options.o)
	if options.d is not None:
		decode(options.d, options.o)
