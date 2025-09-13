with open('story.txt', 'r') as f:
    story = f.read()

words = set()
target_start= '<'
target_end = '>'
start_idx = -1

for i, char in enumerate(story):
    if char == target_start:
        start_idx = i

    if char == target_end and start_idx != -1:
        words.add(story[start_idx:i+1])
        start_idx = -1

answers = {}

for word in words:
    answer = input(f'Enter a word {word}: ')
    answers[word] = answer
for word in words:
    story = story.replace(word, answers[word])
print(story)