"""
**Miscellaneous Functions**
"""


def pigLatin(stg):
    """
    Takes a single word as a string and returns the word in pig latin.
    This function was made for a homework problem.
    """
    vowels = "aeiou"
    sng = stg.lower()
    ix = -1
    found = False
    while ix < len(sng) - 1 and not found:
        ix += 1
        if sng[ix] in vowels:
            found = True
    if not found or sng[:ix] == '':
        return sng + 'way'
    else:
        return sng[ix:] + sng[:ix] + 'ay'


# I recommend playing around with the functions!
# Some suggested function calls are commented out below.


if __name__ == "__main__":

    # Sample calls for pigLatin()
    print('triple', pigLatin('triple'))
    print('anvil', pigLatin('anvil'))
