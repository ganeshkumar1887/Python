def ask_question(question,answer):
    user_answer = input(question + " ")
    if user_answer.lower()==answer.lower():
        print("Correct Answer::")
    else:
        print(" incorrect Answer::")
def main():
    print("---welcome in Quiz game ---")
    ask_question("who is the current PM of India ?","Narendra Modi")
    ask_question("who is the current CM of India ?","Nitish kumar")
    ask_question("who was the First PM of India ?","Pd.Jawahar lal nehru")
    ask_question("who was the first President of India ?","Dr.Rajendra prasad")
    print("--Thanks for participant--")
    print("--Have a great day--")
    print("--Good bye--")
if __name__ =="__main__":
    main()