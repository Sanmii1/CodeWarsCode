def product_fib(_prod):
    # variable initialization
    n1 = 0
    n2 = 1
    n3 = 1

    # Looping to find prod n1 and n2 and check the result is it the same in input value?
    while True :
       # Save Value as list
       list_number = [n1,n2,n3]
       # Looping for fibonacci numbers
       for i in range(len(list_number)-1) :
          product = list_number[i] * list_number[i+1]
          # Check the value is it the same in input value?
          if product == _prod :
              return [list_number[i],list_number[i+1],True]
          elif product > _prod :
              return [list_number[i],list_number[i+1],False]

       n1 += n2
       n2 += n3
       n3 = n1 + n2
      
