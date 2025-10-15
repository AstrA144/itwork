def find_min(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value
my_list = [11, 56, 55, 78]
min_number = find_min(my_list)
print(f"минимальное число в списке: {min_number}")


#3)
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i == 0:
        if n % i == 0:
            return False
        i += 1
    return True
def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count
my_list = [4, 2, 8, 4, 24, 6, 13, 8, 74, 10, 155, 12]
prime_count = count_primes(my_list)
print(f"количество простых чисел в списке: {prime_count}")


#5)
def combine_lists(list1, list2):
    combined_list = list1 + list2
    return combined_list
list_a = [3, 2, 1]
list_b = ['z', 'x', 'c']
result_list = combine_lists(list_a, list_b)
print(result_list)









