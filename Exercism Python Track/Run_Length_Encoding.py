"""
Instructions:

Run-length encoding (RLE) is a simple form of data compression,
where runs (consecutive data elements) are replaced by just one data value and count.
For example we can represent the original 53 characters with only 13.

"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
RLE allows the original data to be perfectly reconstructed from the compressed data, which makes it a lossless data compression.

"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
For simplicity, you can assume that the unencoded string will only contain the letters A through Z (either lower or upper case)
and whitespace. This way data to be encoded will never contain any numbers and numbers inside data to be decoded always represent the count for the following character.
"""

def decode(string):
    decoded = ""
    last_count = "1"
    for i in range(len(string)):
        if string[i].isalpha() or string[i] == " ":
            decoded += string[i] * int(last_count)
            last_count = "1"
        elif string[i - 1].isdigit():
            last_count += string[i]
        elif string[i].isdigit():
            last_count = string[i]
    return decoded


def encode(string):
    encoded = ""
    count_list = []
    last = ""
    for i in string:
        if i == last:
            count_list[-1] = (i, count_list[-1][1] + 1)
        else:
            count_list.append((i, 1))
            last = i
    for i in count_list:
        if not i[1] == 1:
            encoded += str(i[1]) + i[0]
        else:
            encoded += i[0]
    return encoded
