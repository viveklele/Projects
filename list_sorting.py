def list_sort(list_):
    for i in range(0, len(list_)):
        list_[i] = int(list_[i])
    for i in range(len(list_)-1, 0, -1):
        for j in range(i):
                if list_[j] < list_[j+1]:
                    temp = list_[j]
                    list_[j] = list_[j+1]
                    list_[j+1] = temp
    print(list_)
    
number_list = input("Enter the number: ").split(", ")
list_sort(number_list)                
