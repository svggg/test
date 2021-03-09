s = input().split()
fin = ''

for i in range(len(s)):
    counter = 0
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            counter += 1
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            if 97 <= ord(s[i][j]) + counter <= 122 or 65 <= ord(s[i][j]) + counter <= 90:
                fin += chr(ord(s[i][j]) + counter)

            else:
                if s[i][j] == s[i][j].lower():
                    fin += chr(96 + (counter - (122 - ord(s[i][j]))))

                else:
                    fin += chr(64 + (counter - (90 - ord(s[i][j]))))

        else:
            fin += s[i][j]
    fin += ' '
print(fin)
