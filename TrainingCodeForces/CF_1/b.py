import math
# https://codeforces.com/problemset/problem/1/B
# Inputs:
    #Exel Grid Location Systems, Convert Char to Column Number
    # 1 = A, Z = 26, AA = 27
excel_1 = 'BC23'


#(26^CharIndexWithinString)*CharIndexWithinAlphabet
def square_n_times(char_index_within_string: int, char: str) -> int:
    letter_to_number_upper = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
    'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}       
    char_index_with_alphabet = letter_to_number_upper[char]
    return_index = ((math.pow(26, char_index_within_string)) * char_index_with_alphabet)
    return return_index

def convert_exc_to_exc2(exc1: str):
        #If is type str
        found_keys = [key for key in exc1 if not key.isdigit()]
        #Last valid char in list is first index
        found_keys = list(reversed(found_keys))

        column_odinal = 0
        #For current index, calculate number of squared by position and number in index char
        for index, char in enumerate(found_keys):
               column_odinal = column_odinal + square_n_times(index,char)

        return column_odinal

# print(print(square_n_times(1,'A')))
print(convert_exc_to_exc2(excel_1))
print(convert_exc_to_exc2('AAA'))
print(convert_exc_to_exc2('BAA'))

