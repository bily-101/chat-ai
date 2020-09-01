import os
import aiml



dump = "main.dump"

k = aiml.Kernel()

if os.path.exists(dump):
    print("Pulling information from the dump: " + dump)
    k.loadBrain(dump)
else:
    print("Fixing...")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving information in the dump")
    k.saveBrain(dump)

while True:
    input_text = input("> ")
    response = k.respond(input_text)
    print(response)
