import piexif
import imghdr
import argparse
from glob import glob
from os.path import isfile

# from _version import __version__

__version__ = "0.6"

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
parser.add_argument('-s', '--snark', help="snarky message to replace default.")
parser.add_argument('--verbose', action="store_true", help="verbose progress output.")
parser.add_argument('file', help="Filename(s) to process.")
args = parser.parse_args()


def clear_EXIF(filename):
    try:
        piexif.remove(filename)
        return (True)
    except OSError:
        print("Yeah, that file ( " + filename + " ) doesn't exist.\n")


def put_EXIF(filename, snarky_message):
    zeroth_ifd = {piexif.ImageIFD.Make: snarky_message}
    exif_ifd = {piexif.ExifIFD.CameraOwnerName: snarky_message,
                piexif.ExifIFD.DateTimeOriginal: snarky_message,
                piexif.ExifIFD.ExifVersion: snarky_message,
                piexif.ExifIFD.MakerNote: snarky_message,
                piexif.ExifIFD.UserComment: snarky_message,
                piexif.ExifIFD.ImageUniqueID: snarky_message}
    gps_ifd = {piexif.GPSIFD.GPSAreaInformation: snarky_message}
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd}
    exif_bytes = piexif.dump(exif_dict)
    try:
        piexif.insert(exif_bytes, filename)
        return (True)
    except OSError:
        print("Yeah, that file ( " + filename + " ) doesn't exist.\n")


if args.snark is not None:
    snarky = args.snark
else:
    snarky = "Who's a clever dick now?"

if args.verbose:
    print("=======================================================\n\nStarting EXIF-ication!\n")

for filename in glob(args.file):
    if isfile(filename):
        if (imghdr.what(filename) is 'tiff') or (imghdr.what(filename) is 'jpeg'):
            if args.verbose:
                print("--------------------------")
            if clear_EXIF(filename):
                if args.verbose:
                    print(filename + " : EXIF data has been cleared.")
            else:
                print("Something went wrong clearing EXIF for " + filename)
            if put_EXIF(filename, snarky):
                if args.verbose:
                    print("==>" + filename + " : Snarky messages set.")
            else:
                print("Something went wrong writing snarky message for " + filename)

if args.verbose:
    print("=======================================================")
