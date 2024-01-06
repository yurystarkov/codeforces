from re import sub

num, interview = int(input()), input()

parasite = r"ogo(go)+|ogo"

print(sub(parasite, "***", interview))
