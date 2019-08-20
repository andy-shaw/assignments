'''

8/29/2019

## Length of the Range ##





We use the range and len python functions all the time, but to peep under the hood, we're going to make our own.




'''



def my_len(obj):
    n = 0


    return n


def my_range(start, end):
    r = []


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