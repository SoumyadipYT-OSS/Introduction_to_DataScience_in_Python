# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

users = [ 
            {"id: ": 0, "name": "Ayon"},
            {"id: ": 1, "name": "Sayan"},
            {"id: ": 2, "name": "Subhasis"},
            {"id: ": 3, "name": "Dishant"},
            {"id: ": 4, "name": "Mansish"},
            {"id: ": 5, "name": "Saswat"},
            {"id: ": 6, "name": "Om kar"},
        ]

friendship_pairs = [ (0, 1), (2, 3), (4, 5), (2, 6), (3, 6) ]  # these tuples in the list indicates the friendship pairs that is id '0' is friend of id '1'.


print(friendship_pairs)

print("\n")

for pair in friendship_pairs:
    id1, id2 = pair
    n1 = users[id1]["name"]
    n2 = users[id2]["name"]
    print(f"{n1} is a friend of {n2}")
    