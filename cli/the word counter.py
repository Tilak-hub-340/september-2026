## Word Counter
"""
step to do that 
1. open the file 
2. read the text 
3. count the number of words
4. print the result
"""


with open("sample.txt", "r") as file:
    content = file.read()
    counts = {}
    for word in content.split():
        word = word.lower().strip(".,!?;:\"'()[]{}")  # Normalize the word by converting to lowercase and stripping punctuation
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

def get_count(item):
    return item[1]

for word, count in sorted(counts.items(), key=get_count, reverse=True):
    print(f"{word}: {count}")