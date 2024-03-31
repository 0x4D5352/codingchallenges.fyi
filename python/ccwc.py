import argparse
from sys import stdin

parser = argparse.ArgumentParser(
    description="print newline, word, and byte counts for each file"
)
parser.add_argument("-c", "--bytes", action="store_true", help="print the byte counts")
parser.add_argument(
    "-l", "--lines", action="store_true", help="print the newline counts"
)
parser.add_argument(
    "-m", "--chars", action="store_true", help="print the character counts"
)
parser.add_argument("-w", "--words", action="store_true", help="print the word counts")
parser.add_argument("filename", default="file")

args = parser.parse_args()


def count_bytes(file):
    return str(len(file))


def count_lines(file):
    return str(file.count(b"\n"))


# gh copilot ended up helping me with these next two which i feel a bit ashamed of


def count_words(file):
    return str(len(file.split()))


def count_chars(file):
    return str(len(file.decode("utf-8")))


if args.filename == "file":
    pass
    # i need to figure out how to reformat this as a stdin-able thing...
else:
    with open(args.filename, "rb") as f:
        file = f.read()
        answer = ""
        spacing = " "
        if args.bytes:
            answer += count_bytes(file) + spacing
        if args.lines:
            answer += count_lines(file) + spacing
        if args.words:
            answer += count_words(file) + spacing
        if args.chars:
            answer += count_chars(file) + spacing

        if answer == "":
            answer = (
                count_lines(file)
                + spacing
                + count_words(file)
                + spacing
                + count_bytes(file)
                + spacing
            )
        print(f"{answer}{args.filename}")
