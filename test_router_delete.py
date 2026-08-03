from core.command import Command
from core.router import process
from brain.state_manager import get_pending


cmd = Command("delete file test123.txt")

result = process(cmd)

print(result)

print("PENDING:", get_pending())


cmd2 = Command("yes")

result = process(cmd2)

print(result)