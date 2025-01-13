import gen_input, held_karp, simple_alg
import time
import matplotlib.pyplot as plt

def test_alg(alg, adj_mat):
    start_time = time.time()
    alg(adj_mat)
    end_time = time.time()
    return end_time - start_time

def input_to_mat(in_file):
    f = open(in_file, 'r')
    first_line = f.readline().strip()
    first_line = list(map(int, first_line.split()))
    nr_nodes = first_line[0]
    nr_edges = first_line[1]

    matrix = [[0 for _ in range(nr_nodes)] for _ in range(nr_nodes)]
    for line in f:
        line = list(line.split())
        node_a = int(line[0])
        node_b = int(line[1])
        cost = float(line[2])
        matrix[node_a][node_b] = matrix[node_b][node_a] = cost

    return matrix

def test_hk():
    nr_tests = gen_input.nr_tests
    input_dir = gen_input.input_dir
    duration_arr = []
    for i in range(nr_tests):
        in_file = input_dir + "input" + str(i + 1)
        adj_mat = input_to_mat(in_file)
        duration_arr.append(test_alg(held_karp.held_karp, adj_mat))
    return duration_arr

def test_nn():
    nr_tests = gen_input.nr_tests
    input_dir = gen_input.input_dir
    duration_arr = []
    for i in range(nr_tests):
        in_file = input_dir + "input" + str(i + 1)
        adj_mat = input_to_mat(in_file)
        duration_arr.append(test_alg(simple_alg.tsp, adj_mat))
    return duration_arr

def simple_test():
    gen_input.change_nr_nodes(20)
    gen_input.gen_input_files()
    test_nn()
    test_hk()

def duration_array(test_func):
    dur_arr= []
    for i in range(10, 21):
        gen_input.change_nr_nodes(i)
        gen_input.gen_input_files()
        durations = test_func()
        average = sum(durations) / len(durations)
        dur_arr.append(average)
    return dur_arr

def run_alg(alg):
    nr_tests = gen_input.nr_tests
    input_dir = gen_input.input_dir
    distance_arr = []
    for i in range(nr_tests):
        in_file = input_dir + "input" + str(i + 1)
        adj_mat = input_to_mat(in_file)
        distance_arr.append(alg(adj_mat))
    return distance_arr 

def dist_percentage(test_func1, test_func2):
    dist_mat = []
    dist_arr1 = []
    dist_arr2 = []
    for i in range(10, 21):
        gen_input.change_nr_nodes(i)
        gen_input.gen_input_files()

        dist1 = run_alg(test_func1)
        dist2 = run_alg(test_func2)

        dist_arr1.append(sum(dist1) / len(dist1))
        dist_arr2.append(sum(dist2) / len(dist2))
    dist_mat.append(dist_arr1)
    dist_mat.append(dist_arr2)
    return dist_mat

def distance_array(test_func1, test_func2):
    distances = []

    dist1 = run_alg(test_func1)
    dist2 = run_alg(test_func2)

    distances.append(dist1)
    distances.append(dist2)

    return distances

def plot_dur(in_file):
    f = open(in_file, "r")
    dur_arr_nn = list(map(float, f.readline().strip().split()))
    dur_arr_hk = list(map(float, f.readline().strip().split()))

    indexes = list(range(10, 21))

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(indexes, dur_arr_nn, marker='o', linestyle='-', color='b')
    axs[0].set_ylabel("duration (seconds)")
    axs[0].set_xlabel("nummber of nodes")
    axs[0].set_title("nearest_neighbour")

    axs[1].plot(indexes, dur_arr_hk, marker='o', linestyle='-', color='b')
    axs[1].set_ylabel("duration (seconds)")
    axs[1].set_xlabel("nummber of nodes")
    axs[1].set_title("held_karp")

    plt.tight_layout()
    plt.show()

def plot_dist(hk_dist, nn_dist):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    max_value = max(max(hk_dist), max(nn_dist))  # Determine the maximum value for scaling
    min_value = min(min(hk_dist), min(nn_dist))  # Determine the minimum value for scaling

    axs[0].bar(range(len(nn_dist)), nn_dist, color='blue', alpha=0.7)
    axs[0].set_ylabel("Total Cost")
    axs[0].set_title("Nearest Neighbour")
    axs[0].grid(axis='y', linestyle='--', alpha=0.6)
    axs[0].set_xticks([])
    axs[0].set_ylim(min_value, max_value)

    axs[1].bar(range(len(hk_dist)), hk_dist, color='green', alpha=0.7)
    axs[1].set_ylabel("Total Cost")
    axs[1].set_title("Held-Karp")
    axs[1].grid(axis='y', linestyle='--', alpha=0.6)
    axs[1].set_xticks([])
    axs[1].set_ylim(min_value, max_value)

    plt.tight_layout()
    plt.show()

def output_test_results(out_file):
    f = open(out_file, 'w')
    nn_dur = duration_array(test_nn)
    for element in nn_dur:
        f.write(str(element) + ' ')
    f.write("\n")
    hk_dur = duration_array(test_hk)
    for element in hk_dur:
        f.write(str(element) + ' ')

def run_algs():
    gen_input.change_nr_nodes(20)
    arr = gen_input.gen_vertices()
    mat = gen_input.calc_adj_matrix(arr)
    simple_alg.tsp(mat)
    held_karp.held_karp(mat)

def calc_percentages(arr1, arr2):
    perc_arr = []
    for i in range(len(arr1)):
        perc_arr.append((arr2[i] - arr1[i]) * 100 / arr2[i])

    return perc_arr

def display_table(data, column_labels, row_labels):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.axis("tight")
    ax.axis("off")

    table = ax.table(
        cellText=data,
        colLabels=column_labels,
        rowLabels=row_labels,
        cellLoc="center",
        loc="center",
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(column_labels))))

    plt.show()

column_labels = list(range(10, 21))
row_labels = ["Held-Karp", "Nearest neighbor", "Difference(%)"]

mat = dist_percentage(held_karp.held_karp, simple_alg.tsp)
mat.append(calc_percentages(mat[0], mat[1]))

mat = [[round(element, 2) for element in row] for row in mat]

display_table(mat, column_labels, row_labels)
