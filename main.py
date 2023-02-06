text = "";
output = ""
charList = []
index = 0

# get input
text = input("text: ")

# loop through string and modify the char
for i in text:
  charList.insert(index, "||" + text[index] + "||")
  index += 1

# combind each string to form a big string 
for words in charList:
  output += words;

print(output)