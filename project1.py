'''

8/5/2019


##  Factorial. Industry or math? ##


In math, you have the factorial operator ('!')

You multiply the number with all it's preceding numbers from n..1

i.e.
5! = 5 * 4 * 3 * 2 * 1 = 120
8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320


The task is to help the great minds of today by giving them code to run their calculations for them

Things to consider:
factorial(0) = 1 <- special case
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
... and so on

'''






def factorial(n):
    result = 1

    # You fill in the code here to return a correct result

    return result











# test the results - you can simply run the code to test the function you made works correctly
error_hit = False
if factorial(0) != 1:
    print 'function failed: 0'
    error_hit = True
if factorial(1) != 1:
    print 'function failed: 1'
    error_hit = True
if factorial(2) != 2:
    print 'function failed: 2'
    error_hit = True
if factorial(5) != 120:
    print 'function failed: 5'
    error_hit = True
if factorial(8) != 40320:
    print 'function failed: 8'
    error_hit = True

if not error_hit:
    print 'You did it!'