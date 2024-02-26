def max_subArray(list_numbers):
    currTotal = 0
    localTotal = 0

    for i in range(elements_number):
        localTotal = localTotal + elements[i]

        if (localTotal < elements[i]):
            localTotal = elements[i]

        if (currTotal < localTotal):
            currTotal = localTotal

    return currTotal


elements = []
#Define una lista

elements_number = int(input("Enter number of elements on the array: "))

for i in range(0,elements_number):
    element = int(input())
    elements.append(element)

#print(elements)
if (elements_number == 0):
    print(0)
if (elements_number == 1):
    print([0])
max_sub_array = max_subArray(elements)
print(max_sub_array)
