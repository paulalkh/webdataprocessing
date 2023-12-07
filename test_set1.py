# test_set.py

questions = [
    "What is the capital of Japan?",
    "Who is the author of 'To Kill a Mockingbird'?",
    "Explain the process of photosynthesis.",
    "What are the main features of Python programming language?",
    "When was the Declaration of Independence signed?",
    "Compare and contrast classical conditioning and operant conditioning.",
    "List the planets in our solar system in order of distance from the sun.",
    "What are the benefits of regular exercise?",
    "Describe the concept of artificial intelligence.",
    "How does the Internet work?",
    "What is the significance of the Mona Lisa painting?",
    "Who won the Nobel Prize in Physics in 2020?",
    "Explain the principles of supply and demand in economics.",
    "What are the health benefits of meditation?",
    "Discuss the impact of climate change on the environment.",
    "Who is the current president of Brazil?",
    "Solve the quadratic equation: ax^2 + bx + c = 0",
    "What is the process of mitosis in cell division?",
    "List three major components of the human respiratory system.",
    "What is the meaning of life?"
]

with open("test_set.txt", "w") as file:
    for i, question in enumerate(questions, 1):
        file.write(f"question-{i}\t{question}\n")
