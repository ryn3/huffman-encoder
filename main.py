from Node import *
import math

def get_dict(string):
    currentDict = {}
    for i in range(0, len(string)):
        if string[i] in currentDict:
            currentDict[string[i]] += 1 
        else:
             currentDict[string[i]] = 1
    return currentDict

def get_bitstream_dict(string_):
    string_dict = get_dict(string_)
    num_chars = len(string_dict)
    num_bits = int(math.ceil(math.log(num_chars, 2)))
    return num_bits    

input_string = "the swiss wristwatch was difficult to maintain"
tree = Node()
tree.huffman_fill(get_dict(input_string))
print(tree)
tree.add_bin_code()
huffman_dict = tree.get_bin_dict()
encoded_string = ''

for char in input_string:
    encoded_string += huffman_dict[char]

print(input_string)
print(len(encoded_string), encoded_string)
print("Compare to ", len(input_string) * get_bitstream_dict(input_string))
print(huffman_dict)