"""
# DAY 26 : LIST COMPREHENSION
# CREATE A NEW LST USING PREVIOUS LIST
numbers =[1,2,3]
new_list = []
for n in numbers:
    add = n+1
    new_list.append(add)
print(new_list)

LIST COMPREHENSION : new_list = [new_item for item in list]
Basically, it is used for creating new lists from already existing ones.

numbers =[1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

PYTHON SEQUENCES:list,strings,tuples,range
list
name ="Simran"
new_list = [letter for letter in name]
print(new_list)

range
range_list =[num*8 for num in range(1,5)]
print(range_list)

CONDITIONAL LC
new_list=[new_item for item in list if test]

names = ["Alex","Betty","Catherine","Dolly","Ernold","Frederick"]
new_names = [ name.upper() for name in names if len(name) >= 5]
print(new_names)

DICTIONARY COMPREHENSION:
new_dict={new_key:new_value for (key,value) in dict.items() if test}

import random
names = ["Alex","Betty","Catherine","Dolly","Ernold","Frederick"]
students_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student , score) in students_scores.items() if score>=60}
print(students_scores)
print(f"The passed students are: {passed_students}")

#DICTIONARY COMPREHENSION USING PANDAS DATAFRAME
{new_key:new_value for (index,row) in dataframe_name.iterrow()}

import pandas

student_scores ={
  "student": [ "Angela","James","Lily"],
    "score": [58,76,98]
}
student_data = pandas.DataFrame(student_scores)
#print(student_data)
#loop through a data frame
#for (key,value) in student_data.items():
 # print(key)
for (index,row) in student_data.iterrows():
  if row.student=="Lily":
    print(row.score)
"""
import pandas
