from collections import defaultdict

with open("about.txt") as data_file:
     data = data_file.read().split("\n")


data_structure = defaultdict(set)

for i in range(len(data)):
    for j in range(len(data[i])):
        for k in range(j+1, len(data[i])+1):
            data_structure[data[i][j:k]].add(i)
            data_structure[data[i][k:j]].add(i)

data_structure.pop("")




# sentence = ["hello world", "hi everyone"]
#
# data = {"h": [sentence[0],sentence[1]],
# "he": sentence[0],
# "hel":  sentence[0],
# "hell":  sentence[0],
# "hello":  sentence[0],
# "hello w": sentence[0],
# "hello wo": sentence[0],
# "hello wor": sentence[0],
# "hello worl": sentence[0],
# "hello world ": sentence[0],
# "world": sentence[0],
# "worl": sentence[0],
# "wor": sentence[0],
# "wo": sentence[0],
# "w": sentence[0],
# "hi": sentence[1],
# "hi e": sentence[1],
# "hi ev": sentence[1],
# "hi eve": sentence[1],
# "hi ever": sentence[1],
# "hi every": sentence[1],
# "hi everyo": sentence[1],
# "hi everyon": sentence[1],
# "hi everyone ": sentence[1],
# "e": sentence[1],
# "ev": sentence[1],
# "eve": sentence[1],
# "ever": sentence[1],
# "every": sentence[1],
# "everyo": sentence[1],
# "everyon": sentence[1],
# "everyone": sentence[1],
# }

