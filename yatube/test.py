# def create_phone_number(n):
#     x1 = ''.join(map(str, n[0:3]))
#     x2 = ''.join(map(str, n[3:6]))
#     x3 = ''.join(map(str, n[6:-2]))
#     return f'({x1}) {x2}-{x3}'
    
# def is_pangram(st):
#     alphabet = set('abcdefghijklmnopqrstuvwxyz')
#     if alphabet == set(st.lower()):
#         return True
#     else:
#         return False

# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False

#     north_south = walk.count('n') - walk.count('s')
#     east_west = walk.count('e') - walk.count('w')

#     if north_south == 0 and east_west == 0:
#         return True
#     else:
#         return False

# is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])

# def square_sum(numbers):
#     square = [x ** 2 for x in numbers]
#     return(sum(square))
# square_sum([1, 2, 2])

# def solution(text, ending):
#     reversed_text = text[::-1]
#     reversed_ending = ending[::-1]
#     return reversed_text.startswith(reversed_ending)

# def solution(text, ending):
#     return text.endswith(ending)

# # Приклади використання
# print(solution('abc', 'bc'))  # Виведе: True
# print(solution('abc', 'd'))   # Виведе: False

def remove_char(s):
    # Видаляємо перший і останній символи
    return s[1:-1]
