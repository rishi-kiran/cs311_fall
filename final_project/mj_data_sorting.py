import json
import random
import sys
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        comparison_number = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > comparison_number:
             arr[j + 1] = arr[j]
             j -= 1
        arr[j + 1] = comparison_number

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i 
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
def read_data():
    f = open('GmSc.json',)
    data = json.load(f)
    return data

def random_data():
    n = 1000
    iterations = 0
    tbubble = []
    tinsertion = []
    tselection = []
    print("Array size", "Bubble", "Insertion", "Selection")
    for i in range(10):
        a = []
        b = []
        c = []
        for i in range(n):
            rand_num = random.randrange(0, n)
            a.append(rand_num)
            b.append(rand_num)
            c.append(rand_num)
        start = time.time()
        bubble_sort(a)
        end = time.time()
        tbubble.append(end - start)
        
        start = time.time()
        insertion_sort(b)
        end = time.time()
        tinsertion.append(end - start)

        start = time.time()
        selection_sort(c)
        end = time.time()
        tselection.append(end - start)

        print(n,"{:.4f}".format(tbubble[iterations]).rjust(14), "{:.4f}".format(tinsertion[iterations]).rjust(7), "{:.4f}".format(tselection[iterations]).rjust(10)) 
        n += 1000
        iterations += 1

time_bubble = []
time_insertion = []
time_selection = []
bubble_arr = []
insertion_arr = []
selection_arr = []
print("Array size, Bubble, Insertion, Selection")
dict = read_data()
game_score = dict["GmSc"]
n = 250
ntime = 0
for i in range(4):
    #for num in game_score:
    for i in range(n):
        num = game_score[i]
        bubble_arr.append(num)
        insertion_arr.append(num)
        selection_arr.append(num)
    start = time.time()
    bubble_sort(bubble_arr)
    end = time.time()
    time_bubble.append(end - start) 

    start = time.time()
    insertion_sort(insertion_arr)
    end = time.time()
    time_insertion.append(end - start)

    start = time.time()
    selection_sort(selection_arr)
    end = time.time()
    time_selection.append(end - start)
    print(n, "{:.4f}".format(time_bubble[ntime]).rjust(14), "{:.4f}".format(time_insertion[ntime]).rjust(7), "{:.4f}".format(time_selection[ntime]).rjust(10))
    ntime+=1
    n+=250
    bubble_arr = []
    insertion_arr = []
    selection_arr = []

random_data()
