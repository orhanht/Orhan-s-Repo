"""
Instructions:

Output the lyrics to 'The Twelve Days of Christmas'.
"""

def recite(start_verse, end_verse):
    items_list = ["twelve Drummers Drumming, ", "eleven Pipers Piping, ", "ten Lords-a-Leaping, ",
                  "nine Ladies Dancing, ", "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ",
                  "six Geese-a-Laying, ", "five Gold Rings, ", "four Calling Birds, ", "three French Hens, ",
                  "two Turtle Doves, ", "and a Partridge in a Pear Tree."]
    cardinal_numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
                        "eleventh", "twelfth"]
    lyrics = []
    for i in range(start_verse, end_verse + 1):
        if i == 1:
            lyrics.append("On the first day of Christmas my true love gave to me: "
                          "a Partridge in a Pear Tree.")
        else:
            lyrics.append(f"On the {cardinal_numbers[i - 1]} day of Christmas my true love gave to me: ")
            for j in items_list[12 - i:]:
                lyrics[-1] += j
    return lyrics
