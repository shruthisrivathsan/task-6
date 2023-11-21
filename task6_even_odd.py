#create a list with given numbers
num_list = [10,501,22,37,100,999,87,351]

#create two empty lists- odd_list and even_list
odd_list = []
even_list = []

#iterate num_list 
for num in num_list:
    #check if num is even and if true, add to even_list
    if num % 2 == 0:
        even_list.append(num)
    #if num is odd, add to odd_list
    else:
        odd_list.append(num)
print(even_list)
print(odd_list)
