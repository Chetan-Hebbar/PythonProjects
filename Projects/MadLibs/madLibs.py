import re,pathlib,pyinputplus


def GrabPlaceholders(templatestr):
    madlibregex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
    return madlibregex.findall(templatestr)


def RecordUserEntries(placeholderlist):
    responselist = []
    for entry in placeholderlist:
        while True:
            response=input('Please provide a ' + str(entry) + ':\n')
            if response.isalpha():
                break
        responselist += [response]
    return responselist


# Overall Steps:
# Read reference template file. TODO: Improvement, offer a couple different generic choices for the user to choose

# Reference file will live in C:/Users/Chetan
TemplateFile = open('C://Users//Chetan//MadlibTemplates//Template1.txt')
TemplateContents = TemplateFile.read()

# Grab the list of inputs we need from the template file
placeholderlist = GrabPlaceholders(TemplateContents)

# Prompt the user for inputs

inputlist = RecordUserEntries(placeholderlist)

# Replace the placeholder texts with the responses given by the user

for i in range(len(placeholderlist)):
    placeholderregex=re.compile(placeholderlist[i])
    TemplateContents=placeholderregex.sub(inputlist[i],TemplateContents,1)

# Share the new madlib with the user
print('Here\'s your Madlib:\n' + TemplateContents)
TemplateFile.close()

# Write that contents of the filled somewhere, and tell the user where they can reference it.
output=pathlib.Path('C:/Users/Chetan/MadlibTemplates/output.txt')
output.write_text(TemplateContents)