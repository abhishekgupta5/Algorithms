from random import randrange

def quicksort(arr):
    size = len(arr)
    if size<=1:
        return arr
    else:
        pivot = arr.pop(randrange(size))
        lesser = quicksort([x for x in arr if x < pivot])
        greater = quicksort([x for x in arr if x >= pivot])
        #print(lesser + [pivot] + greater)
        return lesser + [pivot] + greater

if __name__ == '__main__':
    array = []
    for i in range(10):
        array.append(randrange(100))

    print("Orignal array: ", array)
    sorted_array = quicksort(array)
    print("Sorted array: ", sorted_array)
