#DAY 1:
- Write a function called add_checker that accepts two arguments.
- The first argument is a list containing at least two integers. 
- The second argument is an integer.
- The add_checker function should return True if there are two integers in the list of integers (first argument) that when added together, equals the integer passed in as the second argument.
- If there are no two integers in the list that sum up to equal the second argument, add_checker should return false.

#DAY 2:
- You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

- Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

```
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
```
-For 4 or more names, the number in and 2 others simply increases.

