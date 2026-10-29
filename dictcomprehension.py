# l=["google","apple","python","orange"]
# res={value:index for index, value in enumerate(l)}
# print(res)


# 3. WAP create a dictionary having first char of word and word pair if word having even length

l=["google","apple","python","orange"]
res={value[0]:value for value in l if len(value)%2==0}
print(res)


# 4. WAP to check length of words and create a dict having word and word pair if it is even but if is it having odd length then reverse and add

l=["google","apple","python","orange"]
res={value:value if len(value)%2=0 else value[::-1] for value in l}
print(res)
