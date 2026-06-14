import sys # give info about python like version etc or os info and command line arguments
import subprocess # allows python to run terminal cmds like pip list, git status or python main.py

print(f"Python version: {sys.version}")
result = subprocess.run(
    ["pip", "list"],
    capture_output =True, # save output instead of only showing it
    text=True # convert output into normal string
)
print(result.stdout)
with open('installed.txt', 'w') as f: # open file with with statement generally close file automatically
    f.write(result.stdout) # write data
print("Saved to installed.txt") # final msg