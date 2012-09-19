import os
with open("images.txt", "r") as f:
    rows = f.readlines()
    for r in rows:
        target = r.strip()
        os.system("wget %s" % target)

