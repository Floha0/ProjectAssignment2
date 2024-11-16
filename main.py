from collections import Counter

# Sample text
text = "Hello! This is a well-known example. They're working on it. well-known n text is a here."

# list for end of sentence punctuation
end_of_sentence_punctuation = ['.', '!', '?', '...']

# Split the text by the end of sentence punctuations
splitted_text = []
tmp = ""
for i in range(len(text)):
    if text[i] in end_of_sentence_punctuation:
        splitted_text.append(tmp)
        tmp = ""
    else:
        # this if statement stands for removing the leading space 
        if len(tmp) > 0: 
            if tmp[0] == " ":
                tmp = tmp[1:]
        
        tmp += text[i]

# Avarage word count in a sentence
words_per_sentence = sum([len(sentence.split()) for sentence in splitted_text]) / len(splitted_text)
        
# Remove the end of sentence punctuations
cleaned_text = ''.join([char for char in text if char not in end_of_sentence_punctuation])

# Count the number of sentences by looking at the punctuation marks at the end of each sentence
sentence_count = sum([1 for char in text if char in end_of_sentence_punctuation])

# Tokenize the text
tokens = cleaned_text.split()

# Finding the longest and shortest token(s)
max_length = max(len(token) for token in tokens)
longest_tokens = list(set(token for token in tokens if len(token) == max_length))

min_length = min(len(token) for token in tokens)
shortest_tokens = list(set(token for token in tokens if len(token) == min_length))


# Count the number of unique words
counter = Counter(tokens)
sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

# Create a dictionary for the words where the key is the count of the word and the value is a list of words with that count
word_dict = dict()
for word, count in sorted_words:
    if count in word_dict:
        word_dict[count].append(word)
    else:
        word_dict[count] = [word]
        
# Find the most common word(s)
most_common_words = [item[0] for item in sorted_words if item[1] == sorted_words[0][1]]

number_of_characters_in_words = sum([len(token) for token in tokens])

print("Statistics about <FILE_NAME>:")
print(f"#Words: {len(tokens)}")
print(f"#Sentences: {sentence_count}")
print(f"#Words/#Sentences: {words_per_sentence:.2f}")
print(f"#Characters: {len(text)}")
print(f"#Characters (Just Words): {number_of_characters_in_words}")

if len(longest_tokens) == 1:
    # longest word and its frequency 
    print(f"The Longest Word: {longest_tokens[0]:<24} ({counter[longest_tokens[0]]})")
else:
    print("The Longest Words:")
    for token in longest_tokens:
        print(f"{token} ({counter[token]})")

if len(shortest_tokens) == 1:
    # shortest word and its frequency
    print(f"The Shortest Word: {shortest_tokens[0]} ({counter[shortest_tokens[0]]})")
else:
    print("The Shortest Words:")
    for token in shortest_tokens:
        print(f"{token:<24} ({counter[token]})")

print("Words and Frequencies:")
for frequency in sorted(word_dict.keys(), reverse=True):  # Sort the frequencies in descending order
    real_frequency = frequency / len(tokens)
    words = sorted(word_dict[frequency])  # Sort the words in alphabetical order
    for word in words:  
        print(f"{word:<24} : {real_frequency:.4f}")
