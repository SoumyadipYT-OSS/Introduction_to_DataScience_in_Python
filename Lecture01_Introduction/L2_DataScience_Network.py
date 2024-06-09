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


# Initialize the dict with [] for each user id
friendships = { user["id"]: [] for user in users }

# Loop over the friendship_pairs to populate it.
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


# Simple iteration to see the frienship connections
print("Friendship_network:")
for i in friendships:
    print(i,":", friendships[i])


# The frienship network name display
print("\n _Display names_:")
for i in friendships:
    connectionNames = [users[friend_id]["name"] for friend_id in friendships[i]]
    print(f"{users[i]['name']}: {','.join(connectionNames)}")