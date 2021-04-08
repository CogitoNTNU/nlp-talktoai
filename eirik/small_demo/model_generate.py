#heavily inspired by the tutorial at: https://www.youtube.com/watch?v=cHymMt1SQn8

from transformers import GPT2LMHeadModel, GPT2Tokenizer

#load model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2', pad_token_id=tokenizer.eos_token_id) #what token to pad text

def return_blog_post(user_theme):
    #tokenize input sentence
    input_ids = tokenizer.encode(user_theme, return_tensors="pt") #identifiers, return pytorch tensors
    
    #generate takes to following inputs: input identifiers, mac length of output (100 words), number of beams(how many search trees),
    #sequences of 2 can only repeat once, earlystopping - stop when output stops making sense
    output = model.generate(input_ids, max_length = 50, num_beams = 5, no_repeat_ngram_size = 2, early_stopping = True)

    #de-tokenize and return
    return tokenizer.decode(output[0], skip_special_tokens=True)
