import re
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="input file (example: 'file.txt')")
ap.add_argument("-o", "--output", required=True, help="output file (example: 'file.md')")

args = vars(ap.parse_args())

input_file = str(args["input"])
output_file = str(args["output"])

input = open(input_file, "r", encoding="utf-8")
output = open(output_file, "w", encoding="utf-8")

text = input.read()

type = "Basic"

text = re.sub(r"^(.*)\t(.*)\t(.*)", fr"START\n{type}\n\1\nBack: \2\nTags: \3\nEND\n\n", text, flags=re.MULTILINE)

output.write(text)

input.close()
output.close()