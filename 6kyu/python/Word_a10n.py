"""
The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").
Example
abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"
"""


"""
    WITHOUT USING REGEX
"""

def create_non_alph_lst(s):
    non_alph_lst = []
    na_char = ""
    for char in s:
        if not char.isalpha():
            na_char += char
        else:
            if len(na_char) > 0:
                non_alph_lst.append(na_char)
                na_char = ""
    if len(na_char) > 0:
        non_alph_lst.append(na_char)
    return non_alph_lst

def create_alpha_lst(s):
    alph_lst = []
    alp_char = ""
    for char in s:
        if char.isalpha():
            alp_char += char
        else:
            if len(alp_char) > 0:
                alph_lst.append(alp_char)
                alp_char = ""
    if len(alp_char) > 0:
        alph_lst.append(alp_char)
    return alph_lst
def abbreviate(s):
    word_lst =  create_alpha_lst(s)
    non_alph = create_non_alph_lst(s)
    while len(word_lst) > len(non_alph):
        non_alph += [""]

    lst = [(x[0] + str(len(x) - 2)+ x[-1]) if len(x) >= 4 else x for x in word_lst]
    return ''.join([(lst[i] + non_alph[i]) for i in range(len(lst))])


