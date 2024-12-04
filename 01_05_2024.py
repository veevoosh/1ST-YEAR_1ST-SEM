number = input("Enter a number [0-9999]: ")

ones = ["", "one ", "two ", "three ", "four ", "five ", "six ",
        "seven ", "eight ", "nine "]

tens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
        "fifteen ", "sixteen ", "seventeen ", "eighteen ",
        "nineteen "]

decades = ["", "", "twenty ", "thirty ", "forty ", "fifty ",
           "sixty ", "seventy ", "eighty ", "ninety "]

hundreds = ["", "one hundred ", "two hundred ", "three hundred ",
            "four hundred ", "five hundred ", "six hundred ",
            "seven hundred ", "eight hundred ", "nine hundred "]

thousand = ["thousand "]

num_word = ""
num_length = len(number)
num_change = num_length
up_change = 0

while num_change > 0:
    if number == "0":
        num_word = "zero"
        break

    elif num_change > 1 and number[num_change - 2] == "1":
        for digit in range(0, 10):
            if number[num_change - 1] == str(digit):
                num_word = tens[digit] + num_word

    else:
        for digit in range(0, 10):
            if number[num_change - 1] == str(digit):
                num_word = ones[digit] + num_word
        if num_change > 1:
            for digit in range(0, 10):
                if number[num_change - 2] == str(digit):
                    num_word = decades[digit] + num_word
        if num_change > 2:
            for digit in range(0, 10):
                if number[num_change - 3] == str(digit):
                    num_word = hundreds[digit] + num_word
        if num_change > 3:
            num_word = thousand[up_change] + num_word
        num_change -= 3
        up_change += 1

print(num_word)
