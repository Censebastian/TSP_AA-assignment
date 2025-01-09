import random
import math 

max_nr_nodes = 20
max_nr_edges = max_nr_nodes * (max_nr_nodes - 1)
resolution = 100
no_tests = 20
input_dir = "input/"

class vertex:
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else round(random.uniform(0.0, 100.0), 1)
        self.y = y if y is not None else round(random.uniform(0.0, 100.0), 1)

    def __str__(self):
        return f"{self.x}, {self.y}"

def gen_vertices(): #generate vertices coordinates
    arr = [0 for i in range(max_nr_nodes)]
    for i in range(max_nr_nodes):
        arr[i] = vertex()
    return arr

def calc_dist(vert1, vert2): #calculate distance between two vertices
    delta_x = vert1.x - vert2.x
    delta_y = vert1.y - vert2.y
    return round(math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2)), 1)

def calc_adj_matrix(arr): #calculate every distance between two vertices
    adj_mat = [[0 for i in range(max_nr_nodes)] for j in range(max_nr_nodes)]

    for i in range(max_nr_nodes):
        for j in range(i + 1, max_nr_nodes):
            adj_mat[i][j] = adj_mat[j][i] = calc_dist(arr[i], arr[j])
    return adj_mat

def print_adj_matrix(adj_mat):
    for row in adj_mat:
        for element in row:
            print(element, end=' ')
        print()

def gen_input_files():
    file_name = "input"
    for i in range(no_tests):
        f = open(input_dir + file_name + str(i + 1), 'w')
        f.write(str(max_nr_nodes) + ' ' + str(max_nr_edges) + '\n')
        adj_mat = calc_adj_matrix(gen_vertices())
        for j in range(max_nr_nodes):
            for k in range(j + 1, max_nr_nodes):
                f.write(str(j) + " " + str(k) + " " + str(adj_mat[j][k]) + "\n")
        f.close()
