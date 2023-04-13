name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith('From '): 
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

max_email = None
max_count = None
for email,count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(max_email, max_count)
