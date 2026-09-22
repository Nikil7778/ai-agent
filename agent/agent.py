import os
import json

from dotenv import load_dotenv
from groq import Groq

from tools import (
    read_tasks,
    find_tasks_before,
    check_task_status
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


tools = [
    {
        "type": "function",
        "function": {
            "name": "read_tasks",
            "description": "Read the student's private task data.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_tasks_before",
            "description": "Find tasks due before a specified date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in YYYY-MM-DD format"
                    }
                },
                "required": ["date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_task_status",
            "description": "Check the status of a student task.",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_name": {
                        "type": "string"
                    }
                },
                "required": ["task_name"]
            }
        }
    }
]


def execute_tool(name, arguments):

    if name == "read_tasks":
        return read_tasks()

    elif name == "find_tasks_before":
        return find_tasks_before(
            arguments["date"]
        )

    elif name == "check_task_status":
        return check_task_status(
            arguments["task_name"]
        )


messages = [
    {
        "role": "system",
        "content": """
You are a student task management AI agent.

The student's task information is private.

Use the available tools to access the private data.

Do not invent task information.

Use tools whenever necessary.
"""
    }
]


question = input(
    "What would you like to know about your tasks?\nYou: "
)

messages.append(
    {
        "role": "user",
        "content": question
    }
)


print("\n=== AI AGENT ===")


while True:

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if not message.tool_calls:

        print("\nFinal Answer:")
        print(message.content)

        break

    messages.append(message)

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        print("\nAgent selected tool:")
        print(tool_name)

        print("Arguments:")
        print(arguments)

        result = execute_tool(
            tool_name,
            arguments
        )

        print("\nTool result:")
        print(result)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            }
        )