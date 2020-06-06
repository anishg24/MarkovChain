import json
import os
import glob
import itertools

text_directory = os.path.join(os.getcwd() + "/texts")
json_directory = os.path.join(os.getcwd() + "/jsons")

make_dir = lambda x: os.mkdir(x) if not os.path.exists(x) else 1
make_dir(text_directory)
make_dir(json_directory)


def get_dict(a):
    res_dict = {}
    for i in range(len(a) - 1):
        word = a[i]
        next_word = a[i + 1]

        if word in res_dict:
            if next_word in res_dict[word]:
                res_dict[word][next_word] += 1
            else:
                res_dict[word][next_word] = 1
        else:
            res_dict[word] = {next_word: 1}
    return res_dict


files = glob.glob(text_directory + "/*.txt")
for file in files:
    json_name = json_directory + f'/{(file.split("/")[-1]).split(".")[0]}.json'
    if not os.path.exists(json_name):
        with open(file, "r") as f:
            file_list = list(map(lambda l: l.split(" "), f.read().splitlines()))
            dictionary = get_dict(list(itertools.chain.from_iterable(file_list)))
        with open(json_name, "w+") as out:
            json.dump(dictionary, out)


# def pickRandom(dictionary):
#     num = random.randint(0, len(dictionary) - 1)
#     new_word = list(dictionary.keys())[num]
#     return new_word
#
#
# def get_next_word(word, dictionary):
#     if word not in dictionary:
#         new_word = pickRandom(dictionary)
#         return new_word
#     else:
#         candidates = dictionary[word]
#         candidates_normed = []
#
#         for cword in candidates:
#             freq = candidates[cword]
#             for i in range(0, freq):
#                 candidates_normed.append(cword)
#
#         rnd = random.randint(0, len(candidates_normed) - 1)
#         return candidates_normed[rnd]
#
#
# last_word = "~~~" * 100
# result = ""
# for i in range(0, 50):
#     new_word = get_next_word(last_word, dictionary)
#     result += " " + new_word
#     last_word = new_word
# print(result)
