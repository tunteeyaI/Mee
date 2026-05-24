from groq import generate_response
def main():
    print('Welcome to Chatty. Ask Anything!')
    vague=input('Enter a non-clear prompt:')
    print("\n Chatty's response to a non-clear prompt\n")
    print(generate_response(vague))
    clear=input("Enter a much more clearer prompt:")
    print("\nChatty's response to a clearer prompt\n")
    print(generate_response(clear))
main()
import requests
import html #didplay html content
import random #generate random questions
import keyboard
def get_questions(amount=10,category=9):
    url=f"https://opentdb.com/api.php?amount={amount}&category={category}&type=multiple"
    response=requests.get(url)
    if response.status_code!=200:#the request was unsuccessful
        print("Sorry couldn't get the questions")
        return []
    else:
        #convert the data to json
        data=response.json()
        #return the results
        return data['results']
#display the questions
def display_quiz(questions):
    score=0
    #display each questions
    for i,question in enumerate(questions):
        #print the questions
        print(f"Question {i+1}: {html.unescape(question['question'])}")
        #get the correct answer
        correct_answer=html.unescape(question['correct_answer'])
        wrong_answers=[html.unescape(ans) for ans in question['incorrect_answers']]
        #combine and shuffle answers
        options=wrong_answers+[correct_answer]
        random.shuffle(options)
        print("\nOptions:",options)
        #get user answer
        user_answer=input('Enter your answer here')
        if user_answer.strip().lower()==correct_answer.strip().lower():
            print("Correct Answer!\n")
            score+=1
        else:
            print(f"Wrong answer! The correct answer was: {correct_answer}\n")
    print(f"Your final score is: {score}/{len(questions)}")
    if keyboard.is_pressed('q'): #stopping the programq
            print("Program stopped by keyboard.")
if __name__=="__main__":
    display_quiz(get_questions())
