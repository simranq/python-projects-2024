'''
heights = [145, 151,163,178,159]
#max = 0
total_height = 0
for height in heights :
    total_height += height
print(f"total_height = {total_height}")

total = 0
for i in heights :
    total += 1
print(f"no. of students =  {total}")

#avg of height

avg = total_height/total
print(avg)

'''
#to find highest score amongst a list of scores

scores = [78,88,56,98,36,97]
max = 0
for score in scores :
    if max < score :
        max = score
print(max)
