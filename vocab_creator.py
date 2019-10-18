import argparse
import os

from preprocess import build_vocab_from
import re

def create_vocab_from_files(dir_path, output_vocab_file):
    sentence = []
    # Only look at fold 0
    for f in filter(lambda f: f.endswith(".txt") and "_f0_" in f, os.listdir(dir_path)):
        with open(os.path.join(dir_path, f), "r") as f:
            for l in f.readlines():
                sentence.append( [w.strip("\n").replace("\t", " ") for w in  l.split()])

    vocab_dict = build_vocab_from(sentence)
    persist_vocab(vocab_dict, output_vocab_file)


def persist_vocab(vocab, output_vocab_file):
    with open(output_vocab_file, "w") as f:
        for k, v in vocab.items():
            f.write("{}\t{}\n".format(k, v))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='train.py')
    parser.add_argument('-datadir', required=True,
                        help='The directory containing the files to load')
    parser.add_argument('-outputfile', required=True,
                        help='The outputfile', default="data.vocab")
    opt = parser.parse_args()

    create_vocab_from_files(opt.datadir, opt.outputfile)

    print("Created vocab in {}".format(opt.outputfile))
