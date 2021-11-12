import random
import string
class Node():
    def __init__(self, name):
        self.children = []
        self.children_connection_weights = []
        #for i in range(3): 
        #self.node_name = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        self.node_name = name

    def make_children(self, current_layer, nodes_per_layer_map):
        if current_layer == len(nodes_per_layer_map):
            return
        for i in range(nodes_per_layer_map[current_layer]):
            if (current_layer == 0):
                self.children.append(Node('Input layer node' + str(i + 1)))
            elif(current_layer == 1):
                self.children.append(Node('Hidden layer node' + str(i + 1)))
            else:
                self.children.append(Node('Output layer node' + str(i + 1)))
        first_born = self.children[0]
        first_born.make_children(current_layer + 1, nodes_per_layer_map)

        for i in range(1, len(self.children)):
            self.children[i].children = first_born.children[:]

    def adjust_child_weights(self):
        if len(self.children) == 0:
            return
        self.children_connection_weights = []
        for i in range(len(self.children)):
            self.children_connection_weights.append(random.uniform(0, 1))
            self.children[i].adjust_child_weights()

    def output_children(self, layer):
        indent = '     ' * layer
        if len(self.children) == 0:
            print(f"{indent}{self.node_name}")
            return
        print(f"{indent}{self.node_name} is connected to ")

        for i in range(len(self.children)):
            self.children[i].output_children(layer+1)
            if i < len(self.children_connection_weights):
                print(f"{indent}with weight {self.children_connection_weights[i]} ")

my_first_node = Node('Master node')
NODE_COUNT_PER_LAYER = [4, 3, 2] 
my_first_node.make_children(0, NODE_COUNT_PER_LAYER)
my_first_node.output_children(0)

print("!! Set Weights !!")
my_first_node.adjust_child_weights()
my_first_node.output_children(0)
