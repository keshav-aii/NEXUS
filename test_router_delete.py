from core.command import Command
from core.router import process


cmd = Command("delete file test.txt")

result = process(cmd)

print(result)


cmd2 = Command("yes")

result = process(cmd2)

print(result)