#USE_GPU = False
#Bare nødvendig i visse versjoner av tensorflow
# if USE_GPU:
#     import tensorflow as tf
#     physical_devices = tf.config.list_physical_devices('GPU')
#     tf.config.experimental.set_memory_growth(physical_devices[0]), True)

from transformers import pipeline, Conversation, GPT2TokenizerFast, GPT2LMHeadModel
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
conversational_pipeline = pipeline("conversational")

######vConversationv#######

conv1_start = "Let's watch a movie tonight, any recommendations?"

conv1 = Conversation(conv1_start)

conversational_pipeline([conv1])

conv1_next = "What is it about?"

conv1.add_user_input(conv1_next)

conversational_pipeline([conv1])

while conv1_next != "bye":
    print(conv1)
    conv1_next = input()
    conv1.add_user_input(conv1_next)
    print(conversational_pipeline([conv1]))
