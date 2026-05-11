import json
import threading

def load_questions():
    with open("questions.json") as f:
        return json.load(f)
    
def load_highscores():
    try:
        with open("highscores.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
def save_highscore(name, score):
    highscores = load_highscores()
    highscores.append({"name": name, "score": score})
    highscores = sorted(highscores, key=lambda x: x["score"], reverse=True)
    with open("highscores.json", "w") as f:
        json.dump(highscores, f, indent=2)

def show_highscores():
    highscores = load_highscores()
    print("\n HIGH SCORES")
    if not highscores:
        print("No scores yet.")
    for i, entry in enumerate(highscores[:5], 1):
        print(f"{i}. {entry['name']} {entry['score']}")

def play_quiz():
    questions = load_questions()
    name = input("Enter your name: ")
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nq{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        print("⏲️ You have 5 seconds!")

        answer = [None]
        def get_input():
            answer[0] = input("Your answer (A/B/C/D):").upper()

        thread = threading.Thread(target=get_input)
        thread.start()
        thread.join(timeout=5)

        if answer[0] is None:
            print("⏲️ Time's up!")
        elif answer[0] == q["answer"]:
            print("✅Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Answer was {q['answer']}")

    print(f"\nGame over! {name} scored {score}/{len(questions)}")
    save_highscore(name, score)
    show_highscores()

play_quiz()
