def verbing(s):
  length = len(s)

  if length > 2:
    if s[-3:] == 'ing':
      s += 'ly'
    else:
      s += 'ing'

  return s

def not_bad(s):
  snot = s.find('not')
  sbad = s.find('bad')

  if sbad > snot:
    s = s.replace(s[snot:(sbad+3)], 'good')

  return s

def front_back(a, b):
  alength = len(a)
  blength = len(b)

  if alength % 2 == 0:
    aindex = alength // 2
  else:
    aindex = (alength // 2) + 1

  if blength % 2 == 0:
    bindex = blength // 2
  else:
    bindex = (blength // 2) + 1

  afront = a[0:aindex]
  aback = a[aindex:]

  bfront = b[0:bindex]
  bback = b[bindex:]

  return afront + bfront + aback + bback


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()


  


