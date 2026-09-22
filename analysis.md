# Day 1 – Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The private-data scenario selected for this project is a Personal Student Task Assistant.

The system contains private student task information such as task name, due date, and task status. The data is stored locally in a JSON file named `tasks.json`.

The sample private data contains the following tasks:

- DSA Practice – Due: 2026-09-24 – Pending
- Machine Learning Assignment – Due: 2026-09-25 – Pending
- AI Agent Day 1 Task – Due: 2026-09-26 – Pending
- GitHub Project – Due: 2026-09-28 – Pending

The same user request is used to compare all three approaches:

> "What tasks do I have to complete before September 26?"

The purpose is to demonstrate the difference between a plain chatbot, a rule-based workflow, and an AI agent when working with the same problem and private data.

---

## 2. Plain Chatbot

The first approach is a plain chatbot using a Groq-hosted language model.

The chatbot receives the user's question and sends it to the language model. The model generates a natural-language response.

The plain chatbot does not have a tool for reading the student's private `tasks.json` file. Therefore, it cannot directly retrieve the student's private task information from the local data source.

### Data Used

The chatbot uses the user's question as its input. It does not directly access the private task database or JSON file.

### Tools Used

No external tools are used.

The main component is the language model.

### Process

The process is:

User request → Language Model → Generated Response

The chatbot can understand and generate natural-language responses, but it does not independently perform operations on the private task data.

### Limitation

The main limitation in this scenario is private-data access. Since the chatbot does not have a tool connected to the student's task data, it cannot reliably retrieve the actual tasks from `tasks.json`.

---

## 3. Rule-Based Workflow

The second approach is a rule-based workflow.

Unlike the chatbot, this system directly reads the student's private `tasks.json` file and applies predefined programming rules.

The workflow does not use an LLM.

### Data Used

The workflow uses the private task data stored in `data/tasks.json`.

### Tools and Rules Used

The system uses predefined programming logic:

1. Read the task data.
2. Read the date provided by the user.
3. Convert the dates into a comparable format.
4. Compare each task's due date with the requested date.
5. Display tasks whose due date is before the specified date.

### Process

The process is:

User date → Read JSON → Apply predefined rules → Filter tasks → Display result

For example, when the user enters `2026-09-26`, the workflow checks each task and displays the tasks due before that date.

### Limitation

The main limitation is flexibility. The workflow works according to predefined conditions. If the user asks a more complex question that is not covered by the programmed rules, additional rules or code have to be created.

---

## 4. AI Agent

The third approach is an AI agent using a Groq language model together with tools and a loop.

The AI agent has access to tools that can read and process the student's private task data.

The agent can determine which tool is required for the user's request, execute the tool, observe the result, and then continue processing until it can provide a final answer.

### Data Used

The agent uses the student's private task information stored in `data/tasks.json`.

### Tools Used

The project provides tools such as:

- `read_tasks()` – reads the private task data.
- `find_tasks_before(date)` – finds tasks due before a specified date.
- `check_task_status(task_name)` – checks the status of a particular task.

### Process

The agent follows this general process:

User request → Groq LLM → Select tool → Execute tool → Observe result → Groq LLM → Final response

For example, when the user asks:

> "What tasks do I have to complete before September 26?"

the agent can select the `find_tasks_before()` tool, provide the required date, receive the matching tasks, and then generate the final response.

### Limitation

The agent depends on both the language model and the tools. Incorrect tool selection or incorrect interpretation of a request can affect the result. The tools must also be implemented correctly and have appropriate access to the required private data.

---

## 5. Comparison Table

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Can understand natural-language questions but has limited access to the private task data | Limited to predefined rules and conditions | Can handle different requests by selecting appropriate tools |
| Decision-making | Generates a response using the language model | Follows predefined programming conditions | Uses the language model to decide which tool or action is required |
| Tool usage | No tools | Uses fixed program operations | Uses tools selected during the agent process |
| Private-data access | Does not directly access `tasks.json` | Directly reads `tasks.json` | Accesses private data through tools |
| Multi-step task handling | Mainly generates a response | Performs predefined steps | Can perform multiple tool calls and continue until the task is completed |
| Automation | Limited | High for predefined tasks | High for tasks that can be handled by available tools |
| Reliability | Depends on the generated response and available information | Predictable when the rules are correctly defined | Depends on both the language model and correct tool execution |

---

## 6. Suitability Analysis

For the Personal Student Task Assistant scenario, the three approaches demonstrate different capabilities.

The plain chatbot is useful for natural-language interaction and general responses, but it does not directly access the student's private task data in this implementation.

The rule-based workflow can reliably process the task data when the required operation is already defined. For example, comparing due dates and filtering tasks can be performed using fixed programming conditions.

The AI agent can combine language-model reasoning with tools that access the private task data. It can interpret the user's request, select an appropriate tool, receive the tool result, and produce a final response.

Therefore, the AI agent demonstrates the capabilities required for requests involving natural-language understanding, private-data access, tool usage, and multiple steps. However, its operation also depends on the correct implementation of the tools and the language model.

---

## 7. Conclusion

A plain chatbot, a rule-based workflow, and an AI agent solve problems in different ways.

A plain chatbot is appropriate when the main requirement is natural-language interaction, explanation, or content generation and direct access to external tools or private data is not required.

A rule-based workflow is appropriate when the problem has clear and predictable conditions. It can provide consistent results when the required steps and rules are known in advance.

An AI agent is appropriate when a problem requires natural-language understanding together with access to tools, private data, and multiple steps. The agent can use the language model to determine actions, use tools to obtain information, observe the results, and continue processing until the task is completed.

This project demonstrates these differences using the same Personal Student Task Assistant scenario and the same private task data.