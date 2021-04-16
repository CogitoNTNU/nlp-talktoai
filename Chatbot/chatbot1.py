from transformers import pipeline, Conversation

print("printes dette") 

conversational_pipeline = pipeline("conversational")

print("printes dette her") 

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

def customConversation():
    
    customConv_input = input(">> ")
    
    customConv = Conversation(customConv_input)
    
    conversational_pipeline([customConv])

    while customConv_input != "bye":
        print(customConv)
        
        customConv_input = input(">> ")
        customConv.add_user_input(customConv_input)
        conversational_pipeline([customConv])
     
customConversation()
    

