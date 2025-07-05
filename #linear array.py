#linear array
def linear_array(arr,target):
  for index,value in enumerate(array):

    if value == target:
      print('we found the value ',value)
      break
array = (10,20,30,40,5,88,7)
array = list(map(int,input().split()))
target = int(input(40))
linear_array(array,target)