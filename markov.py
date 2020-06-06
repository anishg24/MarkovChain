import random
import json
import os
import glob

json_directory = os.path.join(os.getcwd() + "/jsons")
jsons = glob.glob(json_directory + "/*.json")
dictionary = {}
for j in jsons:
    with open(j, "r") as f:
        dictionary = {**dictionary, **(json.load(f))}


last_word = "~~~" * 100
result = ""
new_word = input(">> ")
for i in range(0, 50):
    if new_word not in dictionary:
        new_word = dictionary[random.choice(list(dictionary.keys()))]
    else:
        candidates = dictionary[new_word]
        candidates_normed = []

        for word in candidates:
            freq = candidates[word]
            for _ in range(0, freq):
                candidates_normed.append(word)

        new_word = random.choice(candidates_normed)
    result += " " + new_word
    last_word = new_word

print(result)
