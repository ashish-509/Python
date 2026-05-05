# Read a text file and return:
    # word frequency dictionary
    # top 5 most common words


def word_frequency(file_path):
    frequency = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?";()')
                frequency[word] = frequency.get(word, 0) + 1
    return frequency

def top_5_words(frequency):
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:5]


# Example usage
file_path = '7_readFile.txt'  
frequency = word_frequency(file_path)
print("Word Frequency Dictionary:", frequency)  
print("Top 5 Most Common Words:", top_5_words(frequency))
