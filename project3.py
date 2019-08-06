'''

8/5/2019


##  igpay. Latin..... ##



Write function that translates a text to Pig Latin and back.
English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding 'ay'.
"the quick brown fox" becomes "hetay uickqay rownbay oxfay".


For this project, assume no punctuation or capitalizations (only letters will be present)

'''


def to_pig_latin(text):

    # You fill in the code here to return a correct result
    pl_text = ''


    return pl_text


def to_english(text):

    # You fill in the code here to return a correct result
    e_text = ''

    return e_text








# test the results - you can simply run the code to test the function you made works correctly
error_hit = False
if to_pig_latin('the quick brown fox') != 'hetay uickqay rownbay oxfay':
    print 'function failed: to_pig_latin 1'
    error_hit = True
if to_english('hetay uickqay rownbay oxfay') != 'the quick brown fox':
    print 'function failed: to_english 1'
    error_hit = True
if to_pig_latin('all the words of my mouth are just none of them is crooked or perverse') != 'llaay hetay ordsway foay ymay outhmay reaay ustjay onenay foay hemtay siay rookedcay roay erversepay':
    print 'function failed: to_pig_latin 2'
    error_hit = True
if to_english('llaay hetay ordsway foay ymay outhmay reaay ustjay onenay foay hemtay siay rookedcay roay erversepay') != 'all the words of my mouth are just none of them is crooked or perverse':
    print 'function failed: to_english 2'
    error_hit = True

if not error_hit:
    print 'You did it!'
    print 'the quick brown fox', '->', to_pig_latin('the quick brown fox')
    print 'hetay uickqay rownbay oxfay', '->', to_english('hetay uickqay rownbay oxfay')
    print 'all the words of my mouth are just none of them is crooked or perverse', '->', to_pig_latin('all the words of my mouth are just none of them is crooked or perverse')
    print 'llaay hetay ordsway foay ymay outhmay reaay ustjay onenay foay hemtay siay rookedcay roay erversepay', '->', to_english('llaay hetay ordsway foay ymay outhmay reaay ustjay onenay foay hemtay siay rookedcay roay erversepay')