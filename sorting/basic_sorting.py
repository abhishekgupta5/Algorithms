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

if __name__ == '__main__':
    lis = generate_list(100)
    print("\n")
    print("Generated list: ", lis)
    print("\n")
    lis = bubble_sort(lis)
    print("Sorted list: ", lis)
    print("\n")

