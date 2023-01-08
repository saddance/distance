import argparse
from Levenshtein import distance
def compare(first_path, second_path):
    with open(first_path, 'r') as first, open(second_path, 'r') as second:
        first_text = first.read()
        second_text = second.read()
        return distance(first_text, second_text) / max(len(first_text), len(second_text))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('document_pairs_path')
    parser.add_argument('output_path')
    args = parser.parse_args()

    with open(args.document_pairs_path, 'r') as document_pairs, open(args.output_path, 'a') as output:
        for pair in document_pairs.readlines():
            first_path, second_path = pair.split()
            output.write(str(compare(first_path, second_path)) + '\n')


if __name__ == "__main__":
    main()
