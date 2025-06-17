from tqdm import tqdm
import time

# The progress bar can be used for any kind of loop

for i in tqdm(range(30)):
    time.sleep(0.05) 

# For a file:
with open("progress_bar.py", "r") as f:
    lines = f.readlines()
    for line in tqdm(lines, total=len(lines), unit='lines'):
        # This is where the line would be processed
        time.sleep(0.05)  


# For a more complex loop or a set of operations, 
#   manually control the progress bar:
progress = tqdm(total=100)
for i in range(10):
    time.sleep(0.1)
    progress.update(10)
progress.close()