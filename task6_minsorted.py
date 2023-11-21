#create a list with the input
num_list = map(int, input())
#create new_list 
new_list= []

#iterate new_list to add numbers
for i in num_list:
    new_list.append(i)

#sort new_list
sorted(new_list)

#print the min number in the list
print(min(new_list))