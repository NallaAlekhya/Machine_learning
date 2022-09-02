#text_file = open('data.txt', 'r')
text = str("“I am a teacher and I love to inspire and teach people")

#cleaning
#text = text.lower()
words = text.split()
#words = [word.strip('.,!;()[]') for word in words]
#words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

#sort
#unique.sort()

#print
print(unique)
