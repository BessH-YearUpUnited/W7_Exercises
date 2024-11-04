characters = {
    'main': 'Little Red Riding Hood',
    'villain': 'Big Bad Wolf',
    'supporting': 'Grandmother'
}

basket = {
    'pastries': ('buns', 'bread', 'pie'),
    'medicines': ('willow bark tea', 'elderberry cordial')
}








# # # # # # #

# def char_descr():

#     count = 0
#     descr = ''

#     for i in characters.values():
#         count += 1
#         descr = descr + f'Character {count} in the story is {i}.\n'
    
#     return descr


# def basket_check():

#     report = ''

#     for i in basket.items():
#         goodies = ''
#         for x in i[1]:
#             if x == i[1][-1]:
#                 goodies = goodies + 'and '
#             goodies = goodies + x
#             if x != i[1][-1]:
#                 goodies = goodies + ', '
#         report = report + f'{characters["main"]}\'s basket includes {i[0]} consisting of {goodies}.\n'
        
#     return report

# print(char_descr())
# print(basket_check())