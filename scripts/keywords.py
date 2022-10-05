import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import brown
import csv
from nltk.tokenize import word_tokenize
from typing import Counter
from nltk.stem.wordnet import WordNetLemmatizer

Penn_tags = ["CC","CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBG", "VBD", "VBN", "VBP", "VBZ", "WDT", "WP", "WRB"]

# Name of path to file
path = "../data/final_data.csv"

def extract_frequencies(transcript): 
    # create a dictionary that stores the relevant information for each type
    tag_dictionary = {}
    for tag in Penn_tags:
        tag_dictionary[tag] = []
    #transcript = row["transcript"]
    transcript_list = word_tokenize(transcript)
    tagged_transcript_list = nltk.pos_tag(transcript_list)
    for word_pairing in tagged_transcript_list:
        if ("'" not in word_pairing[0]) and (word_pairing[1] != "NNP") and (word_pairing[1] != "NNPS"):
            if word_pairing[1] in Penn_tags:
                tag_dictionary[word_pairing[1]].append((word_pairing[0]).lower())

    # converting all the verbs to the same form
    for word1 in tag_dictionary["VBD"]:
        new_word1 = WordNetLemmatizer().lemmatize(word1,'v')
        tag_dictionary["VB"].append(new_word1)
    tag_dictionary.pop("VBD")
    for word2 in tag_dictionary["VBG"]:
        new_word2 = WordNetLemmatizer().lemmatize(word2,'v')
        tag_dictionary["VB"].append(new_word2)
    tag_dictionary.pop("VBG")
    for word3 in tag_dictionary["VBN"]:
        new_word3 = WordNetLemmatizer().lemmatize(word3,'v')
        tag_dictionary["VB"].append(new_word3)
    tag_dictionary.pop("VBN")
    for word4 in tag_dictionary["VBP"]:
        new_word4 = WordNetLemmatizer().lemmatize(word4,'v')
        tag_dictionary["VB"].append(new_word4)
    tag_dictionary.pop("VBP")
    for word5 in tag_dictionary["VBZ"]:
        new_word5 = WordNetLemmatizer().lemmatize(word5,'v')
        tag_dictionary["VB"].append(new_word5)
    tag_dictionary.pop("VBZ")

    # converting all the adjectives to the same form
    for word6 in tag_dictionary["JJR"]:
        new_word6 = WordNetLemmatizer().lemmatize(word6,'a')
        tag_dictionary["JJ"].append(new_word6)
    tag_dictionary.pop("JJR")
    for word7 in tag_dictionary["JJS"]:
        new_word7 = WordNetLemmatizer().lemmatize(word7,'a')
        tag_dictionary["JJ"].append(new_word7)
    tag_dictionary.pop("JJS") 

    # putting all the adverbs into one list (the RB list)
    for word8 in tag_dictionary["RBR"]:
        tag_dictionary["RB"].append(word8)
    tag_dictionary.pop("RBR")
    for word9 in tag_dictionary["RBS"]:
        tag_dictionary["RB"].append(word8)
    tag_dictionary.pop("RBS")


    # converting all nouns to the same form (add all to NN)
    for word10 in tag_dictionary["NNS"]:
        new_word10 = WordNetLemmatizer().lemmatize(word10)
        tag_dictionary["NN"].append(new_word10)
    tag_dictionary.pop("NNS") 
    for word11 in tag_dictionary["NNP"]:
        new_word11 = WordNetLemmatizer().lemmatize(word11)
        tag_dictionary["NN"].append(new_word11)
    tag_dictionary.pop("NNP")
    for word12 in tag_dictionary["NNPS"]:
        new_word12 = WordNetLemmatizer().lemmatize(word12)
        tag_dictionary["NN"].append(new_word12)
    tag_dictionary.pop("NNPS")

    # get rid of tags we don't want to analyze
    tag_dictionary.pop("CC")
    tag_dictionary.pop("CD")
    tag_dictionary.pop("DT")
    tag_dictionary.pop("EX")
    tag_dictionary.pop("IN")
    tag_dictionary.pop("LS")
    tag_dictionary.pop("MD")
    tag_dictionary.pop("POS")

    for key in tag_dictionary:
        tag_dictionary[key] = Counter(tag_dictionary[key]).most_common()
    tagged_transcript_dictionary[row["title"]] = tag_dictionary
    nouns = (tagged_transcript_dictionary[row["title"]]["NN"])
    print(nouns[0])
    

