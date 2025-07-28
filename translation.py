from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_to_hindi(text):
    tokens = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")
    translation = model.generate(**tokens)
    hindi = tokenizer.decode(translation[0], skip_special_tokens=True)
    return hindi
