def get_formatted_name_first_last(first, last):
    """Generate a neatly-formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

def get_formatted_name_first_middle_last(first, last, middle=''):
    """Generate a neatly-formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
