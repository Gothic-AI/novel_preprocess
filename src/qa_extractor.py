from transformers import pipeline

# Load pre-trained models for Q&A and text generation
qa_pipeline = pipeline("question-answering")
text_generation_pipeline = pipeline("text-generation", model="gpt2")

# Define the context (a chunk of your novel text)
context = """
_3 may. bistritz._--left munich at 8:35 p. m., on 1st may, arriving at vienna early next morning; should have arrived at 6:46, but train was an hour late. buda-pesth seems a wonderful place, from the glimpse which i got of it from the train and the little i could walk through the streets. i feared to go very far from the station, as we had arrived late and would start as near the correct time as possible. the impression i had was that we were leaving the west and entering the east; the most western of splendid bridges over the danube, which is here of noble width and depth, took us among the traditions of turkish rule.
"""

# Function to generate questions based on the context
def generate_questions(context):
    # You could use a model like GPT-2 or T5 to generate possible questions for the context.
    question_prompt = f"Generate several questions based on the following text: {context}"
    questions = text_generation_pipeline(question_prompt, max_length=200, num_return_sequences=5)
    
    return [q['generated_text'].strip() for q in questions]

# Function to extract answers for each generated question
def extract_answers(context, questions):
    answers = []
    for question in questions:
        # Use a question-answering model to extract the answer from the context
        answer = qa_pipeline(question=question, context=context)
        answers.append(answer['answer'])
    return answers

# Step 1: Generate possible questions based on the context
questions = generate_questions(context)

# Step 2: Extract the corresponding answers for each generated question
answers = extract_answers(context, questions)

# Display Q&A pairs
for i, (q, a) in enumerate(zip(questions, answers)):
    print(f"Q{i + 1}: {q}")
    print(f"A{i + 1}: {a}\n")
