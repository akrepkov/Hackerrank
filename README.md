**Minion_game.py**

Kevin and Stuart want to play the 'The Minion Game'.
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
Scoring
A player gets +1 point for each occurrence of the substring in the string 


**Split_str_&_remove_dubl.py**

You have a string of length n and an integer k, where k divides evenly into n. 
You can split the string #into n/k equal parts, each with k characters. 
For each part, remove any duplicate characters while #keeping the original order. 
Finally, print each of these unique segments on a new line.


**Dictionary_sort.py**

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
Explanation of Sorting Options

sorted(dict.items(), key = lambda item:(item[1], item[0])) - value ascending, after that key ascending

sorted(dict.items(), key = lambda item:(-item[1], item[0])) - value descending, key ascending

sorted(dict.items(), key = lambda item:(-item[1], item[0]), reverse = True) - value ascending, key descending

sorted(dict.items(), key = lambda item:(-item[1], item[0]), reverse = True) - value descending, key descending