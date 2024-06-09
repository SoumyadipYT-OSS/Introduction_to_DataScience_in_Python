interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),                 (0, "Spark"), (0, "Storm"), (0, "Storm"), (0, "Cassandra"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"), (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"), (5, "Python"), (5,"R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"), (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"), (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")]



from collections import defaultdict, Counter

u_ids_by_interest = defaultdict(list)
for u_id, u_interest in interests:
    u_ids_by_interest[u_interest].append(u_id)
    
interests_by_uId = defaultdict(list)
for u_id, u_interest in interests:
    interests_by_uId[u_id].append(u_interest)


def most_common_interests_with(usr):
    return Counter(
            x
            for u_interest in interests_by_uId[usr["id"]]
            for x in u_ids_by_interest[u_interest]
            if interests_by_uId != usr["id"]
        )
    
