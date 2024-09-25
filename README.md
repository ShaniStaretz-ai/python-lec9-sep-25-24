# python-lec8-sep-22-24

## Subjects learnt today:

1) None vs 0: we put None when we don't have the init value.
 
   explanation:
    
    0-counter of something - we know it starts from the minimus=0. 

    None - we don't know the smallest player, because it doesn't start from 0, 0 is a valid value
    
    Therefore, if we know , we can ask: do we know the init value? is 0 is a valid value?
2) list continue:
   * sum: basic function receive the list and returns the sum of it's values
   * for-each: 
     * same as for loop, but without iterator, simple gives the value, replaces arr[i]:
     * using it when we don't care about the iterator, the location of the value in the list
     ```
     for num in numbers:
        print(number)
     ```
     * same as in str: because str is a list of characters
      ```
     for letter in "hello": 
         print(letter)
     ```
   * extend list (concat list  to the current):
      ```
     newL=list+[4,5,6]
     list.expend([4,5,6])
      ```
      ** list1+list2-> returns a new  list
      ** extend function changes the current list
## Extra:

1) syntax shortcuts:
   * arr== True= len(arr)==True=len(arr)>0 - if the list is not empty