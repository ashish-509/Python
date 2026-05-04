
givenString = "Any random text or feedback of the customer that needs to be analyzed. So, the customers reaction can be understood."

class textAnalyzer (object):

    def __init__ (self, text):
        text = text.lower() # make text lowercase
        formattedText = text.replace('!', '').replace('.', '').replace(',', '').replace('?', '') # remove punctuation
        self.fmtText = formattedText

    def frequencyAll (self):
        wordList = self.fmtText.split(' ') # split text into words

        # create dictionary
        frequencyMap =  {}
        for word in set(wordList) : # use set to remove duplicate items
            frequencyMap[word] = wordList.count(word)

        return frequencyMap
    
    def frequencyOf (self, word):
        frequencyDict = self.frequencyAll() # get frequency map

        if word in frequencyDict:
            return frequencyDict[word]
        else:
            return 0
        
analyzed = textAnalyzer (givenString)

print ("Formatted text is : ", analyzed.fmtText)

frequencyMap = analyzed.frequencyAll()
print (frequencyMap)

word = "customer"
frequency = analyzed.frequencyOf(word)
print("In the given string the word ", word, " appears ", frequency, " times.")

