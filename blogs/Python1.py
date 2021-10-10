def main():
    dictionary = {}
    dictionary["learning"] = "awesome"
    dictionary["coding"] = "fun"
    # ... Fill with more data
    remove_keys_containing_string(dictionary, "coding")


"""
This Python method takes in a dict and a string, then loops through
the dict and removes all entries that have a key containing that string.
"""


def remove_keys_containing_string(dictionary, remove):
    toRemove = []
    for key in dictionary:
        if key == remove:
            toRemove.append(key)
    print(toRemove)
    if toRemove != None:
        for key in toRemove:
            del dictionary[key]

main()
