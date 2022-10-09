Masha Allah, atlast solved the problem.

Today, i was learning selenium, page no 283 of the book 'automate the boring stuff using python'
pip installed selenium
installed mozilla firefox
first command worked. 'from selenium import webdriver'
but the second command did not.
checked stack overflow and got the answer. something called geckodriver should have been installed.
downloaded geckodriver but it should be in the PATH
what is the path, changed the path in the view advanced setting -> environment variables
then everything gone. could not even use pip.
Tried various method whole day to fix the path to its previous configuration.
failed
failed
failed.
then did quit as there was no time.
then again tried after few hours. Now came across a different method. SYSTEM RESTORE.
DID
SUCCESS
but now the 'from selenium import webdriver' command which was already working did not work.
installed firefox
but still selenium did not work
uninstalled selenium and re-installed.
now fine.
In the mean time, while undergoing system restore search.
found a way to know the path. successfully copy-pasted geckodriver in the path.
it works. the next line. 
'browser = webdriver.Firefox()'
Masha Allah.


