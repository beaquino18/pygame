wizard = "Harry Potter"
print(f"Hello {wizard}, would you like to learn some Python today?")

print(wizard.lower()) #all lowercase
print(wizard.upper()) #all uppercase
print(wizard.title()) #first letter of the word upper case

quote = "'It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.' by Albus Dumbledore"
print(quote)

famous_wizard ="Albus Dumbledore"
quote2 = "'It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.' by "
print(f"{quote2} {famous_wizard}") #string literal f" "

wizard2 = " Ron"
print(wizard2.lstrip()) #leading whitespace removed

wizard3 = "Ron "
print(wizard3.rstrip()) #trailing whitespace removed

wizard4 = " Ron "
print(wizard4.rstrip()) #trailing only

filename = "wizard_notes.txt"
print(filename.removesuffix(".txt")) #remove suffix, output "wizard_notes"