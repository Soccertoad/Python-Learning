#   String: stored letter or text
#       String: Single line '' or ""  and '' '' or "" ""
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

#   Syntax arrangment and order of words
#   SyntaxError: Something different then python was expecting
#       EOL: End Of Line
