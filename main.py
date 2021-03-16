for i in range(1,1001,2):
    n = i ** 3
    print(n, i)
#* далее нужно по каждому нечетному посчитать сумму его отдельных цифр и вот эту сумму как раз проверить на кратность 7
# если сумма кратна 7, то само число нужно суммировать
    suma = 0
    while n > 0:
        digit = n % 10
        suma += digit
        n //= 10
    print("Сумма по каждому нечетному числу в кубе  :", suma)

    sum2 = 0
    sum3 = 0
    if suma % 7 == 0:
        digits = suma % 10
        sum2 += digits
        suma //= 10
        digits = suma %10
        sum2 += digits
        sum3 = sum2 + 17
        print('=', sum2, ' КРАТНО 7', 'если прибавить 17 =', sum3)
        print('         ')
        if sum3 % 7 == 0:
            digits = sum3 % 10
            sum4 += digits
            sum3 //= 10
            digits = sum3 % 10
            sum4 += digits
            print(sum3, ' ДЕЛИТЬСЯ =', sum4)
            print('         ')
            print('         ')
            print('    $     ')
        else:
            print(sum3, 'не делится на 7 к сожалению!!!!!!!!!!!!!')
            print('    ////////////////     ')
    else:
        print('число не кратно 7')
        print('----------------------------------')
        sum4 = 0
