def sort(array):
    for i in range(len(array)-1):
        for b in range(len(array)-1):
            print(f"{b}) {array}")
            if array[b] != array[b+1]:
                array[b], array[b+1] = array[b+1], array[b]
