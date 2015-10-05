#! /usr/bin/python3

import configparser
import glob
import os
import sys
import textwrap

from collections import namedtuple
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zackphotos.settings')
import django
django.setup()

from django.utils import timezone
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from gallery.models import Gallery, GalleryImage, GalleryComment

# For now, we hardwire UTC+1 as the date of everything to import.
IMPORT_TIMEZONE = timezone.get_fixed_timezone(+60)
def parse_date(date):
    return timezone.make_aware(datetime.strptime(date, "%Y-%m-%d %H:%M:%S"),
                               IMPORT_TIMEZONE)

def prep_text(text):
    corrected = []
    for line in text.splitlines():
        if line == "":
            continue
        elif line == ".":
            corrected.append("")
        else:
            corrected.append(line)
    return "\n".join(corrected)

Annotation = namedtuple("Annotation",
                        ("fname", "date", "photog", "title", "loc",
                         "people", "tags", "desc", "comment"))
def load_annotation(dir_to_import, annf, sect):
    fname = os.path.join(dir_to_import, sect)

    sect    = annf[sect]
    date    = parse_date(sect['date'])
    photog  = sect.get('photog', 'unknown')
    title   = sect.get('title',  '')
    loc     = sect.get('loc',    'unknown')
    people  = sorted(p.strip() for p in sect.get('people', '').split(','))
    tags    = sorted(p.strip().lower() for p in sect.get('tags', '').split(','))
    desc    = prep_text(sect.get('desc', ''))
    comment = prep_text(sect.get('comment', ''))

    return Annotation(fname, date, photog, title, loc,
                      people, tags, desc, comment)

def load_annotations(dir_to_import):
    annf = configparser.ConfigParser(
        defaults = {
            'date':    None,
            'photog':  'unknown',
            'title':   '',
            'loc':     'unknown',
            'people':  '',
            'tags':    '',
            'desc':    '',
            'comment': '',
        },
        empty_lines_in_values = False,
        interpolation = None)

    with open(os.path.join(dir_to_import, "annot.ini")) as f:
        annf.read_file(f)

    anns = []
    fail = False
    for img in annf.sections():
        ann = load_annotation(dir_to_import, annf, img)
        if os.path.exists(ann.fname):
            anns.append(ann)
        else:
            sys.stderr.write("image missing: " + ann.fname + "\n")
            fail = True

    unused = set(glob.iglob(os.path.join(dir_to_import, "*.jpg")))
    unused.update(glob.iglob(os.path.join(dir_to_import, "*.jpeg")))
    unused.difference_update(ann.fname for ann in anns)

    if unused:
        sys.stderr.write(textwrap.fill("images not imported: " +
                                       ", ".join(sorted(unused)) + ".\n",
                                       subsequent_indent="    "))
        fail = True

    if fail: sys.exit(1)

    return anns

def do_import(annotations, gallery, commenter):
    sys.stderr.write("Importing {} images to gallery '{}'\n"
                     .format(len(annotations), gallery.title))

    ndigits = len(str(len(annotations)-1))

    comment_timestamp = timezone.make_aware(datetime(2015, 10, 4, 20, 0),
                                            timezone.get_fixed_timezone(-240))

    for seq, ann in enumerate(annotations):
        sys.stderr.write(ann.fname + "\n")
        img = GalleryImage(gallery      = gallery,
                           sort_order   = seq,
                           date         = ann.date,
                           notes        = ann.desc)
        img.save()

        if ann.photog: img.photographer.set(ann.photog)
        if ann.loc:    img.location.set(ann.loc)
        if ann.people: img.people.set(*ann.people)
        if ann.tags:   img.tags.set(*ann.tags)

        ifile = ImageFile(open(ann.fname, 'rb'))
        img.image.save("I{1:0{0}}.jpg".format(ndigits, seq),
                       ifile)
        img.save()

        if ann.comment:
            comment = GalleryComment(image   = img,
                                     user    = commenter,
                                     date    = comment_timestamp,
                                     comment = ann.comment)
            comment.save()

def main():
    dir_to_import = sys.argv[1]
    gallery       = Gallery.objects.get(slug=sys.argv[2])
    commenter     = User.objects.get(username='zack')
    annotations   = load_annotations(dir_to_import)

    do_import(annotations, gallery, commenter)
    sys.exit(0)

main()
