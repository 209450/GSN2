
import argparse
from pathlib import Path
import os
import shutil

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tags_file", action="store", dest="tags_file",
                        help="avaible tags file", required=True),
    parser.add_argument("--albums_dirs", nargs="+", dest="albums_dirs",
                        help="directories with albums", required=True)
    parser.add_argument("--output", action="store", dest="output",
                        help="csv file", required=True)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    tags_file_path = Path(args.tags_file)
    assert tags_file_path.is_file()

    albums_dirs = [Path(path) for path in args.albums_dirs]

    output_path = Path(args.output)
    shutil.rmtree(output_path, ignore_errors=True)
    os.makedirs(output_path)

    print(tags_file_path, output_path, albums_dirs)
