import requests 
def add(a,b):
    return a+b 
def divide(a,b):
    return a/b
def greet(name):
    return "Hello, "+ name 
def multiply(a,b):
    return a*b
cities ={
    "troy":[42.61,-83.15],
    "detroit":[42.33,-83.05],
    "hyderabad":[17.38,78.48]
}
def get_weather(city):
    city=city.lower()
    if city not in cities:
        return "I don't know the city"+ city
    lat= cities[city][0]
    lon = cities[city][1]
    url = ("https://api.open-meteo.com/v1/forecast?latitude=" + str(lat)
           + "&longitude=" + str(lon)
           + "&current=temperature_2m&temperature_unit=fahrenheit")
    response=requests.get(url)
    if response.status_code != 200:
        return "weather API error:"+ str(response.status_code)
    data = response.json()
    temp = data["current"]["temperature_2m"]
    unit=data["current_units"]["temperature_2m"]
    return str(temp)+ unit
toolbox={"add":add,
         "divide": divide,
         "greet":greet,
         "multiply":multiply,
         "weather": get_weather}
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
        print("Agent: I dont have a tool called " + tool_name)
        continue

    chosen_tool = toolbox[tool_name]

    try:
        if tool_name == "greet" or tool_name== "weather":
            result= chosen_tool(parts[1])
        else:
            a= float(parts[1])
            b=float(parts[2])
            result = chosen_tool(a,b)
        print("Agent: " + str(result))
    except Exception as e :
        print("Agent: something went wrong- "+ str(e))