"""
Instructions:

Tally the results of a small football competition.
Based on an input file containing which team played against which and what the outcome was, create a file with a table like this:
Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1

Your tallying program will receive input that looks like:
Allegoric Alaskans;Blithering Badgers;win
Devastating Donkeys;Courageous Californians;draw
Devastating Donkeys;Allegoric Alaskans;win
Courageous Californians;Blithering Badgers;loss
Blithering Badgers;Devastating Donkeys;loss
Allegoric Alaskans;Courageous Californians;win
"""

def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    teams = set()
    mp_total = []
    w_total = []
    d_total = []
    for i in rows:
        splitted = i.split(";")
        teams.add(splitted[0])
        teams.add(splitted[1])
        mp_total.append(splitted[0])
        mp_total.append(splitted[1])
        if splitted[2] == "win":
            w_total.append(splitted[0])
        elif splitted[2] == "loss":
            w_total.append(splitted[1])
        else:
            d_total.append(splitted[0])
            d_total.append(splitted[1])
    teams = list(teams)
    points = {}
    for i in teams:
        points[i] = (w_total.count(i) * 3 + d_total.count(i))

    teams.sort(key=lambda x: (-points[x], x))

    for i in teams:
        table.append(f"{i:<31}|  {mp_total.count(i)} |  {w_total.count(i)} |  {d_total.count(i)} |  "
                     f"{mp_total.count(i) - w_total.count(i) - d_total.count(i)} | "
                     f" {w_total.count(i) * 3 + d_total.count(i)}")

    return table
