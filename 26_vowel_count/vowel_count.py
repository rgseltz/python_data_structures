def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    letters = {}
    for char in phrase:
        char = char.lower()
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            letters[char] = letters.get(char, 0) + 1
    return letters
    