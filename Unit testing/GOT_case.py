'''
Write a function that takes a string and returns a string with the correct case for character titles in the Game of Thrones series.

The words and, the, of and in should be lowercase.
All other words should have the first character as uppercase and the rest lowercase.
Examples
correct_title("jOn SnoW, kINg IN thE noRth.")
➞ "Jon Snow, King in the North."

correct_title("sansa stark, lady of winterfell.")
➞ "Sansa Stark, Lady of Winterfell."

correct_title("TYRION LANNISTER, HAND OF THE QUEEN.")
➞ "Tyrion Lannister, Hand of the Queen."
Notes
Punctuation and spaces must remain in their original positions.
Hyphenated words are considered separate words.
Be careful with words that contain and, the, of or in.
See the Resources tab for more info on the various Python string methods.
'''
""" class Test:
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        
    def assert_equals(string1,string2):
        if string1 == string2:
            return 1
        else:
            return 0  """



import unittest

class Test(unittest.TestCase): 
    # test function to test equality of two value 
    def test_positive(self): 
        firstValue = "geeks"
        secondValue = "geeks"
        # error message in case if test case got failed 
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(firstValue, secondValue, message) 
    
    def assert_equals(self,a,b): 
        # error message in case if test case got failed 
        message = "Some message!"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(a, b, message) 


def correct_title(string):
    string1 = string.lower()
    string1 = string1.title()
    Words2check = ["in","the","and","of"]
    separators = [" ","-"]
    LWCWords = []
    checkwords = []
    for word in Words2check:
        for sep in separators:
            checkwords.append(sep + word.title() + sep)
            LWCWords.append(sep + word.lower() + sep)
        
    for wordlistindex, testword in enumerate(checkwords):
        if string1.count(testword):
            string1 = string1.replace(testword,LWCWords[wordlistindex])

    return string1
# return the input text with the correct case
  
if __name__ == '__main__': 
    #unittest.main()
    Test.assert_equals(correct_title("sansa stark, lady of winterfell."), "Sansa Stark, Lady of Winterfell.")
    Test.assert_equals(correct_title("lord eddard stark, hand of the king."), "Lord Eddard Stark, Hand of the King.")
    Test.assert_equals(correct_title("jaime lannister, lord commander of the kingsguard."), "Jaime Lannister, Lord Commander of the Kingsguard.")
    Test.assert_equals(correct_title("varys, master of whisperers."), "Varys, Master of Whisperers.")
    Test.assert_equals(correct_title("doran martell, prince of dorne, lord of sunspear."), "Doran Martell, Prince of Dorne, Lord of Sunspear.")
    Test.assert_equals(correct_title("TYRION LANNISTER, HAND OF THE QUEEN."), "Tyrion Lannister, Hand of the Queen.")
    Test.assert_equals(correct_title("GRAND MAESTER PYCELLE."), "Grand Maester Pycelle.")
    Test.assert_equals(correct_title("EURON GREYJOY, KING OF THE IRON ISLANDS, LORD REAPER OF PYKE."), "Euron Greyjoy, King of the Iron Islands, Lord Reaper of Pyke.")
    Test.assert_equals(correct_title("PETYR BAELISH, LORD PROTECTOR OF THE VALE."), "Petyr Baelish, Lord Protector of the Vale.")
    Test.assert_equals(correct_title("MANCE RAYDER, KING-BEYOND-THE-WALL."), "Mance Rayder, King-Beyond-the-Wall.")
    Test.assert_equals(correct_title("jOn SnoW, kINg IN thE noRth."), "Jon Snow, King in the North.")
    Test.assert_equals(correct_title("Jeor MORMONT, Lord COMMANDER of the NIGHT'S WATCH."), "Jeor Mormont, Lord Commander of the Night's Watch.")
    Test.assert_equals(correct_title("cERSei LANnIStEr, QuEEn Of the aNdals and THE fIRSt men, PROtecTOR OF tHe SEVEN KInGdOmS."), "Cersei Lannister, Queen of the Andals and the First Men, Protector of the Seven Kingdoms.")
    Test.assert_equals(correct_title("DAeneRYS StOrmboRn oF hOuse TARGARYEn, ThE FirsT OF HER naMe, QUeEn OF The ANdAlS And THe FirsT mEN, PROtECtOr Of tHE SEven KinGDOmS, The MoTHeR of DrAGONS, thE KhALeEsi oF THE GReAt gRAss sEa, The UnburNT, The BReakEr of cHAInS."), "Daenerys Stormborn of House Targaryen, the First of Her Name, Queen of the Andals and the First Men, Protector of the Seven Kingdoms, the Mother of Dragons, the Khaleesi of the Great Grass Sea, the Unburnt, the Breaker of Chains.")