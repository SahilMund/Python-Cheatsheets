
# conversion from string to list

s="hy my name is sahil"

#  1.
print(s.split())   -#split always return a list
print(s)

# 2.
print(list(s))

#conversion from string to list

l=['hey','guys','what','up']
print("".join(l))

print("	 ".join(l))


print(" , ".join(l))


#conversion of list to tuple

l=['hey','guys','what','up']
print(tuple(l))

#ord -- it gives the ASCII value of the alphabets
ord('a')  # 97

#chr ---it gives the value of given ascii value
chr(97)     # a
