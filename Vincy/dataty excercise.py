even_sum = 0
odd_sum = 0
for numa in range (1,21,1):
    if (numa % 2 == 0) :
        even_sum = even_sum + numa
    else :
        odd_sum = odd_sum + numa

    print(even_sum)
    print(odd_sum)
    print("-" *6)
