import os
import glob

def run(command):
	print(command)
	os.system(command)

CMD = """wkhtmltopdf --javascript-delay 5000 {1} {0}.pdf """
CMD2 = """"/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py" -o labs.pdf {}"""


files = [filename for filename in glob.iglob('./Lab*/*.html', recursive=True)]

files.sort(key=lambda x: os.path.basename(os.path.dirname(x)))
files = ["index.html"] + files

print(files)

labs = []
for i in range(1, len(files)+1):
	run(CMD.format(i, files[i - 1]))
	labs.append(str(i) + ".pdf")

run(CMD2.format(" ".join(labs)))

for l in labs:
	run("rm " + l)