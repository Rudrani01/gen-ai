#arithematic operators
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3) #gives quotient
print(5 % 3)   # modulo gives remainder
print(5 ** 3)

# assignment operators
x = 1
# x = x + 5 # 6
x += 5
print(x)

# Operator Precedence (BODMOS)
# (() > *,/ > +,-)

ans = (2 + 5) * 3
print(ans)

#Comparision Operators
# >, <, >=, <=, ==, !=

print(2 > 1) # True
print(2 > 5) # False

# Logical Operators - AND, OR, NOT

st1 = 3 > 5
st2 = 3 > 2
print(st1 or st2)

print((1>2) and (3<12))

print(not (3 > 2))