import glob
import pdfkit
import tqdm
import os

os.makedirs("output", exist_ok=True)

with open("template.html") as f:
	template = f.read()

for file in tqdm.tqdm(glob.glob("output/*.txt")):
	with open(file) as fi, open(file.replace(".txt", ".html"), "w") as fo:
		art_url, sentences = fi.read().split("@@===#####===@@")
		fo.write(template.replace("$url", art_url).replace("$data", sentences))

	pdfkit.from_file(file.replace(".txt", ".html"), file.replace(".txt", ".pdf"))
