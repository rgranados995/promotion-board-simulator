# python board_simulator.py
def main():
    print("\nWelcome to Promotion Board Simulator")
    print("-----------------------------------\n")
    
    candidate_name = input("Enter your name: ")
    print(f"\nCandidate: {candidate_name.upper()}\n")
    
    # Basic question bank
    questions = [
        "Why should you be promoted?",
        "What does leadership mean to you?",
        "How do you maintain military bearing under stress?"
    ]
    
    for i, question in enumerate(questions, 1):
        input(f"{i}. {question}\nPress Enter to continue...")
    
    print("\nBoard deliberation...")
    print("\nConclusion: Thank you for your service. Dismissed!\n")

if __name__ == "__main__":
    main()