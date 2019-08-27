n = int(input())
listoffees = list(map(int,input().split()))
listoffeescopy = []
sumlist = []


def calculatemax1():
    max_pair_value = 0
    max_index = 0
    newlist = []
    for i in range(n):
        if(i < (n-1)):
            if(max_pair_value < (listoffees[i] + listoffees[i+1])):
                max_pair_value = listoffees[i] + listoffees[i+1]
                max_index = i
            else:
                continue

    for i in range(max_index, n):
        newlist.append(listoffees[i])
    for i in range(max_index-1):
        newlist.append(listoffees[i])

    max_earnings = 0
    counter = 0
    for i in newlist:
        if(counter == 2):
            counter = 0
            continue
        else:
            counter = counter + 1
            max_earnings = max_earnings + i
    return max_earnings


def calculatemax2():
    listoffeescopy = listoffees.copy()
    listoffeescopy.sort(reverse=True)
    # print(listoffeescopy)
    for i in listoffeescopy:
        index = listoffees.index(i)
        b, bb, f, ff = 0, 0, 0, 0
        if(index == 0):
            b, bb = 0, 0
            f = listoffees[index+1]
            ff = listoffees[index+2]
            if(f==-1 and ff==-1):
                continue
            else:
                sumlist.append(i)
                listoffees[index] = -1
        elif(index == 1):
            bb=0
            b = listoffees[index-1]
            f = listoffees[index+1]
            ff = listoffees[index+2]
            if((b==-1 and f==-1) or (f==-1 and ff==-1)):
                continue
            else:
                sumlist.append(i)
                listoffees[index] = -1
        elif(index == (len(listoffeescopy)-1)):
            f, ff = 0, 0
            b = listoffees[index-1]
            bb = listoffees[index-2]
            if(b==-1 and bb==-1):
                continue
            else:
                sumlist.append(i)
                listoffees[index] = -1
        elif(index == (len(listoffeescopy)-2)):
            f = listoffees[index+1]
            ff = 0
            b = listoffees[index-1]
            bb = listoffees[index-2]
            if((b==-1 and f==-1) or (b==-1 and bb==-1)):
                continue
            else:
                sumlist.append(i)
                listoffees[index] = -1
        else:
            b = listoffees[index-1]
            bb = listoffees[index-2]
            f = listoffees[index+1]
            ff = listoffees[index+2]
            if((b==-1 and f==-1) or (b==-1 and bb==-1) or (f==-1 and ff==-1)):
                continue
            else:
                sumlist.append(i)
                listoffees[index] = -1
    return sum(sumlist)


if(len(listoffees)>n):
    print("You have entered fees for more than", n, "matches")
elif(len(listoffees)<n):
    print("Please enter fees for", n, "matches")
else:
    max1 = calculatemax1()
    max2 = calculatemax2()
    if(max1 >= max2):
        print(max1)
    else:
        print(max2)
    