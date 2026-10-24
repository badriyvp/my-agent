def add(a,b):
    return a+b 
def divide(a,b):
    return a/b
def greet(name):
    return "Hello, "+ name 
def multiply(a,b):
    return a*b
toolbox={"add":add,
         "divide": divide,
         "greet":greet,
         "multiply":multiply}
while True:
    command = input("you: ")
    parts = command.split()

    if len(parts) == 0:
        print("Agent: type something")
        continue
    tool_name=parts[0]

    if tool_name == "quit":
        print("Agent:Bye!")
        break
    if tool_name not in toolbox:
        print("Agent: I dont have a tool" + tool_name)
        continue

    chosen_tool = toolbox[tool_name]

    try:
        if tool_name == "greet":
            result= chosen_tool(parts[1])
        else:
            a= float(parts[1])
            b=float(parts[2])
            result = chosen_tool(a,b)
        print("Agent: " + str(result))
    except Exception as e :
        print("Agent: something went wrong- "+ str(e))