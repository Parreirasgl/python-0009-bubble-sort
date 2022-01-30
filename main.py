# I saw some people talking about bubble sort
# and tried to make it. According to Wikipedia,
# bubble sort, is a simple sorting algorithm
# that repeatedly steps through a list,
# compares adjacent elements and swaps them
# if they are in the wrong order. The pass through
# the list is repeated until the list is sorted.

# Eu vi algumas pessoas falando sobre bubble sort
# e tentei fazer um. De acordo com a Wikipédia,
# bubble sort, é um algoritmo de ordenação simples
# que percorre repetidamente uma lista, compara
# elementos adjacentes e os troca se estiverem
# na ordem errada. A passagem pela lista é repetida
# até que a lista seja ordenada.

from random import randint

list_of_numbers = []
counter = 0
list_changed = False

print("")
list_size = int(input("How many numbers do you want on your list?\n"))
print("Do you want the values on your list to vary between which numbers?")
first_number = int(input("Type first number:\n"))
second_number = int(input("Type second number:\n"))

for i in range(list_size):
    list_of_numbers.append(randint(first_number, second_number))

print("")
print(f"This is the starting list: {list_of_numbers}")

while counter < (len(list_of_numbers) - 1):

    if list_of_numbers[counter] > list_of_numbers[counter + 1]:
        list_changed = True
        temp = list_of_numbers[counter]
        list_of_numbers[counter] = list_of_numbers[counter + 1]
        list_of_numbers[counter + 1] = temp
    counter += 1

    if counter == (len(list_of_numbers) - 1) and list_changed == True:
        counter = 0
        list_changed = False

print(f"This is the list after sorting: {list_of_numbers}")