import csv
import argparse
from itertools import chain
from itertools import repeat
from itertools import combinations

import textgrid
from textgrid import IntervalTier
from textgrid import Interval
from textgrid.exceptions import TextGridError


def validate_overlapping_tiers(t1, t2):
    for i1 in filter(lambda x: x.mark, t1):
        for i2 in filter(lambda x: x.mark, t2):
            if i1.overlaps(i2):
                raise TextGridError(
                    "{t1name} {i1} overlaps {t2name} {i2}".format(
                        t1name=t1.name, i1=i1, t2name=t2.name, i2=i2))


def merge_and_mark_tiers(tg_file="", output_file="", tiers=()):
    """
    Creates a new TextGrid file with an added IntervalTier.
    """
    tg = textgrid.TextGrid()
    tg.read(f=tg_file)

    for t1_name, t2_name in combinations(tiers, 2):
        validate_overlapping_tiers(tg.getFirst(t1_name), tg.getFirst(t2_name))

    merged_tier = IntervalTier(
        name="Merged",
        minTime=min(map(lambda x: tg.getFirst(x).minTime, tiers)),
        maxTime=min(map(lambda x: tg.getFirst(x).maxTime, tiers)))

    marked_tier = IntervalTier(
        name="Marked",
        minTime=min(map(lambda x: tg.getFirst(x).minTime, tiers)),
        maxTime=min(map(lambda x: tg.getFirst(x).maxTime, tiers)))

    for tier_name, interval in filter(
            lambda x: x[1].mark,
            chain.from_iterable(
                map(lambda x: zip(repeat(x.name), iter(x)),
                    map(lambda t: tg.getFirst(t), tiers)))):
        marked_tier.addInterval(
            Interval(
                minTime=interval.minTime,
                maxTime=interval.maxTime,
                mark=tier_name))

        merged_tier.addInterval(
            Interval(
                minTime=interval.minTime,
                maxTime=interval.maxTime,
                mark=interval.mark))

    tg.tiers.insert(1, marked_tier)
    tg.tiers.insert(2, merged_tier)

    with open(output_file, "w") as f:
        tg.write(f)


def copy_tiers(source_file="", target_file="", tiers=()):
    """
    Copies given Tiers from source to target
    """
    source_tg = textgrid.TextGrid()
    source_tg.read(f=source_file)

    target_tg = textgrid.TextGrid()
    target_tg.read(f=target_file)

    for tier in tiers:
        target_tg.tiers.append(source_tg.getFirst(tier))

    with open(target_file, "w") as f:
        target_tg.write(f)


def remove_tiers(target_file="", tiers=()):
    """
    Remove given Tiers from target
    """
    target_tg = textgrid.TextGrid()
    target_tg.read(f=target_file)

    for tier in tiers:
        try:
            target_tg.pop(target_tg.getNames().index(tier))
        except ValueError:
            continue

    with open(target_file, "w") as f:
        target_tg.write(f)


def list_tiers(tg_file):
    #print(tg_file)
    target_tg = textgrid.TextGrid()
    target_tg.read(f=tg_file)
    print(target_tg.getNames())


def merge_main():
    """Entry point for the application script"""

    import sys
    import argparse
    import json
    from functools import partial

    import argcomplete

    description = ""
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("-i", "--input-file", type=str, help=("input file"))
    parser.add_argument("-o", "--output-file", type=str, help=("output file"))
    parser.add_argument(
        "--tiers", type=str, nargs="+", help=("tiers to merge and mark."))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    merge_and_mark_tiers(
        tg_file=args.input_file,
        output_file=args.output_file,
        tiers=args.tiers)


def copy_tiers_main():
    """Entry point for the application script"""

    import sys
    import argparse
    import json
    from functools import partial

    import argcomplete

    description = ""
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument(
        "-i",
        "--source",
        type=str,
        help=("Search this Textgrid file for Tiers of the "
              "given Name"))
    parser.add_argument("-o", "--target", type=str, help=(""))
    parser.add_argument(
        "--tiers",
        type=str,
        nargs="+",
        help=("tiers to copy from "
              "source to target"))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    copy_tiers(
        source_file=args.source, target_file=args.target, tiers=args.tiers)


def remove_tiers_main():
    """Entry point for the application script"""

    import sys
    import argparse
    import json
    from functools import partial

    import argcomplete

    description = ""
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("-f", "--file", type=str, help=("textgrid file"))
    parser.add_argument(
        "-t",
        "--tiers",
        type=str,
        nargs="+",
        help=("tiers to copy from "
              "source to target"))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    remove_tiers(target_file=args.file, tiers=args.tiers)


def list_main():
    """Entry point for the application script"""

    import sys
    import argparse
    import json
    from functools import partial

    import argcomplete

    description = ""
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("file", type=str, help=("textgrid file"))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    list_tiers(tg_file=args.file)


if __name__ == '__main__':
    merge_main()
