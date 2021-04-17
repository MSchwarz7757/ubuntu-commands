''' Ubuntu Commands'''
import random

''' creates a dictionary with all excercises with question as keys and answers as values '''
def createExcercises():
    global exercise_list
    exercise_list = {}

    question_pos = 0
    temp_pos= ""

    exercise_file = open("aufgaben_ubuntu.txt", "r")
    
    #Go trough file and seek for questions (uppercase lines)
    for line in exercise_file:
        question_pos+=1
        #Create key in dict for found question with empty value/answer
        if(line.isupper()):
            exercise_list[line] = ""
            temp_pos = line
        #Append line to value/answer of key/question
        elif(line != "\n"):
            exercise_list[temp_pos] += str(line)
    
    exercise_file.close()

''' generates the exercises and variables '''
def init():
    createExcercises()

    global old_questions
    old_questions = []

    global wrong_questions
    wrong_questions = []

    global max_commands
    max_commands = len(exercise_list)

    global max_points
    max_points = max_commands

    global successes
    successes = 0

''' start the game '''
init()
print("{} gefundene Fragen --- Viel Erfolg!\n".format(max_commands))
while True:
	#Reset tries
    tries= 1
    
    #Choose random question
    questions, answers = random.choice(list(exercise_list.items()))
    if max_commands >= len(old_questions):
        #Choose new question if already asked
        while questions in old_questions and max_commands != len(old_questions):
            questions, answers = random.choice(list(exercise_list.items()))
        
        #Print question
        print("Frage Nr: {}".format(len(old_questions)+1)) # +1 because the len starts with 0
        print("\033[36m{}\033[0m".format(questions[:-2])) # -2 to remove the \n

        #Save question into old_questions
        old_questions.append(questions)
        
        #Ask for answer
        while True:
            answer = str(input("Antwort: "))
            
            #Correct answer
            if(answer in answers and answer not in "" and answer not in " "):
                #Count only as a success if it's the first time the question is answered
                if(questions not in wrong_questions):
                    successes+=1
                
                #Print solution
                print("\n\033[95mRichtig!\n"+"\033[0m"+"Die Lösung ist: "+answers)
                print("------------------------------------------------------------------------------------------------------\n")
                break
            else:
            	#No tries left for current question
                if(tries == 3):
                    #Remove question from old_questions so it'll be asked again
                    old_questions.remove(questions)
                    wrong_questions.append(questions)
                    
                    #Print solution
                    print("\033[31m"+"Hier die richtige Antwort: "+"\033[0m"+answers)
                    print("------------------------------------------------------------------------------------------------------\n")
                    break
                #Some tries left for current question
                else:
                    tries+=1
                    print("\n\033[31mFalsch!"+"\033[36m"+"\n"+questions+"\033[0m")
            continue
            
	#All questions have been answered
    else:
        successes = 0
        old_questions = []

        #Print result
        print("Sie haben {} von {} Fragen richtig beantwortet".format(successes,max_points))
        print("\nNächste Runde!\n")
