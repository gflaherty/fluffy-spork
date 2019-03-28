
import os
import random
import shutil
import sys


PATH_LENGTH = (2, 5)
FILE_COUNT = (1, 10)

TEST_SOURCE = "random_test.py"

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
WORDS = [x for x in WORDS if "'" not in x]


def get_word():
    return random.choice(WORDS)

def get_dir(word_count):
    retv = get_word()
    for i in xrange(word_count - 1):
        retv += "/{}".format(get_word())
    return retv

def generate_source(dest_path):
    """
    Copy our random file to the specified destination directory, with a random name.
    """
    dest_path = os.path.join(dest_path, "{}_test.py".format(get_word()))
    print("   Creating file {}".format(dest_path))
    shutil.copy(TEST_SOURCE, dest_path)

def make_random_dir(depth, file_count):
    new_dir = get_dir(depth)
    print("Making directory {}".format(new_dir))
    os.makedirs(new_dir)
    for i in range(file_count):
        generate_source(new_dir)
    return new_dir


def main(argv):
    make_random_dir(3, 4)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
