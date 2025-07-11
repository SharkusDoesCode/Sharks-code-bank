#frequency analysis
import re
import json
from enum import Enum
class Frequencies(Enum):     #to acess an Enum: Frequencies."character".value
    A = 8.2
    B = 1.5
    C = 2.8
    D = 4.3
    E = 12.7
    F = 2.2
    G = 2.0
    H = 6.1
    I = 7.0
    J = 0.2
    K = 0.8
    L = 4.0
    M = 2.4
    N = 6.7
    O = 7.5
    P = 1.9
    Q = 0.1
    R = 6.0
    S = 6.3
    T = 9.1
    U = 2.8
    V = 1.0
    W = 2.4
    X = 0.2
    Y = 2.0
    Z = 0.1

cipherText = "ZIOL VQL YOKLZ SGCT. OZ IQR ZIQZ LTFLT GY LXKKTFRTK, QFR Q ITOUIZTFTR QVQKTFTLL, QL GY WKOSSOQFZ EGSGXK WXKLZOFU XHGF Q WSQEA QFR VIOZT VGKSR"

def cryptAnalysis(cipherText):   #compiles each characters frequency into a dictionary
    string = re.sub(r"[!?#-,. ]", '', cipherText) #removes punctuation including spaces
    freq = {i: string.count(i) for i in string} #dictionary comprehension
    for i in freq:   #to access: freq["character"]
        freq[i] = round((freq[i]/len(string))*100,1) #convert into percentages rounded to 1 d.p
    return freq

def dictAverageFrequencies(Frequencies): #average frequency converted from enum to dictionary
    AverageFrequencies = {i.name: i.value for i in Frequencies} #dictionary comprehension
    return AverageFrequencies   

def txtFrequencyFile(cipherText):       #txt file 
    with open('data.txt', 'w') as text_file:
        text_file.write(str(cryptAnalysis(cipherText)))

def jsonFrequencyFile(cipherText):   #json file
    with open('data.json', 'w') as json_file:
        json.dump(cryptAnalysis(cipherText), json_file)
        open('data.json','r')

jsonFrequencyFile(cipherText)