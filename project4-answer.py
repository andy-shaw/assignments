'''

8/29/2019

## Length of the Range ##





We use the range and len python functions all the time, but to peep under the hood, we're going to make our own.


len simply counts the items of the list/string/array/etc
'hello' has 5 letters so len('hello') is 5
[123,51,99] has 3 numbers so len([123,51,99]) is 3



range(start, end) returns an array of numbers starting with start and ending before end
notation for this is [0..3)  -> start at 0 and stop before 3
range(0,3) = [0,1,2]

python's built in range function assumes that it will start at 0 if you do not supply a parameter
range(3) = [0,1,2]

our range function will have a start and an end parameter
my_range(0,3) = [0,1,2]


'''



def my_len(in_item):
    '''return how many items are in in_item'''
    n = 0

    for e in in_item:
        n += 1

    return n


def my_range(start, end):
    '''return array containing the numbers between start and end'''
    r = []

    i = start
    while i < end:
        r.append(i)
        i += 1

    return r










# test the results - run the code to test the function you made
error_hit = False
if my_len('hello world') != len('hello world'):
    print 'my_len function failed: hello world'
    error_hit = True
if my_len([1,2,3]) != len([1,2,3]):
    print 'my_len function failed: [1,2,3]'
    error_hit = True
if my_range(0,5) != range(0,5):
    print 'range function failed: 0,5'
    error_hit = True
if my_range(22,50) != range(22,50):
    print 'range function failed: 22,50'
    error_hit = True


if not error_hit:
    print 'You did it!'