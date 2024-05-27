from matplotlib import pyplot as plt

movies =["Annie Hall","Ben-Hur","Casablanca","Gandhi", "WestSideStory"]
num_oscars=[5, 11,3,8,10]

plt.bar(range(len(movies)), num_oscars)
plt.title("My Favourite Movies")
plt.ylabel("# of Academy Awards")
plt.xticks(range(len(movies)), movies)
plt.show()