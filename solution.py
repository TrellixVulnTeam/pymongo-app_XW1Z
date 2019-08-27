n = input()
total_matches = int(n)
match_fees = list(map(int,input().split()))
max_pair_value = 0
max_index = 0

if(len(match_fees) > int(n)):
    print("You have entered fees for more than", n, "matches")
elif(len(match_fees) < total_matches):
    print("Please enter fees for", n, "matches")
else:
    for i in range(total_matches):
        if(i < (total_matches-1)):
            if(max_pair_value < (match_fees[i] + match_fees[i+1])):
                max_pair_value = match_fees[i] + match_fees[i+1]
                max_index = i
            else:
                continue

print("Maximum value pair", max_pair_value)
print("Max index", max_index)

counter1 = 0
counter2 = 0

for i in range(max_index-2, -1, -1):
    print("should not come into this for loop", i)
    if(counter1 == 2):
        counter1 = 0
        continue
    else:
        print("else", match_fees[i])
        counter1 = counter1 + 1
        max_pair_value = max_pair_value + match_fees[i]

for i in range(max_index+3, total_matches):
    print("comes under this", i)
    if(counter2 == 2):
        counter2 = 0
        continue
    else:
        counter2 = counter2 + 1
        max_pair_value = max_pair_value + match_fees[i]

print("Maximum Earnings : ", max_pair_value)