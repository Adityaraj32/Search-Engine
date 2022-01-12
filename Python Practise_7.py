'''
Author: Adityaraj Yadav 
Date: 11 January 2022
Project Name: Search Engine
Purpose:For Practising Purpose
'''


# It Splits and gives the matches word and also lowers the words and return the matched word
def MatchingWords(Sentence1, Sentence2):
    Words1 = Sentence1.split(" ")
    Words2 = Sentence2.split(" ")
    Matched_Words = 0
    for Word1 in Words1:
        for Word2 in Words2:
            if Word1.lower() == Word2.lower():
                Matched_Words += 1
    return Matched_Words


Sentences = ["Python is good", "Aditya is a good boy",
             "Shut down you comp", "I love Python"]

# The sentence searched by the user
query = input("\nSearch or Enter the url: ")

# it gives a list in which there are nubmer which says how many times the word that user searched is in the our Sentences
Result = [MatchingWords(query, Sentence) for Sentence in Sentences]

# It gives the number of results found
Sorted_Result = [Sorted for Sorted in sorted(
    zip(Result, Sentences), reverse=True)]
print(f"\t\t\t\t\t{len(Sorted_Result)} results found\n")

# It gives the number of results found in the Sentences variable 
for Result, item in Sorted_Result:
    print(f"\"{item}\": with a result of {Result}")
