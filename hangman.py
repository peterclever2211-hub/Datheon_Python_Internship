# Datheon Python Internship - Task 1
# Intern: Peterclever Mmegwa | ID: DT-2026-K9SYK
import random
words = ["python","datheon","intern","github","asaba","scholar","coding","developer"]
word = random.choice(words)
guessed = ["_"]*len(word)
lives = 6
print("=== DATHEON HANGMAN ===")
print(f"Word: {' '.join(guessed)} ({len(word)} letters)")
while lives>0 and "_" in guessed:
    g=input("Enter letter: ").lower()
    if g in word:
        for i,c in enumerate(word):
            if c==g: guessed[i]=g
        print("Good!"," ".join(guessed))
    else:
        lives-=1
        print(f"Wrong! Lives left {lives}")
    if "_" not in guessed:
        print(f"YOU WIN! Word: {word}")
        break
else:
    print(f"GAME OVER! Word was {word}")