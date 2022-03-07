import glob
import pdfkit
import tqdm
import os
import regex as re

import sys

lat = re.compile(r"([^\p{Latin}\s\p{posix_punct}\d]+)")

os.makedirs("output", exist_ok=True)

with open("template.html") as f:
	template = f.read()

directory = "output"
if len(sys.argv) > 1:
	directory = sys.argv[1]

for file in tqdm.tqdm(glob.glob(f"{directory}/*.txt")):
	with open(file) as fi, open(file.replace(".txt", ".html"), "w") as fo:
		art_url, sentences = fi.read().split("@@===#####===@@")
		fo.write(template.replace("$url", art_url).replace("$data", lat.sub("[...]", sentences)))

	pdfkit.from_file(file.replace(".txt", ".html"), file.replace(".txt", ".pdf"))
