print ("hello_world")

import math

def median(input):

    input.sort()
    lengthList = len(input)
    middleList = math.floor(lengthList / 2)

    if lengthList % 2 == 0:
        return (input[middleList - 1] + input[middleList]) / 2
    else:
          return input[middleList]

list1 = [0, 3, 5, 7, 10, 11, 32, 87, 100, 999]
print (median(list1))
test_list = [12, 7, 22, 5, 13, 9, 18]
print (median(test_list))
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))
