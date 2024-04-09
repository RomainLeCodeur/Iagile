from transformers import pipeline
pipe = pipeline("text-classification", model="lighteternal/fact-or-opinion-xlmr-el")

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("lighteternal/fact-or-opinion-xlmr-el")
model = AutoModelForSequenceClassification.from_pretrained("lighteternal/fact-or-opinion-xlmr-el")
classifier = pipeline("text-classification",model=model,tokenizer=tokenizer)



def scoreFact(text):
    var=classifier(text)[0]
    return str(var['score'])