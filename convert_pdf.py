import glob
import pdfkit
import tqdm

for file in tqdm.tqdm(glob.glob("output/*.html")):
	pdfkit.from_file(file, file.replace(".html", ".pdf"))
