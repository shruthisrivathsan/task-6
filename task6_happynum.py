#create a list with given numbers
num_list = [10,501,22,37,100,999,87,351]

#assign a varible to count the happy numbers
count = 0

#iterate num_list
for num in num_list:
    #create a variable with the value of the iterated number
    a=num

    #while a is greater than or equal to 10 a new variable to find the sum is created
    while a >= 10:
        sum = 0

        #while the number is greater than 0
        while a>0:
            #the remainder is assigned to the variable rem
            rem = a%10
            #square of rem is added to sum
            sum += rem**2
            #a is divided by 10 and the decimals are omitted 
            a= a//10
        a= sum
    #if the vale of a is 1, the count is incresed by 1
    if a ==1:
        count += 1
print (count)