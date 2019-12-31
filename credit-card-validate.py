# Validate whether a Credit Card is a valid one based on the Luhn Check
cred_arr = []
total = 0
credit_card = input('Enter the credit card to be validated :')


def CreditCardValidate(reversed_string):
    sum_odd = 0
    sum_even = 0
    # Reverse the String and add into an array
    reversed_string = credit_card[::-1]
    for x in range(len(reversed_string)):
        cred_arr.append(reversed_string[x:x+1])
    # Logic
    for i in range(0, len(reversed_string)):
        int_digits = int(cred_arr[i])
        if i % 2 == 0:
            sum_odd += int_digits
        else:
            int_digits *= 2
            if int_digits > 9:
                int_digits -= 9
            sum_even += int_digits

    total = sum_even + sum_odd


CreditCardValidate(credit_card)

if total % 10 == 0:
    print('Valid Credit Card')
else:
    print('Invalid Credit Card')
