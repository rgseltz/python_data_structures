def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    result = "";
    list_phrase = list(phrase)
    list_phrase.reverse()
    for char in list_phrase:
        result += char
    return result
    
