'''

8/5/2019


##  Banner Time! ##



The king needs banners to be posted all around the kingdom.  However, the previous scribe couldn't format the text correctly


Here is an example banner

*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********


The task is to find the length of the longest string in the text that the king needs.
Using spaces, pad until it's the proper length, then use * to frame the banner

Hints:
Kings are JUSTIFIED in their rule you might even say ljust


'''

def create_banner(text_list):
    formatted_banner_list = []

    #  You fill in the code here to return a correct result


    # find length of longest word
    longest_word_len = 0
    for word in text_list:
        if len(word) > longest_word_len:
            longest_word_len = len(word)


    # banner header all the *'s
    formatted_header = ''
    # +4 is to offset the padding
    for i in range(longest_word_len+4):
        formatted_header += '*'
    formatted_banner_list.append(formatted_header)

    # banner words
    for word in text_list:
        formatted_word = '* ' + word.ljust(longest_word_len) + ' *'
        formatted_banner_list.append(formatted_word)

    # banner footer (can reuse header)
    formatted_banner_list.append(formatted_header)

    return formatted_banner_list


banner_list1 = ['The', 'King', 'and', 'his', 'men', 'request', 'meat!']
banner_list2 = ['But','since','you','refuse','to','listen','when','I','call','and','no','one','pays','attention','when','I','stretch','out','my','hand']





#==========================================================================================================================================================

# test results
error_hit = False
if create_banner(banner_list1) != [
                                 "***********"
                                ,"* The     *"
                                ,"* King    *"
                                ,"* and     *"
                                ,"* his     *"
                                ,"* men     *"
                                ,"* request *"
                                ,"* meat!   *"
                                ,"***********"]:
    print 'function failed: banner_list1'
    error_hit = True
if create_banner(banner_list2) != [
                                 "*************"
                                ,"* But       *"
                                ,"* since     *"
                                ,"* you       *"
                                ,"* refuse    *"
                                ,"* to        *"
                                ,"* listen    *"
                                ,"* when      *"
                                ,"* I         *"
                                ,"* call      *"
                                ,"* and       *"
                                ,"* no        *"
                                ,"* one       *"
                                ,"* pays      *"
                                ,"* attention *"
                                ,"* when      *"
                                ,"* I         *"
                                ,"* stretch   *"
                                ,"* out       *"
                                ,"* my        *"
                                ,"* hand      *"
                                ,"*************"]:
    print 'function failed: banner_list2'
    error_hit = True


if not error_hit:
    print 'You did it!'
    print '\n'.join(create_banner(banner_list1))
    print '\n'.join(create_banner(banner_list2))

