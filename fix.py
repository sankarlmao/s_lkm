import re
with open("/home/sankar/github/s_lkm/monitor.c", "r") as f:
    content = f.read()

content = re.sub(r"filename\[sizeof\(filename\) - 1\] = .*;", "filename[sizeof(filename) - 1] = '\\0';", content)

with open("/home/sankar/github/s_lkm/monitor.c", "w") as f:
    f.write(content)
