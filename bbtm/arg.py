import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "echo", 
    help="echo the string you use here.", 
    choices=["*", "^", "$", "@"],
)
parser.add_argument("times", help="No. of times to print the string.", type=int)
parser.add_argument("--format", help="Format the output.")

# A new kind of output.
parser.add_argument("-e", "--end", help="Add the ending character.", action="store_true")
args = parser.parse_args()

char = "#"
end_char = ""
if args.format:
    char = args.format
if args.end:
    end_char = ";"
print(char, args.echo * args.times, char, end_char)
