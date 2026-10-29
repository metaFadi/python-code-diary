# l=["google","apple","python","orange"]
# res={value:index for index, value in enumerate(l)}
# print(res)


# 3. WAP create a dictionary having first char of word and word pair if word having even length

l=["google","apple","python","orange"]
res={value[0]:value for value in l if len(value)%2==0}
print(res)
