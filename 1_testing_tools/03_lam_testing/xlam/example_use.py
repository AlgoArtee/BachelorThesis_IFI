import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.random.manual_seed(0)

model_name = "Salesforce/xLAM-1b-fc-r"

# Initialize tokenizer and model
print("Initializing tokenizer and model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    device_map="auto", 
    torch_dtype="auto", 
    trust_remote_code=True
)
print("Tokenizer and model initialized.")

# Add a distinct pad token if not present
print("Adding special pad token...")
tokenizer.add_special_tokens({'pad_token': '<PAD>'})
model.resize_token_embeddings(len(tokenizer))
print("Pad token added and model embeddings resized.")

# Task and format instructions
print("Setting up task and format instructions...")
task_instruction = """
You are an expert in composing functions. You are given a question and a set of possible functions. 
Based on the question, you will need to make one or more function/tool calls to achieve the purpose. 
If none of the functions can be used, point it out and refuse to answer. 
If the given question lacks the parameters required by the function, also point it out.
""".strip()

format_instruction = """
The output MUST strictly adhere to the following JSON format, and NO other text MUST be included.
The example format is as follows. Please make sure the parameter type is correct. If no function call is needed, please make tool_calls an empty list '[]'.
```
{
    "tool_calls": [
    {"name": "func_name1", "arguments": {"argument1": "value1", "argument2": "value2"}},
    ... (more tool calls as required)
    ]
}
```
""".strip()
print("Task and format instructions set up.")

# Define the input query and available tools
query = "What's the weather like in New York in fahrenheit?"

print("Defining available tools...")
get_weather_api = {
    "name": "get_weather",
    "description": "Get the current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, New York"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "The unit of temperature to return"
            }
        },
        "required": ["location"]
    }
}

search_api = {
    "name": "search",
    "description": "Search for information on the internet",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query, e.g. 'latest news on AI'"
            }
        },
        "required": ["query"]
    }
}

openai_format_tools = [get_weather_api, search_api]
print("Available tools defined.")

# Helper function to convert OpenAI format tools to xLAM format
def convert_to_xlam_tool(tools):
    print("Converting tools to xLAM format...")
    if isinstance(tools, dict):
        return {
            "name": tools["name"],
            "description": tools["description"],
            "parameters": {k: v for k, v in tools["parameters"].get("properties", {}).items()}
        }
    elif isinstance(tools, list):
        return [convert_to_xlam_tool(tool) for tool in tools]
    else:
        return tools

# Helper function to build the input prompt for the model
def build_prompt(task_instruction: str, format_instruction: str, tools: list, query: str):
    print("Building prompt...")
    prompt = f"[BEGIN OF TASK INSTRUCTION]\n{task_instruction}\n[END OF TASK INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF AVAILABLE TOOLS]\n{json.dumps(xlam_format_tools)}\n[END OF AVAILABLE TOOLS]\n\n"
    prompt += f"[BEGIN OF FORMAT INSTRUCTION]\n{format_instruction}\n[END OF FORMAT INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF QUERY]\n{query}\n[END OF QUERY]\n\n"
    print("Prompt built.")
    return prompt

# Build the input and start inference
print("Converting tools and building input...")
xlam_format_tools = convert_to_xlam_tool(openai_format_tools)
content = build_prompt(task_instruction, format_instruction, xlam_format_tools, query)

messages = [
    { 'role': 'user', 'content': content}
]

print("Tokenizing input...")
# Tokenize input with padding and attention mask
inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    return_tensors="pt", 
    padding=True
).to(model.device)
print("Input tokenized.")

print("Generating output...")
# Generate output with appropriate parameters
outputs = model.generate(
    **inputs, 
    max_new_tokens=512, 
    do_sample=False, 
    num_return_sequences=1, 
    attention_mask=inputs["attention_mask"],  # Explicitly pass the attention mask
    eos_token_id=tokenizer.eos_token_id
)
print("Output generated.")

# Decode and print the model's output
print("Decoding output...")
print(tokenizer.decode(outputs[0][len(inputs["input_ids"][0]):], skip_special_tokens=True))
print("Decoding completed.")

