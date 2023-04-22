def mult_list(lst):
  if len(lst) == 0:
    print(0) 
  result = lst[0]

  if len(lst) > 1:
    for x in lst[1:]:
      result = result * x

  print (result)
    
mult_list([6,5,7])