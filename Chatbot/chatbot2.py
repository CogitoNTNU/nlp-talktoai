from transformers import pipeline, Conversation

conversational_pipeline = pipeline("conversational")

customConv = ""

def firstConversation(text):
    global customConv
    customConv = Conversation(text)
    conversational_pipeline([customConv])
    return customConv.generated_responses[-1]

def nextConversation(text):
    global customConv
    if text == "bye":
        pass
    customConv.add_user_input(text)
    conversational_pipeline([customConv], num_return_sequences=1, repetition_penalty=1.2, top_k = 50, temperature = 0.6)
    return customConv.generated_responses[-1]
