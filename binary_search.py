
def binary_search(array, item):
    'Returns the position/index the item in the array, or null.'

    # Defining the range to search through
    # Keeps track of which part of the list is being searched in.
    low = 0
    high = len(array) - 1

    # While the search space is not narrowed down, left to only 1 element
    while low <= high:

        # Each time, check the middle of that range
        mid = (low + high) // 2

        guess = array[mid]

        if guess == item: # ITEM FOUND
            return mid

        if guess > item: # The guess was too hight
            high = mid - 1 # lower the high to 1 below the mid

        else: # The guess was too low
            low = mid + 1 # increa the low to 1 above the mid

    # THe item is not in the list
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 5)) # => 2
print(binary_search(my_list, 2)) # => None
