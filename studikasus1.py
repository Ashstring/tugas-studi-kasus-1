def find_min_max(a, b, c):
    if a > b:
        max_temp = a
    else:
        max_temp = b

    if max_temp > c:
        max_value = max_temp
    else:
        max_value = c
        
# nilai minimum
    if a < b:
        min_temp = a
    else:
        min_temp = b

    if min_temp < c:
        min_value = min_temp
    else:
        min_value = c

    return min_value, max_value

a = int(input("Masukkan Nilai A :"))
b = int(input("Masukkan Nilai B :"))
c = int(input("Masukkan Nilai C :"))

min_val, max_val = find_min_max(a, b, c)
print(f"Nilai Minimum: {min_val}, Nilai Maksimum: {max_val}")
 