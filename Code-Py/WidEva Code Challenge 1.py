Code Challenge 1 :
Read the question slowly, carefully and multiple times if necessary.

Write a python code, lets call it find_best_matching_list.py, which will match input list with randomnly generated lists, and print matching or closely matching lists.
- generate "x" lists, each containing "y" unique random alphabets (a-z). x and y should be passed as arguments to the program.
- Unique implies that each list should have unique elements. Obviously, one element(or alphabet) can occur in multiple lists.
- prompt for input, which should accept comma or space separated set of small case alphabets. Ignore alphabets more than 10. If input has upper case, convert to lower case
- find the list that best matches the input letters, with matching percentage.
100% means all input matches a single list. If 4 out of 5 input letter matches a particular list, it is a 80% match.
The input list could match with multiple lists, and hence each should be reported with the match. The matching list should be printed in descending order of matching percentage.
To verify, print the matching list, highlighting the matched alphabets, by any means.
- handle exceptions as necessary
- assume that this is a module of a big project. Code maturity counts!


Eg,
# python find_best_matching_list.py 20 10
Enter letters (a-z) :   a,b, h,l,p

list1 matches 40% :  [ /a/, /b/, d, f, y, i, k, /l/, u, q ]
list3 matches 20% :  [ /a/ , z, u, /l/, o, w, f ]
