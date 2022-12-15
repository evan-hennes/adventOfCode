from useful import convertToVar

homework = convertToVar('test.txt', '\n')

'''
function is nested (num, pair)
    if num [pair] is nested
        return True
    else
        return False

function check pairs (num)
    for pair in num
        if pair is nested * 4
            return True
    return False

def check numbers (num)
    for regular number in num
        if regular number > 10
            return True
    return False

function is reduced (num)
    if checkPairs (num) or checkNumbers (num)
        return False
    else
        return True

function explode (num)
    if checkPairs (num)
        for pair in num
            explode index = index of leftmost pair
            if explode index - 1 is regular number
                num [left explode index - 1] += pair
            if explode index + 1 is regular number
                num [right explode index + 1] += pair
            num [explode index] = 0
    return num

function split (num)
    if checkNumbers
        for regular number in num
            split index = index of leftmost pair
            split pair = empty pair
            left index of split pair = floor of regular number / 2
            right index of split pair = ceil of regular number / 2
            num [split index] = split pair
    return num

function reduce (num)
    while not isReduced
        explode (num)
        split (num)

function add (list of nums)
    new num = []
    for num in nums
        new num += num #added as new pair
    reduced new num = reduce (new num)
    return reduced new num

TODO: write pseudocode/figure out what function calculate magnitude should do/how it should work
'''