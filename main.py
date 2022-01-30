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

list_of_numbers = [3, 9, 2, 1, 4, 0, 6, 8, 5, 7]
x = 0
list_changed = False

while x < (len(list_of_numbers) - 1):

    if list_of_numbers[x] > list_of_numbers[x + 1]:
        list_changed = True
        temp = list_of_numbers[x]
        list_of_numbers[x] = list_of_numbers[x + 1]
        list_of_numbers[x + 1] = temp
    x += 1

    if x == (len(list_of_numbers) - 1) and list_changed == True:
        x = 0
        list_changed = False

print(list_of_numbers)