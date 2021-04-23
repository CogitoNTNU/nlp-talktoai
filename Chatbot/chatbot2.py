from transformers import pipeline, Conversation


conversational_pipeline = pipeline("conversational")

first = True

def convOneLine():
    conv1_start = "Let's watch a movie tonight - any recommendations?"
    conv2_start = "What's your favorite book?"

    conv1 = Conversation(conv1_start)
    conv2 = Conversation(conv2_start)

    conversational_pipeline([conv1, conv2])
    print(conv1)
    print(conv2)

def convToLines():
    conv1_next = "What is it about?"
    conv2_next = "Cool, what is the genre of the book?"

    conv1.add_user_input(conv1_next)
    conv2.add_user_input(conv2_next)
    
    conversational_pipeline([conv1, conv2])

    print(conv1)
    print(conv2)

def customConversation(text,first):
    if text == "bye":
        pass
    elif first == True:
        customConv = Conversation(text)
    
        conversational_pipeline([customConv])

        return customConv
    else:
        customConv.add_user_input(text)
        conversational_pipeline([customConv])
        return customConv 
     

    

