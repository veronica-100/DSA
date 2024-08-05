kaprekar_constant = 6174
def find_kaprekar(val, n = 0):
    if val == kaprekar_constant:
        return n
    string_val = str(val)
    string_val = ((4 - len(string_val)) * "0" ) + string_val
    asc_val = "".join(sorted(string_val))
    dec_val = int(asc_val[::-1])
    asc_val = int(asc_val)
    value = dec_val - asc_val
    return find_kaprekar(value,n+1)


print(find_kaprekar(1000))
print(find_kaprekar(191))
print(find_kaprekar(123))
print(find_kaprekar(78))