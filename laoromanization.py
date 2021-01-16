# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:07:20 2020

@author: Alex
"""


from csv import reader 

romdict = {} #making a dictionary where you look up a Lao letter and find the values
with open("laoromanization.csv", encoding = "utf8", newline= "") as csvfile:
    reader = reader(csvfile, delimiter=",")
    for line in reader:
        romdict[line[0]] = line[1:] #writes the rest of the entries to the key as a list
        
samplewords = ["ເວົ້າ","ຣາມ","ນິກ","ເດັກ",'ນົກ','ປາ','ແມວ','ໄນ້','ກົງ',"ບໍ່","ນ້ໍາ"] #a list of test cases

#Lists of consonants, vowels, tone markers, and stops
#some consonants and vowels are 2+ unicode chars

conlist = ['ກ','ຂ','ຄ','ງ','ຈ','ສ','ຊ','ຍ','ດ','ຕ','ຖ','ທ','ນ','ບ','ປ','ຜ','ຝ','ພ','ຟ','ມ','ຢ','ຣ','ລ','ວ','ຫ','ອ','ຮ','ຫງ','ຫຍ','ໜ','ຫນ','ໝ','ຫມ','ຫຼ','ຫລ','ຫວ']
vowlist = ['ະ','ັ','າ','ິ','ີ','ຶ','ື','ຸ','ູ','ເະ','ເັ','ເ','ແະ','ແັ','ແ','ໂະ','ົ','ໂ','ເາະ','ັອ','ໍ','ເິ','ເີ','ເັຍ','ັຽ','ເຍ','ຽ','ເຶອ','ເືອ','ົວະ','ົວ','ົວ','ໄ','ໃ','ັຍ','ເົາ','ຳ',"ໍາ",'າວ','ເວ','ແວ','ິວ','ຽວ']
tonlist = "່້໊໋"



def transcribe(word): #word really means syllable here, todo: make the program work for more than one syllable at a time
    wordmeta = {} #The idea is to make a dictionary with entries for different parts of the word. 
    #Lao syllables have a max of two consonants and one vowel
    #Lao vowels can come before and after the consonants. This is the problem.
    #lao consonants have "inherent tones" and also overriding "tone markers"
    wordmeta["word"] = word
    noconsonants = "" #maybe I don't even need these blank lists but it primes the ol' brain
    novowels = ""
    notones = ""
    initialconsonant = ""
    finalconsonant = ""
    if word[0] == "ວ" or word[0] == "ວ": #why did I code this? why does it still work? todo: fix this
        initialconsonant = "ວ" #this letter is a tricky one 
        
    for x in tonlist:
        if x in word:
            wordmeta["tonenumber"] = romdict[x][4]
        else:
            wordmeta["tonenumber"] = "None"
    for x in word:
        if x not in tonlist:
            notones += x
    for x in notones:
        if x not in vowlist:
            novowels += x
    for x in notones:
        if x not in conlist:
            noconsonants += x
    if len(novowels) == 1:
        initialconsonant += romdict[novowels][0]
    if len(novowels) == 2:
        initialconsonant = romdict[novowels[0]][0]
        finalconsonant = romdict[novowels[1]][1]
    if finalconsonant in "ptk":
        wordmeta["endstop"] = "True"
    if finalconsonant not in "ptk" or finalconsonant == "":
        wordmeta["endstop"] = "False"
    for x in novowels: 
        if x not in conlist:#consonant list
            notones += x
    wordmeta["toneclass"] = romdict[novowels[0]][4]
    wordmeta["vowel"] = romdict[noconsonants][0]



    if ":" in romdict[noconsonants][2]:
        wordmeta["vowellength"] = "longvowel"
    if ":" not in romdict[noconsonants][2]:
        wordmeta["vowellength"] = "shortvowel"
        
    # Buncha tone rules
    
    if wordmeta.get("tonenumber") == 1:
        wordmeta["tone"] = "˧"
    if wordmeta.get("tonenumber") == 3:
        wordmeta["tone"] = "˥"
    if wordmeta.get("tonenumber") == 4:
        wordmeta["tone"] = "˨˦"
    if wordmeta.get("toneclass") == "H" and wordmeta.get("tonenumber") == 2:
        wordmeta["tone"] = "˨˩"
    if wordmeta.get("toneclass") == "H" and wordmeta.get("endstop") == "False" and wordmeta.get("tonenumber") == 'None':
        wordmeta["tone"] = "˩˨"
    if wordmeta.get("toneclass") == "H" and wordmeta.get("endstop") == "True" and wordmeta.get("tonenumber") == 'None' and wordmeta.get("vowellength") == "shortvowel":
        wordmeta["tone"] = "˦˥"
    if wordmeta.get("toneclass") == "H" and wordmeta.get("endstop") == "True" and wordmeta.get("tonenumber") == 'None' and wordmeta.get("vowellength") == "longvowel":
        wordmeta["tone"] = "˨˩"
    if wordmeta.get("toneclass") == "M" and wordmeta.get("tonenumber") == 2:
        wordmeta["tone"] = "˥˦"
    if wordmeta.get("toneclass") == "M" and wordmeta.get("endstop") == "False" and wordmeta.get("tonenumber") == 'None':
        wordmeta["tone"] = "˩˨"
    if wordmeta.get("toneclass") == "M" and wordmeta.get("endstop") == "True" and wordmeta.get("tonenumber") == 'None' and wordmeta.get("vowellength") == "shortvowel":
        wordmeta["tone"] = "˦˥"
    if wordmeta.get("toneclass") == "M" and wordmeta.get("endstop") == "True" and wordmeta.get("tonenumber") == 'None' and wordmeta.get("vowellength") == "longvowel":
        wordmeta["tone"] = "˨˩"
    if wordmeta.get("toneclass") == "L" and wordmeta.get("tonenumber") == 2:
        wordmeta["tone"] = "˥˦"
    if wordmeta.get("toneclass") == "L" and wordmeta.get("endstop") == "False" and wordmeta.get("tonenumber") == 'None':
        wordmeta["tone"] = "˦˥"
    if wordmeta.get("toneclass") == "L" and wordmeta.get("endstop") == "True" and wordmeta.get("tonenumber") == 'None' and wordmeta.get("vowellength") == "shortvowel":
        wordmeta["tone"] = "˧"
    if wordmeta.get("toneclass") == "L" and wordmeta.get("endstop") == "True" and wordmeta.get("tonenumber") == 'None' and wordmeta.get("vowellength") == "longvowel":
        wordmeta["tone"] = "˥˦"

    transcribedword = initialconsonant+wordmeta.get("vowel")+finalconsonant+wordmeta.get("tone")
    print(word, transcribedword)
    

for i in samplewords:
    # for x in i:
    #     print(romdict[x])
    # word = ""
    # for x in i:
    #     word += romdict[x][1]
    # #print(word)
    transcribe(i)
"""   
Human-readable tone rules

HC:
    tone 1 = midlevel
    tone 2 = lowfall
    notone + nostop = lowrise
    notone + stop + shortvowel = highrise
    notone + stop + longvowel = lowfall

MC:
    tone 1 = midlevel
    tone 2 = highfall
    tone 3 = highlevel
    tone 4 = rising
    notone + nostop = lowrise
    notone + stop + shortvowel = highrise
    notone + stop + longvowel = lowfall
    
LC:
    tone 1 = midlevel
    tone 2 = highfall
    notone + nostop = highrise
    notone + stop + shortvowel = mid
    notone + stop + longvowel = highfall
    
"""