secret_word="Power"
print("What is it that you seek ?")
guess=input("I seek ")
guess_limit=3
guess_count=0
out_of_guesses=False
while guess!=secret_word and not out_of_guesses:
    if guess_count<guess_limit:
        print("No,Guess again.")
        guess=input("")
        guess_count=guess_count+1
    else:
        out_of_guesses=True
if out_of_guesses:
    print("You lack clarity.")
else:
    print("Adhbut !")
