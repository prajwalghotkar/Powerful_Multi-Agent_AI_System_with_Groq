# Powerful Multi-Agent AI System with Groq

## 1. Project Overview

`powerful_multi_agent_groq.ipynb` is a general-purpose Agentic AI project built with Groq, LangChain, and LangGraph Supervisor.

The project uses a supervisor-based multi-agent architecture. Instead of sending every user question to one agent, the system has three specialized agents:

- `general_agent` for normal knowledge, programming, AI, science, education, business, writing, and everyday questions
- `research_agent` for current, changing, niche, or web-verifiable information
- `math_agent` for mathematical and quantitative problems

The supervisor receives the user's request, determines which specialist is appropriate, delegates the task, and returns one final answer.

The notebook uses Groq through `ChatGroq` and the `openai/gpt-oss-120b` model. It does not require an OpenAI API key.

## 2. What This Project Actually Does

The core purpose is to demonstrate how an Agentic AI system can use multiple specialized agents instead of relying on a single fixed workflow.

A user can ask:

- "What is LangGraph?"
- "Explain machine learning."
- "Write a Python program to reverse a string."
- "What is 25% of 800?"
- "Calculate 500 minus 125, multiply the result by 4, and divide by 5."
- "What are the latest developments in generative AI?"
- "Search the web and explain a specific technology."
- "What is the difference between RAG and fine-tuning?"

The supervisor decides which specialist should handle the request.

## 3. High-Level Architecture

```text
                         USER
                           |
                           v
                    +-------------+
                    | SUPERVISOR  |
                    +-------------+
                      /    |    \
                     /     |     \
                    v      v      v
             GENERAL     RESEARCH   MATH
              AGENT       AGENT     AGENT
                |            |         |
                |            v         v
                |       DuckDuckGo   Math Tools
                |            |         |
                +------------+---------+
                             |
                             v
                       FINAL ANSWER
```

The supervisor is the routing layer. The specialists are the execution layer.

## 4. Why a Multi-Agent Architecture?

A single LLM can answer many types of questions, but a multi-agent architecture separates responsibilities.

```text
Normal question
    -> general_agent

Current information
    -> research_agent
    -> DuckDuckGo search

Mathematical calculation
    -> math_agent
    -> Math tools
```

This separation also makes the project easier to extend because additional specialist agents and tools can be added without redesigning the entire application.

## 5. Technologies Used

### Groq

Groq provides the LLM inference layer through `ChatGroq`.

The notebook configures:

```python
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=os.environ["GROQ_API_KEY"]
)
```

### LangChain

LangChain provides model and tool integration for the agents.

The project uses the current `create_agent` API rather than the older deprecated `create_react_agent` API.

### LangGraph Supervisor

`create_supervisor` provides the orchestration layer that manages the specialist agents.

### DuckDuckGo

The research and general-purpose agents can use DuckDuckGo search when external web information is useful.

### Python

Python functions are exposed as tools to the math agent.

## 6. Notebook Workflow

```text
1. Install dependencies
        |
2. Import libraries
        |
3. Configure Groq
        |
4. Create search and math tools
        |
5. Create research agent
        |
6. Create math agent
        |
7. Create general-purpose agent
        |
8. Create supervisor
        |
9. Compile application
        |
10. Test general question
        |
11. Test mathematical question
        |
12. Test current-information question
        |
13. Ask any question
```

## 7. Groq Configuration

The notebook asks for the Groq API key only when the `GROQ_API_KEY` environment variable is not already available.

```python
if not os.getenv("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")
```

The key should never be hard-coded into the notebook or committed to GitHub.

## 8. Web Search Tool

The project creates a web-search tool:

```python
search = DuckDuckGoSearchRun()

def search_web(query: str) -> str:
    """Search the web for current, factual, or topic-specific information."""
    return search.invoke(query)
```

The research agent can call this tool when information is:

- current
- changing
- niche
- difficult to answer reliably from model knowledge
- useful to verify externally

## 9. Math Agent

The math agent has dedicated tools instead of relying only on the language model to calculate.

Available tools:

| Tool | Purpose |
|---|---|
| `add` | Addition |
| `subtract` | Subtraction |
| `multiply` | Multiplication |
| `divide` | Division |
| `power` | Exponents |
| `modulus` | Remainder |
| `percentage` | Percentage calculation |
| `square_root` | Square root |

The agent can use multiple tools for a multi-step calculation.

Example:

```text
Calculate 20% of 500, multiply the result by 4, and add 50.
```

Expected calculation:

```text
20% of 500 = 100
100 x 4 = 400
400 + 50 = 450
```

The important Agentic AI concept is that the model can decide to invoke the required tools instead of treating the calculation as plain text generation.

## 10. General-Purpose Agent

The `general_agent` is intended for broad questions such as:

- AI
- machine learning
- programming
- technology
- science
- education
- business
- writing
- concepts
- everyday questions

It also has access to web search when specialized or current information is required.

## 11. Research Agent

The `research_agent` specializes in information retrieval and verification.

Its main tool is:

```text
search_web
```

For a question such as:

```text
What are the latest major developments in generative AI?
```

the supervisor can route the request to the research agent, which can use DuckDuckGo to obtain current information before producing the answer.

## 12. Supervisor

The supervisor is the central orchestration component.

It manages:

```text
general_agent
research_agent
math_agent
```

Its routing instructions are based on the type of user request.

Conceptually:

```text
if normal/general question:
    use general_agent

if current/niche/web-verifiable question:
    use research_agent

if mathematical/quantitative question:
    use math_agent

if the question combines multiple capabilities:
    use the required specialists
```

The supervisor is also instructed to return one clear final answer instead of exposing internal routing information or tool calls.

## 13. What Makes This an Agentic AI Project?

This project demonstrates several important Agentic AI concepts:

### Tool Use

Agents can invoke external tools instead of generating every answer directly.

### Specialized Agents

Different agents have different responsibilities.

### Dynamic Routing

The supervisor decides which agent should handle the request.

### Multi-Step Execution

An agent can perform multiple tool operations when required.

### Orchestration

The supervisor coordinates multiple agents into one application.

### Separation of Responsibilities

Research, mathematical calculation, and general reasoning are separated into different components.

## 14. Example End-to-End Flows

### Example A: General Question

```text
User
  |
  v
Supervisor
  |
  v
General Agent
  |
  v
Final Answer
```

### Example B: Mathematical Question

```text
User
  |
  v
Supervisor
  |
  v
Math Agent
  |
  v
Math Tool
  |
  v
Final Answer
```

### Example C: Current Information

```text
User
  |
  v
Supervisor
  |
  v
Research Agent
  |
  v
DuckDuckGo
  |
  v
Research Agent
  |
  v
Final Answer
```

### Example D: Combined Task

A question can require more than one capability. For example:

```text
Find a current numerical fact and calculate something using it.
```

The supervisor can use the research capability to obtain the information and the math capability for the calculation.

## 15. Installation

Run the notebook from the first cell.

The dependency cell installs:

```bash
pip install -U langchain-groq langchain langgraph langgraph-supervisor langchain-community ddgs
```

Then enter your Groq API key when prompted.

## 16. Running the Project

Open:

```text
powerful_multi_agent_groq.ipynb
```

Run the cells from top to bottom.

The final cell provides an interactive interface:

```python
question = input("Ask anything: ")
```

You can enter any supported question and the supervisor will route it to the appropriate agent.

## 17. Important Project Variables

| Variable | Purpose |
|---|---|
| `model` | Groq LLM |
| `search_web` | Web-search tool |
| `add` | Addition tool |
| `subtract` | Subtraction tool |
| `multiply` | Multiplication tool |
| `divide` | Division tool |
| `power` | Power tool |
| `modulus` | Modulus tool |
| `percentage` | Percentage tool |
| `square_root` | Square-root tool |
| `research_agent` | Web research specialist |
| `math_agent` | Mathematics specialist |
| `general_agent` | General-purpose specialist |
| `workflow` | Supervisor workflow |
| `app` | Compiled multi-agent application |

## 18. Security

Never place a real API key directly into source code.

Avoid:

```python
GROQ_API_KEY = "your-real-api-key"
```

Use the environment variable or secure input method already implemented in the notebook.

If the project is pushed to GitHub, make sure the API key is not included in the repository.

## 19. Project Limitations

This is a learning and demonstration project, not a production autonomous system.

Important limitations include:

- Web-search results depend on the search provider.
- Current information should still be verified for high-stakes use.
- The language model can still make reasoning mistakes.
- Tool selection depends on model behavior and supervisor instructions.
- The mathematical tools cover common arithmetic operations, not every area of mathematics.
- No persistent memory or long-term user profile is implemented.
- No authentication, monitoring, rate limiting, or production deployment layer is included.

## 20. Future Extensions

The architecture can be extended with additional specialist agents and tools.

Possible extensions include:

```text
Coding Agent
SQL Agent
Data Analysis Agent
RAG Agent
Document Agent
Vision Agent
Email Agent
Calendar Agent
Finance Agent
API Agent
```

The supervisor can then become the orchestration layer for a much larger Agentic AI system.

## 21. Final Project Summary

`powerful_multi_agent_groq.ipynb` demonstrates a supervisor-based multi-agent architecture where a user interacts with one system while specialized agents handle different classes of tasks.

The main flow is:

```text
User Query
    |
    v
Supervisor
    |
    +---- General Agent
    |
    +---- Research Agent ---- DuckDuckGo
    |
    +---- Math Agent -------- Math Tools
    |
    v
Final Response
```

The key idea is not simply using an LLM to answer a question. The project demonstrates how an Agentic AI system can:

1. Understand the user's request.
2. Decide which capability is required.
3. Delegate the task to a specialist.
4. Use tools when necessary.
5. Perform multi-step work.
6. Return a clean final response.

This makes the notebook a practical demonstration of LLM tool use, specialized agents, dynamic routing, supervision, and multi-agent orchestration.
