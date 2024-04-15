


from transformers import(
    AutoTokenizer,
    AutoConfig,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer
)
output_dir = "path_to_save_model/"
from peft import PeftModel,PeftConfig, get_peft_model, LoraConfig
config = PeftConfig.from_pretrained(output_dir)
model = AutoModelForSequenceClassification.from_pretrained(config.base_model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(output_dir)
model = PeftModel.from_pretrained(model,output_dir)

#label1 factualité
#label0 opinion

# Use a pipeline as a high-level helper
from transformers import pipeline

classifier = pipeline("text-classification",model=model,tokenizer=tokenizer)
var=classifier("The earth is flat")[0]
print(var['label'])

def scoreFact(text):
    var=classifier(text)[0]
    return str(var['score'])
