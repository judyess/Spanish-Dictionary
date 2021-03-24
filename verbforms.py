#This program lets the user create a collection of verbs and their conjugations
#Folders are made for verb entries named in their inifinitive form
#Each folder has a text file for the imperative, present tense indicative and subjunctive verb forms
#The text files are read into an array which is accessed for the print display
#You can add verbs through the program or directly creating new folders in the root directory 
#You can edit the verbs through the program or simply opening the text file directly

#1. Menu display
#2. Calls next function based on user input for menu selection
#3. Asks user for the next verb they would like to act on.
    #If user enters 'menu', program resets selection and promps user with menu display again
    #If there is no input and user hits enter, then the program stops but does not exit shell. Exception occurs.



#(!!!)TO DO: Write exceptions for invalid selections and missing verbs (!!!)
#(!!!)TO DO: Display all folders in the root directory to view list of all existing verbs

import os
import sys
import tkinter
from tkinter import *
import tkinter.messagebox
import webbrowser

#Global parent directory (ADDRESS OF PROJECT FOLDER)
parent_dir=('C:\\Users\judys\Desktop\spanishverbs')

# -----@MAIN()
def main():
    user_input = input('1. Create new verb \n' +
                       '2. Access verb \n' +
                       '3. Edit verb \n')

    #TODO (!!!): MUST CATCH INVALID SELECTIONS HERE. INVALID SELECTIONS STILL EXECUTE OPTIONS() FUNCTION AND ERROR IS CAUGHT THERE.
    if not user_input:
        print("Select a valid option")
        main()
    else:
        options(user_input)

# -----@OPTIONS(USER_INPUT):
# ERROR WHEN NO INPUT ENTERED AFTER A VALID SELECTION IS MADE        
def options(user_input):
    os.chdir(parent_dir)
    verb = input('Enter verb: ')
    if user_input == '1':     
        create_verb(verb)
    elif user_input == '2':     
        go_to(verb)
    elif user_input == '3':  
        edit_verb(verb)
    else:
        print('error')
        main()

    nextt(user_input)


# -----@NEXTT(USER_INPUT):
#Menu addition that assumes user wants to repeat their selected option
    #Calls the option function again and sends the next verb input to the same selection
        #so the user doesn't have to keep re-entering number options if viewing/adding/editing multiple verbs back to back
def nextt(user_input):
    get_input = input('Next? ')
    if get_input == 'menu':
        main()
    elif not get_input:
        sys.exit("goodbye")
    else:
        if user_input == '1':
            os.chdir(parent_dir)
            create_verb(get_input)
        elif user_input == '2':
            go_to(get_input)
        elif user_input == '3':
            edit_verb(get_input)
        
    nextt(user_input)
    


# -----@CREATE_VERB(VERB):
#Creates a folder named after the verb and new text files for its conjugations
# Currently creates an __init__.py file,
    #which currently serves no purpose but may come in handy if I later want to add other capabilities that require me to import the folders as modules
def create_verb(verb):
    
  
    # Creates the folder inside the root directory
    directory = (verb)
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)


    #changes the current working directory to new verb folder 
    new_path = (parent_dir + '\\' + directory)
    os.chdir(new_path)
    
    # creates files inside the new verb folder (which is now the current working directory)
    filename = open('__init__.py','w')
    filename = open('present_indicative.txt', 'w')
    filename = open('present_subjunctive.txt', 'w')
    filename = open('imperative.txt', 'w')

    #resets path to parent directory 
    path = parent_dir

    
    
# -----@GO_TO(VERB):
#DISPLAYS VERB CONJUGATIONS
    #(!!!) TO DO: NEED TO WRITE EXCEPTIONS FOR VERBS THAT DONT EXIST (!!!)
def go_to(verb):
    new_path = (parent_dir + '\\' + verb)
    os.chdir(new_path)


    #CREATES SUBARRAYS OF THE ELEMENTS IN EACH TEXT FILE
    forms_array = []
    ind_subarray = ['INDICATIVE']
    sub_subarray = ['SUBJUNCTIVE']
    imp_subarray = ['IMPERATIVE']

    # ENCODING = 'UTF-8' --- TO CORRECTLY PRINT ACCENTED CHARACTERS
    with open('present_indicative.txt', encoding = 'utf-8') as my_file:
        my_file = [x.strip() for x in my_file]  #removes '\n' from displaying at endlines
        for line in my_file:
            ind_subarray.append(line)

    with open('present_subjunctive.txt', encoding='utf-8') as my_file:
        my_file = [x.strip() for x in my_file]
        for line in my_file:
            sub_subarray.append(line)

    with open('imperative.txt', encoding = 'utf-8') as my_file:
        my_file = [x.strip() for x in my_file]
        for line in my_file:
            imp_subarray.append(line)

    
    #APPEND THE SUBARRAYS TO A MAIN ARRAY
    person_array= [' ','1st-sl', '2nd-sl', '3rd-sl', '1st-pl', '2nd-pl', '3rd-pl']
    title_array = [' ','YO', 'TU' ,'UD.', 'NOSOTROS', 'VOSOTROS', 'UDS.']

    forms_array.append(person_array)
    forms_array.append(title_array)
    forms_array.append(ind_subarray)
    forms_array.append(sub_subarray)
    forms_array.append(imp_subarray)
  
    #PRINT THE MAIN ARRAY AND FORMAT LEFT JUSTIFIED WITH 16 CHAR SPACING
    for x in forms_array:
        print  (" ".join([str(l).ljust(16) for l in x]))
            

# -----@EDIT_VERB(VERB):
#OPENS TEXT FILES IN NOTEPAD
def edit_verb(verb):
    new_path = (parent_dir + '\\' + verb)
    os.chdir(new_path)
    webbrowser.open('present_indicative.txt')
    webbrowser.open('present_subjunctive.txt')
    webbrowser.open('imperative.txt')
main()
