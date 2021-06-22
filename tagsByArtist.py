
import argparse
from pathlib import Path
import os
import shutil
from urllib import parse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tags_file", action="store", dest="tags_file",
                        help="avaible tags file", required=True),
    parser.add_argument("--output", action="store", dest="output",
                        help="csv file", required=True)
    parser.add_argument("--artist_dir", action="store", dest="artist_dir",
                        help="directory with albums", required=True)

    return parser.parse_args()

MUSIC_EXTENSIONS = ['.mp3','.mp4','.ogg','.wav']

if __name__ == "__main__":
    args = parse_args()

    tags_file_path = Path(args.tags_file)
    assert tags_file_path.is_file()

    output_path = Path(args.output)
    shutil.rmtree(output_path, ignore_errors=True)
    os.makedirs(output_path)

    artist_dirs = Path(args.artist_dir)
    assert artist_dirs.is_dir()

    # artist
    artist = artist_dirs.name.replace(" ", "+")

    # tracks
    albums_dirs = [artist_dir for artist_dir in artist_dirs.iterdir() if artist_dir.is_dir()]
    tracks = []
    for album_dir in albums_dirs:
        for track_path in album_dir.iterdir():
            if track_path.suffix in MUSIC_EXTENSIONS:
                tracks.append(track_path.stem.replace(" ", "+"))
    
    # URLs
    

    


    # tracks = [track for track in albums_dirs if track.suffix in MUSIC_EXTENSIONS]
    # print(albums_dirs)

    # print(tags_file_path, output_path, albums_dirs)
