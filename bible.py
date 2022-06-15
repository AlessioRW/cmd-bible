import urllib.request, os, sys


specChar = [
        ['\\xe2\\x80\\x99',"'"],
        ['\\xe2\\x80\\x9c','"'],
        ['\\xe2\\x80\\x9d','"'],
        ['\\xe2\\x80\\x94','—']
        ]


def getPage(link):
    html = (str(urllib.request.urlopen(link).read()))
    html= html.replace('>','<')
    html = html.split('<')
    return html


def NIV(link):
    html = getPage(link)


    textRange = []
    read = False
    for i in html:
        if 'en-NIV' in i:
            read=True
        if 'il-text' in i:
            break
        if read == True:
            textRange.append(i)

    text = []
    newLine = False
    for i in range(len(textRange)):
        tempText = textRange[i]
        if '/span' in tempText or '/sup' in tempText or 'woj' in tempText:
            printText = textRange[i+1]

            for char in specChar:
                printText = printText.replace(char[0],char[1])
            
            if len(printText) >= 3:
                text.append(printText)
                
        if '/p' in tempText:
            text.append('\n')
            text.append('\n')
        
    finalText = ''
    for i in text:
        finalText += i
        
    print(finalText)


def KJV(link):
    html = getPage(link)

    textRange = []
    read = False
    for i in html:
        if 'passage-text' in i:
            read=True
            
        if 'passage-scoller' in i:
            break
        
        if read == True:
            textRange.append(i)


    text = []
    newLine = False
    for i in range(len(textRange)):
        tempText = textRange[i]
        if '/span' in tempText or '/sup' in tempText or 'woj' in tempText:
            printText = textRange[i+1]

            for char in specChar:
                printText = printText.replace(char[0],char[1])
            
            if len(printText) >= 3:
                text.append(printText)
                
        if '/p' in tempText:
            text.append('\n')
            text.append('\n')
        
    finalText = ''
    for i in text:
        finalText += i
        
    print(finalText)

def printBooks():
    oldTest=['Genesis', 'Exodus',
                 'Leviticus', 'Numbers',
                 'Deuteronomy', 'Joshua',
                 'Judges', 'Ruth',
                 '1 Samuel', '2 Samuel',
                 '1 Kings', '2 Kings',
                 '1 Chronicles', '2 Chronicles',
                 'Ezra', 'Nehemiah',
                 'Esther', 'Job',
                 'Psalm', 'Proverbs',
                 'Ecclesiastes', 'Song of Songs',
                 'Isaiah', 'Jeremiah',
                 'Lamentations', 'Ezekiel',
                 'Daniel', 'Hosea',
                 'Joel', 'Amos',
                 'Obadiah', 'Jonah',
                 'Micah', 'Nahum',
                 'Habakkuk', 'Zephaniah',
                 'Haggai', 'Zechariah',
                 'Malachi']

        
    x = 0
    line = '|'
    print((' '*15)+'--------------|Old Testament|--------------\n')
    for i in range(len(oldTest)):
        if x == 3:
            line += '|'
            print(line)
            x = 0
            line = '|'
        line += oldTest[i]
        if x < 2:
            line += ' '*(30-len(oldTest[i]))
        else:
            line += ' '*(13-len(oldTest[i]))
        
        x += 1

    print()
    newTest = ['Matthew','Mark',
               'Luke','John',
               'Acts','Romans',
               '1 Corinthians','2 Corinthians',
               'Galatians','Ephesians',
               'Philippians','Colossians',
               '1 Thessalonians','2 Thessalonians',
               '1 Timothy','2 Timothy',
               'Titus','Philemon',
               'Hebrews','James',
               '1 Peter','2 Peter',
               '1 John','2 John',
               '3 John','Jude',
               'Revelation']

    x = 0
    line = '|'
    print((' '*15)+'--------------|New Testament|--------------\n')
    for i in range(len(newTest)):
        if x == 3:
            line += '|'
            print(line)
            x = 0
            line = '|'
        line += newTest[i]
        if x != 2:
            line += ' '*(30-len(newTest[i]))
        else:
            line += ' '*(13-len(newTest[i]))
        x += 1

    

link = 'https://www.biblegateway.com/passage/?search='
inp = ''.join(sys.argv[1:]).lower()
os.system('cls')
deafult = '&version=NIV'

if 'niv' in inp:
    inp = inp.replace('niv','')
    inp=inp.split(' ')
        
    for i in inp:
        link += i
        link += '+'
            
    link+='&version=NIV'
    NIV(link)

elif 'kjv' in inp:
    inp = inp.replace('kjv','')
    inp=inp.split(' ')
        
    for i in inp:
        link += i
        link += '+'
            
    link+='&version=KJV'
    KJV(link)

elif 'book' in inp:
    printBooks()

elif 'help' in inp.lower():
    print('Type books to list all valid books')
else:
    inp=inp.split(' ')
        
    for i in inp:
        link += i
        link += '+'
            
    link+='&version=NIV'
    NIV(link)
