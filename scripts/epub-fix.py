# EPUB Fix
# Using Calibre, we can fix EPUB files and polish them as well.
# Usage: calibre-debug epub-fix.py -- <path-to-epub-file-or-folder>

from calibre.ebooks.oeb.polish.check.main import run_checks, fix_errors
from calibre.ebooks.oeb.polish.container import get_container
from calibre.ebooks.oeb.polish.main import polish_one

from collections import namedtuple
from os import listdir
from os.path import isfile, join, isdir
import sys

POLISH_OPTS = {
    'embed': False,
    'subset': False,
    'opf': None,
    'cover': None,
    'jacket': False,
    'remove_jacket': False,
    'smarten_punctuation': False,
    'remove_unused_css': True,
    'compress_images': False,
    'upgrade_book': True,
    'add_soft_hyphens': False,
    'remove_soft_hyphens': False,
    'download_external_resources': False,
}

def fix_file(filepath):
    try:
        ## Fix Errors
        container = get_container(filepath, tweak_mode=True)
        errors = run_checks(container)
        if errors:
            if fix_errors(container, errors):
                print("Fixed: %s" % filepath)
                container.commit()
            else:
                print("Unable fix: %s" % filepath)
        else:
            print("Correct: %s" % filepath)
        ## Polish
        report = []
        polish_one(container, namedtuple('Options', POLISH_OPTS.keys())(*POLISH_OPTS.values()), report.append)
        print("\n".join(report))
        container.commit()
    except:
        print("Unhandled error: %s" % filepath)


def fix_folder(folder):
    epubs = [
        f
        for f in listdir(folder)
        if isfile(join(folder, f)) and f.lower().endswith(".epub")
    ]
    for f in epubs:
        fix_file(join(folder, f))
    dirs = [ d for d in listdir(folder) if isdir(join(folder, d)) ]
    for d in dirs:
        fix_folder(join(folder, d))

for arg in sys.argv[1:]:
    if isfile(arg):
        fix_file(arg)
    elif isdir(arg):
        fix_folder(arg)
    else:
        print("Unknown argument: %s" % arg)
