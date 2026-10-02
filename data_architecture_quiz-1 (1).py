# Data Architecture Quiz
# Topics: Data Lake, Data Warehouse, Data Mart, OLAP Cube

questions = [
    {
        "question": "Which store holds raw, unprocessed data?",
        "options": ["Data Mart", "Data Warehouse", "Data Lake", "Database"],
        "answer": "Data Lake",
    },
    {
        "question": "Which system is ideal for business reporting and analytics?",
        "options": ["Data Lake", "Data Warehouse", "Data Mart", "Data Hub"],
        "answer": "Data Warehouse",
    },
    {
        "question": "Which serves a specific business function or department?",
        "options": ["Data Lake", "Data Warehouse", "Data Mart", "Data Mesh"],
        "answer": "Data Mart",
    },
    {
        "question": "Which platform supports machine learning and predictive analysis best?",
        "options": ["Data Lake", "Data Mart", "Data Warehouse", "OLAP Cube"],
        "answer": "Data Lake",
    },
    {
        "question": "Data mart derives data mainly from:",
        "options": ["Data Lake", "Data Warehouse", "Data Fabric", "Data Catalog"],
        "answer": "Data Warehouse",
    },
]

def run_quiz():
    score = 0
    print("\n=== Data Architecture Quiz ===\n")

    for number, item in enumerate(questions, start=1):
        print(f"{number}. {item['question']}")
        for i, option in enumerate(item["options"], start=1):
            print(f"   {i}. {option}")

        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if 1 <= choice <= 4:
                    break
                print("Please enter a number from 1 to 4.")
            except ValueError:
                print("Please enter a valid number.")

        selected = item["options"][choice - 1]
        if selected == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {item['answer']}\n")

    print(f"Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
