#   Addition: +
#   Subtraction: -
#   Multiplication: *
#   Division: /

#   Order of Operations
#   Parenthese: ()
#       Can be Nested (Inside Eachother)
 
#   Variables are like Lables
#       Holds numbers, text, lists of numbers and text
#       Use = sign to create

#   Coin Program
foundCoins = 20 # Coins started with
magicCoins = 10 # Coins that appear each day
stolenCoins = 3 # Coins that get stolen each week

totalCoins = foundCoins + magicCoins * 365 - stolenCoins * 52
print(totalCoins)