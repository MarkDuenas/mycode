# Write a Python function to sum all the numbers in a list.
def find_sum(list):
    total = sum(list)
    print(total)
    return total


find_sum([5, 10, 54, 12, 76, 89])

# Write a Python program to print the even numbers from a given list.
def find_even(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num)
    print(new_list)
    return new_list


find_even([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Write a Python function that checks whether a passed string is palindrome or not.
def find_palindrome(str):
    stripped = str.replace(" ", "")
    return stripped == stripped[::-1]


print(find_palindrome("madam"))
print(find_palindrome("not a palindrome"))
print(find_palindrome("nurses run"))

# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def sort_sequence(str):
    string_list = str.split("-")
    string_list.sort()
    return "-".join(string_list)


print(sort_sequence("green-red-yellow-black-white"))
