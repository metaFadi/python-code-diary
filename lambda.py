# l=["google","apple","python","orange"]
# res={value:index for index, value in enumerate(l)}
# print(res)


# 3. WAP create a dictionary having first char of word and word pair if word having even length

# l=["google","apple","python","orange"]
# res={value[0]:value for value in l if len(value)%2==0}
# print(res)


# 4. WAP to check length of words and create a dict having word and word pair if it is even but if is it having odd length then reverse and add

# l=["google","apple","python","orange"]
# res={value:value if len(value)%2==0 else value[::-1] for value in l}
# print(res)


# # 5. WAP to check elements is palindrome key and value should be same else value is reverse of key

# l=["banana","malayalam","madam","sir","mom","dad"]
# res={value:value if value==value[::-1] else value for value in l}
# print(res)


get_lenortype = lambda col: [len(num) if type(num) in (str, list, tuple, dict, set) else type(num) for num in col]
# get_lenortype2 = lambda num: len(num) if isinstance(num, (str, list, tuple, dict, set)) else type(num)
collection = eval(input('Enter the collection: '))
get_lenortype(collection)
