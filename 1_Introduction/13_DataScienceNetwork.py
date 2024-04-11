# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:06:18 2024

@author: HP
"""

# DataScience network

users = [ 
            {"id: ": 0, "name": "Ayon"},
            {"id: ": 1, "name": "Sayan"},
            {"id: ": 2, "name": "Subhasis"},
            {"id: ": 3, "name": "Dishant"},
            {"id: ": 4, "name": "Mansish"},
            {"id: ": 5, "name": "Saswat"},
            {"id: ": 6, "name": "Om kar"},
        ]

friendship_pairs = [ (0, 1), (2, 3), (4, 5), (2, 6), (3, 6) ]

friendships = { user["id"]: [] for user in users }

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def no_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(no_of_friends(user) for user in users)
avg_connections = total_connections / len(users)

no_friends_by_id = [ (user["id"], no_of_friends(user)) for user in users]
no_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)