import os

challenge = int(input("What challenge do you want to access? : "))

if challenge < 10:
  file = "Challenge 0" + str(challenge) + ".py"
elif challenge == 24:
  file = "Challenge 24/Challenge 24.py"  # In a folder so it's different
else:
  file = "Challenge " + str(challenge) + ".py"

os.system(f'python "{file}"')
