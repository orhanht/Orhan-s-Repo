"""
Instructions:

Implement the classic method for composing secret messages called a square code.
Given an English text, output the encoded version of that text.
First, the input is normalized: the spaces and punctuation are removed from the English text and the message is downcased.
Then, the normalized characters are broken into rows. These rows can be regarded as forming a rectangle when printed with intervening newlines.
For example, the sentence
"If man was meant to stay on the ground, god would have given us roots."
is normalized to:
"ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
The plaintext should be organized in to a rectangle. The size of the rectangle (r x c) should be decided by the length of the message,
such that c >= r and c - r <= 1, where c is the number of columns and r is the number of rows.
Our normalized text is 54 characters long, dictating a rectangle with c = 8 and r = 7:
"ifmanwas"
"meanttos"
"tayonthe"
"groundgo"
"dwouldha"
"vegivenu"
"sroots  "
The coded message is obtained by reading down the columns going left to right.
The message above is coded as:
"imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"
Output the encoded text in chunks that fill perfect rectangles (r X c), with c chunks of r length, separated by spaces.
For phrases that are n characters short of the perfect rectangle, pad each of the last n chunks with a single trailing space.
"imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
"""

import math


def cipher_text(plain_text):
    plain_text = plain_text.lower()
    plain_text = "".join(i for i in plain_text if i.isalnum())
    if plain_text == "":
        return ""
    sqrt_of_len = math.sqrt(len(plain_text))
    if sqrt_of_len.is_integer():
        r = int(sqrt_of_len)
        c = int(sqrt_of_len)
    else:
        if len(plain_text) <= int(sqrt_of_len)*(int(sqrt_of_len) + 1):
            plain_text += " " * (int(sqrt_of_len)*(int(sqrt_of_len) + 1) - len(plain_text))
            r = int(sqrt_of_len)
            c = int(sqrt_of_len) + 1
        else:
            plain_text += " " * ((int(sqrt_of_len) + 1)**2 - len(plain_text))
            r = int(sqrt_of_len) + 1
            c = int(sqrt_of_len) + 1
    final_ish = ""
    for j in range(c):
        for count, i in enumerate(plain_text):
            if count % c == j:
                final_ish += i
    return " ".join(final_ish[i:i+r] for i in range(0, len(final_ish), r))
