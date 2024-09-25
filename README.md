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
     * if you still want the index and the item :
      ```
     for index, color in enumerate(colors):
      ```
   * extend list (concat list  to the current):
      ```
     newL=list+[4,5,6]
     list.expend([4,5,6])
      ```
      ** list1+list2-> returns a new  list
   
      ** extend function changes the current list
   * pop - remove the last item in the list
     
     ** pop(index)- remove the item by its index.
   * delete - remove an item, without returning value.
        ** remove by list[start,end,steps], or by index
        ```
        del list1[1]
        del list1[1:7:2]
        ```
   * remove - remove item from list by value
    
     ** if exist more than 1 time in th list, will remove the first one it finds.
   * clear - function tha clean the list:l1.clear()==l1=[] (same but different...)
   * index - by given value return its first index : l1.index(99)
       ** before remove() or index(), verify the value in list
   * count - by given value, will return how many times the value is in the list
   * l2=l1: copy by reference, same in the memory, 2 points on the same list, works only on saved data structures and not primitive parameters.
   * copy: copy by values. save a new location in the memory. l2=l1.copy()
   * sort - list.sort(): 
     * optional parameters in the function:
       * key= A function to specify the sorting criteria(s)
       * reverse, boolean: list.sort(reverse=True)
## Extra:

1) Syntax shortcuts:
   * arr== True= len(arr)==True=len(arr)>0 - if the list is not empty
   * 99 in list = returns True if the value 99 exist in the list, else return false, same char in string
2) upper: function on string than changes the characters to uppercase:
    ```
    uperString=string.upper()
    ```