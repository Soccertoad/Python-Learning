#   String: stored letter or text
#       Single line: '' or ""  and '' '' or "" ""
#       Multiline: ''' ''' or """ """
#       Escaping: ignoring quotes using \
#       Embedding: A value you want to add later %s
#       Multiplying: makes string apear multiple times

singleString = 'Hello World'
print(singleString)

multiString = '''This is a multiline string.
Isn't this cool!! '''
print(multiString)

escaping = 'I\'d say \'\'s in text is cool '
print(escaping)

user = 'player1'
myPoints = 1000
embedding = "%s scored %s points"
print(embedding % (user, myPoints))

aLot = 10 * 'a'
print(aLot)

print() 

#   Syntax arrangment and order of words
#   SyntaxError: Something different then python was expecting
#       EOL: End Of Line

#   List: Multiple strings and/or number together
#   Lists can hold lists
#       Can call a specific string using index position
#       Index Position: [] starts at 0
#       Printing Parts of Lists
#           {List}[x:x] From Position to another not including its self
#   Editing Lists
#       .append()
#       del {list}[Index]
#   Mathematics
#       +: adds lists together
#       *: number of times it appears
#       - and /: result in errors

wizardList = ['Spider Legs', 'Toe of Frogs', 'Eye of Newt', 'Bat Wing', 'Slug Butter', 'Snake Dandruff']
print(wizardList)
print(wizardList[2])
print(wizardList[2:5])

numberString = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
numbers = [1, 2, 3, 4, 5,]
letters = ['A', 'B', 'C', 'D', 'E']

numbers.append(6)
letters.append('F')


listOfList = [numbers, letters]
print(listOfList)

del numbers[1]
del letters[1]

print(listOfList)

#   Tuples: uses parentheses and cant be changed
#       Uses Index Position
fibS = (0, 1, 1, 2, 3)
print(fibS[3])

#   Maps: store information together
#       Key : value
#       Can call exact location using Key
#   Editing Maps
#       Use key to change value
numberToLetter = {
    1 : 'A', 2 : 'B',
    3 : 'C', 4 : 'D'
}
print(numberToLetter)
print(numberToLetter[1])

numberToLetter[1] = 'Z'