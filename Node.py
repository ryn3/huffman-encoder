class NodeInfo:
    def __init__(self, char_=None, freq_=None, bincode_=''):
        self.char = char_
        self.freq = freq_
        self.bincode = bincode_

    def get_bincode(self):
        return 0

    def get_attr(self):
        return (self.char, self.freq, self.bincode)

class Node:
    def __init__(self, node_info_=None):
        self.left = None
        self.right = None
        self.node_info = node_info_ 

    def reorder_tup_list(self, tupList):
        return sorted(tupList, key=lambda x: x[1])

    def create_call_stack(self, dict_):
        tupList = list(dict_.items())
        tupList.reverse()
        output = []
        for item in tupList:
            node = Node(NodeInfo(char_=item[0], freq_=item[1]))
            output.append(node)
        return output

    def reorder(self, node_list):
        temp_list = []
        output_list = []
        for i, node in enumerate(node_list):
            temp_list.append((i, node.node_info.char, node.node_info.freq))
        temp_list = sorted(temp_list, key=lambda x: x[2])
        for node in temp_list:
            output_list.append(node_list[node[0]])
        return output_list

    def create_head(self, node1_, node2_):
        return NodeInfo(char_=node1_.node_info.char + node2_.node_info.char, freq_=node1_.node_info.freq + node2_.node_info.freq)

    def assign(self, node1_, node2_):
        if node1_.node_info.freq < node2_.node_info.freq:
            return node1_, node2_
        elif node1_.node_info.freq >= node2_.node_info.freq:
            return node2_, node1_

    def huffman_fill(self, dict_):
        call_stack = self.create_call_stack(dict_)

        while len(call_stack) > 1:
            current_node = Node()
            node1, node2 = call_stack[0], call_stack[1]
            call_stack = call_stack[2:]
            current_node.node_info = self.create_head(node1, node2)
            current_node.left, current_node.right = self.assign(node1, node2)
            self.node_info, self.left, self.right = current_node.node_info, current_node.left, current_node.right
            call_stack.append(current_node)
            call_stack = self.reorder(call_stack)

    def add_bin_code(self, bincode_=None):
        if self.node_info is None:
            return
        if bincode_ is not None:
            self.node_info.bincode += bincode_
            left_bin_code_ = bincode_ + '0'
            right_bin_code_ = bincode_ + '1'
        else:
            left_bin_code_ = '0'
            right_bin_code_ = '1'
        self.left.add_bin_code(bincode_=left_bin_code_) if self.left is not None else False
        self.right.add_bin_code(bincode_=right_bin_code_) if self.right is not None else False

    def get_bin_dict(self, dict_={}):
        if self.node_info is None:
            return
        if len(self.node_info.char) == 1:
            index = self.node_info.char
            dict_[index] = self.node_info.bincode 
        self.left.get_bin_dict(dict_) if self.left is not None else False
        self.right.get_bin_dict(dict_) if self.right is not None else False
        return dict_
