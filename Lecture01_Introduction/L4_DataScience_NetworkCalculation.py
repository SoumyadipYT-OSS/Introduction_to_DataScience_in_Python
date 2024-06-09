users = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"}
    ]


friendship_pairs = [
        (0, 1), (0, 2), (1, 2), (1, 3),
        (2, 3), (3, 4), (4, 5), (5, 6),
        (5, 7), (6, 8), (7, 8), (8, 9)
    ]



friendships = {user["id"]: [] for user in users}


for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)



def no_of_friends(user):
    user_id = user["id"]
    f_id = friendships[user_id]
    return len(f_id)


total_connections = sum(no_of_friends(usr) for usr in users)
avg_connections = total_connections / len(users)


no_friends_by_id = [(u["id"], no_of_friends(u)) for u in users]
no_friends_by_id.sort(key=lambda f_id: f_id[1], reverse=True)

print(no_friends_by_id)