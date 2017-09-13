from random import randint

def generate_list(size):
    l=[]
    for i in range(size):
        l.append(randint(1,size))
    return l

def bubble_sort(lis):
    for i in range(len(lis)):
        for j in range(i, len(lis)):
            if lis[i] > lis[j]:
                lis[i], lis[j] = lis[j], lis[i]
    return lis

def selection_sort(lis):
    for i in range(len(lis)):
        min = i
        for j in range(i, len(lis)):
            if lis[j] < lis[min]:
                min = j
        lis[i], lis[min] = lis[min], lis[i]
    return lis

def insertion_sort(lis):
    for i in range(len(lis)):
        item = lis[i]
        j = i
        while j > 0 and lis[j-1] > item:
            lis[j] = lis[j-1]
            j -= 1
        lis[j] = item
    return lis


if __name__ == '__main__':
    lis = generate_list(100)
    print("\n")
    print("Generated list: ", lis)
    print("\n")
    #lis = selection_sort(lis)
    #lis = bubble_sort(lis)
    lis = insertion_sort(lis)
    print("Sorted list: ", lis)
    print("\n")

