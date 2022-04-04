import re,pathlib,os


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

def GetTemplateFromUser():
    while True:
        user_input = input("Enter the path of your MadlibTemplate: ")
        pathaddress=pathlib.Path(user_input)
        if not os.path.exists(pathaddress):
            print("Couldn't find the file!")
            continue
        break
    return user_input

# Overall Steps:

# Validate that the madlib file has tokens to replace
while True:
    filePath = GetTemplateFromUser()
    TemplateFile = open(filePath)
    TemplateContents = TemplateFile.read()

    # Grab the list of inputs we need from the template file
    placeholderlist = GrabPlaceholders(TemplateContents)
    if len(placeholderlist) ==0 :
        print("Your file didn't have any MadLib tokens.\n")
        continue
    break
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
# TODO: Ask user what the filename should be called?
writedirectory=os.path.dirname(filePath)
output=pathlib.Path(writedirectory / pathlib.Path('output.txt'))
output.write_text(TemplateContents)

print("Output saved to "+str(output))