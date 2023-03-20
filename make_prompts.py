import os
import sys
import json
import re
from generate_instruction import encode_prompt

def encode_prompt(task_dict):
    (instruction, input, output) = task_dict["instruction"], task_dict["input"], task_dict["output"]
    instruction = re.sub(r"\s+", " ", instruction).strip().rstrip(":")

    prompt = ''
    if input.lower() != '':
        prompt += f"### Instruction:\n{instruction}\n\n"
        prompt += f"### Input:\n{input}\n\n"
        prompt += f"### Response:"
    else:
        prompt += f"### Instruction:\n{instruction}\n\n"
        prompt += f"### Response:"

    return prompt


instructions = json.load(open('alpaca_data.json'))

data = {}
for i, d in enumerate(instructions):
    data[i] = encode_prompt(d)
    if i % 1000 == 0:
        print(data[i])

with open('formatted_instructions.json', 'w') as f:
    json.dump(data, f, indent=2)


