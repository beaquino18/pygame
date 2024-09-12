first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #use f-strings to insert variables value into string
print(full_name)

message = f"Hello, {full_name.title()}"
line_break = "---------"

print(message)
print(line_break)

#adding tab using \t
print(f"\tHello, {full_name.title()}")
print(line_break)


#add new line using \n
print(f"Hello, \n {full_name.title()}")
print(line_break)

#one-line string and generate four lines of output
print("Languages:\n\tPython\n\tC\n\tJavascript")
print(line_break)

#remove whitespace right or left or all side of string
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(line_break)

#removing prefixes using removeprefix method
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

