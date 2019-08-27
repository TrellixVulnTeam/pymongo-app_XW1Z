n = input()
total_matches = int(n)
match_fees = list(map(int,input().split()))

def calculatemax1():
    max_pair_value = 0
    max_index = 0
    newlist = []
    for i in range(total_matches):
        if(i < (total_matches-1)):
            if(max_pair_value < (match_fees[i] + match_fees[i+1])):
                max_pair_value = match_fees[i] + match_fees[i+1]
                max_index = i
            else:
                continue

    for i in range(max_index, total_matches):
        newlist.append(match_fees[i])
    for i in range(max_index-1):
        newlist.append(match_fees[i])

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

if(len(match_fees) > int(n)):
    print("You have entered fees for more than", n, "matches")
elif(len(match_fees) < total_matches):
    print("Please enter fees for", n, "matches")
else:
    max1 = calculatemax1()
    print(max1)
