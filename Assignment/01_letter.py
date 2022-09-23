print("Welcome to the Letter Counter")
name = input("What is your name: ")

print("Hello " + name + "!")
print("I will count number of time that a  specific letter occurs in a message.")
p = input("Enter your message: ")

if "H".lower() == "h":

      letter_count = (p.count("h"))

print(f" {name} Your message has {letter_count}h's in it." )




