#create 3 lists with integers

list_a = map(int, input())
list_b = map(int, input())
list_c = map(int, input())

#create 3 sets with the items of the list
set_a = set(list_a)
set_b = set(list_b)
set_c = set(list_c)

#check if there are same values in sets a and b
print(set_a.intersection(set_b))
#check if there are same values in sets b and c
print(set_b.intersection(set_c))
#check if there are same values in sets c and a
print(set_c.intersection(set_a))
