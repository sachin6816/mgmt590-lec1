import pandas as pd
from transformers.pipelines import pipeline

hg_comp = pipeline('question-answering', model="bert-large-uncased-whole-word-masking-finetuned-squad", tokenizer="bert-large-uncased-whole-word-masking-finetuned-squad")

data = pd.read_csv('examples.csv')

for idx, row in data.iterrows():
    context = row['context']
    question = row['question']
    answer = hg_comp({'question': question, 'context': context})['answer']
    print(question, end='    ->   ')
    print(answer)
