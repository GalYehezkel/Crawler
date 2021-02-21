"""
*Gal Yehezkel
*315786228
*01- CS
*ass07
"""
import csv
"""
* Function Name: parser
* Input: string
* Output: list
* Function Operation: search for 'href=' and saves the html direction in a list,
                      then returns the list
"""
def parser(file):
    #list decleration
	ls=[]
    #finds in the string 'href=' and saves the index in start
	start=file.find('href=')
    #while there is still 'href=' in the string
	while (start!=-1):
        #finds what comes after 'href="' and save index to it
		start=file.find('"',start)+1
        #finds the next '"' in the string and saves it in end
		end=file.find('"',start)
        #adds the string between the first '"' and last '"' to the list
		ls.append(file[start:end])
        #search for the next 'href='
		start=file.find('href=',end)
    #sort the list
	ls.sort()
    #returns the list
	return ls
"""
* Function Name: crawler
* Input: string
* Output: none
* Function Operation: recusive function, gets a html title from the user input and puts in a dictionary
                      key(the input string) and values(where the content of the file direct to)
"""
def crawler(str):
    #open the file calls in what in str, and saves it's content in a string
	file= open(str,'r').read()
    #saves a key named the value of str and points to value of the returned list
	dictionary[str]=parser(file)
    #loop the runs on all values in the list that str key points to
	for j in dictionary[str]:
        #checks if the value j in the list has already a key in the dictionary
		if(dictionary.get(j)==None):
            #gets the values for that j and put it in the dictionary with that key
			crawler(j)

print('enter source file:')
#saves user input in str
str=input()
#global dictionary so we can add values to it in functions
global dictionary
#define of dictionary
dictionary={}
#inset keys and values to dictionary according to the html files
crawler(str)
#creates csv file and write to it rows
with open('result.csv', 'w',newline='') as f:
  writer = csv.writer(f)
  #loop on all the keys in dictionary
  for j in dictionary:
      #creates a list and puts in it the key 
      save=[j]
      #adds to the list the values of the key from the dictionary
      save.extend(dictionary[j])
      #add the list as a row to the csv file
      writer.writerow(save)
print('enter file name:')
#saves the input of the user
str=input()
#prints the values of the key from the dictionary and input legal
if(dictionary.get(str)!=None):
    print(dictionary[str])





