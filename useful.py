import math

def sieveOfEratosthenes(num):
  # make boolean list of all numbers up to num 
  boolList = [True for i in range(num)]
  boolList[0], boolList[1] = False, False
  p = 2
  # start @ smallest prime
  while p ** 2 < num + 1:
    if not boolList[p]:
      p += 1
      continue
    # i starts @ p^2, goes to num, inc by p
    for i in range(p**2, num, p):
      boolList[i] = False #marks nums as not prime
    p += 1
  # creates tuple list of index (int), primeness (bool) and adds to list if primeness is True
  numList = [index for index, primeness in enumerate(boolList) if primeness]
  return numList
# end function seiveOfEratosthenes

def isPalindrome(num):
  digitList = makeDigitList(num)
  for i in range(len(digitList) // 2): # checks half of digit list instead of repeating
    if digitList[i] != digitList[-i-1]: # checks symmetrical indexes
      return False
  return True
# end function isPalindrome

def makeDigitList(num):
  digitList = []
  while num > 0:
    digitList.append(num % 10) # gets the last digit
    num //= 10 # gets the first digit
  digitList.reverse()
  return digitList
# end function makeDigitList

def divisibleByAll(upper):
  num = upper # num will be final answer
  divisibility = False
  while divisibility == False:
    for i in range(1, upper + 1):
      if num % i != 0: # checks every number up to upper
        num += upper # increase by upper every time
        break
      if i == upper: # when i reaches upper, that's the answer
        divisibility = True
  return num
# end function divisibleByAll

def checkPythag(a, b, c):
  a = a ** 2
  b = b ** 2
  c = c ** 2
  if a + b == c:
    return True
  else:
    return False
# end function checkPythag

def pythagGen(lim):
  c, m = 0, 2
  while c < lim:
    for n in range(1, m):
      a = m * m - n * n
      b = 2 * m * n
      c = m * m + n * n
      if c > lim:
        break
      print(a, b, c)
    m += 1
# end function pythagGen

def convertToMatrix(lst, matrixLen):
  # returns list from i to i + matrixLen for i in range 0 to matrixlen, inc by matrixlen
  return [lst[i:i + matrixLen] for i in range(0, len(lst), matrixLen)]
# end function convertToMatrix

def checkNumDivisors(num):
  numDivisors = 0
  if math.sqrt(num).is_integer():
    numDivisors += 1
  for i in range(1, int(math.sqrt(num))):
    if num % i == 0:
      numDivisors += 2
  return numDivisors
# end function checkNumDivisors

def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  fib = [None] * (n + 1)
  fib[1] = 1
  fib[2] = 1
  for i in range(3, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
  return fib[n]
# end function fibonacci

def maxTriangleSum(triangle):
  for i in reversed(range(len(triangle))):
    for j in range(len(triangle[i]) - 1):
      x1 = triangle[i][j]
      x2 = triangle[i][j + 1]
      y = triangle[i - 1][j]
      s = 0
      if y + x1 > y + x2:
        s = y + x1
      else:
        s = y + x2
      triangle[i - 1][j] = s
  return triangle[0][0]
# end function maxTriangleSum

def phi(n):
  relPrimes = 0
  for i in range(1, n):
    if math.gcd(i, n) == 1:
      relPrimes += 1
  return relPrimes
# end function phi

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
# end function factorial

def phiSieve(num):
  # make list of all numbers up to num 
  phiList = [i for i in range(num + 1)]
  p = 2
  # start @ smallest prime
  while p <= num:
    if phiList[p] == p: # number is prime
      # i starts @ p * 2, goes to num, inc by p
      for i in range(p * 2, num + 1, p):
        phiList[i] *= 1 - (1 / p) # multiplies to remove multiples of p from num
      phiList[p] -= 1 # phi of prime number is itself minus 1
    p += 1
  phiList = [round(phi) for phi in phiList]
  return phiList
# end function phiSeive

def checkDivisors(num):
  divisors = []
  if math.sqrt(num).is_integer():
    divisors.append(int(math.sqrt(num)))
  for i in range(1, int(num / 2) + 1):
    if num % i == 0 and i != math.sqrt(num):
      divisors.append(i)
  return divisors
# end function checkDivisors

def maxMatrixSum(m):
  for i in reversed(range(len(m) - 1)):
    m[len(m) - 1][i] += m[len(m) - 1][i + 1]
    m[i][len(m) - 1] += m[i + 1][len(m) - 1]
  for i in reversed(range(len(m) - 1)):
    for j in reversed(range(len(m) - 1)):
      x1 = m[i][j]
      x2 = m[i][j + 1]
      y = m[i + 1][j]
      # print(x1, x2, y)
      if x1 + x2 < x1 + y:
        s = x1 + x2
      else:
        s = x1 + y
      m[i][j] = s
  return m[0][0]
# end function maxMatrixSum

def convertToVar(file, splitChar):
  var = open(file, "r")
  var = var.read()
  var = var.split(splitChar)
  return var
# end function convertToVar

def t(n):
  triNum = (n / 2) * (n + 1)
  return triNum
# end function t

def isPrime(num):
  if math.sqrt(num).is_integer():
    return False
  for i in range(1, int(math.sqrt(num))):
    if num % i == 0:
      return False
  return True
# end function isPrime

def p(n):
  pentNum = (n * (3 * n - 1)) / 2
  return pentNum
# end function p

def h(n):
  hexNum = n * (2 * n - 1)
  return hexNum
# end function h

def unicodeConverter(numLst):
  numLst = numLst.split(',')
  decrypted = ""
  for num in numLst:
    num = int(num)
    decrypted += chr(num)
  return decrypted
# end function unicodeConverter

def rotations(n):
  n = list(str(n))
  rots = []
  rots.append(int(''.join(n)))
  for d in n:
    n = n[1:] + [n[0]]
    #print(n)
    rots.append(int(''.join(n)))
  return rots
#end function rotations

def decToBin(num, beInt = False):
  if beInt:
    return int(bin(num).replace('0b', ''))
  return bin(num).replace('0b', '')
#end function decToBin

def checkAllIndices(lst, item):
    if lst.count(item) == len(lst):
        return True
    else:
        return False
#end def checkAllIndices