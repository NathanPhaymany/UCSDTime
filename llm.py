from transformers import pipeline

# Set up the pipeline for question answering
pipe = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Context for question answering
context = "The Apollo program was the third human spaceflight program carried out by NASA."

# Ask a question related to the context
question = "What org carried out the third human spaceflight?"

question_refinement_context = ""

# Get the answer using the pipeline
answer = pipe(question=question, context=context)

# Print the answer
print(f"Question: {question}")
print(f"Answer: {answer['answer']}")
print(f"Score: {answer['score']}")