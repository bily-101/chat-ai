import os
import aiml

dump = "main.dump"

k = aiml.Kernel()

if os.path.exists(dump):
    print("Loading from dump: " + dump)
    k.loadBrain(dump)
else:
    print("Fixing...")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving dump: " + dump)
    k.saveBrain(dump)

while True:
    input_text = input("> ")
    response = k.respond(input_text)
    print(response)
