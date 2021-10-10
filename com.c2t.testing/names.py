from name_function import get_formatted_name_first_last

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break

    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name_first_last(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')