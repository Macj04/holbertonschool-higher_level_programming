def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    decimal = 0
    
    for i in range(len(roman_string)):
        if roman_string[i] not in convert:
            return 0
        
        if i > 0 and convert[roman_string[i]] > convert[roman_string[i-1]]:
            decimal += convert[roman_string[i]] - 2 * convert[roman_string[i-1]]
        else:
            decimal += convert[roman_string[i]]
    
    return decimal
