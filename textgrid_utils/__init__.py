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

    for tier_name, interval in filter(
            lambda x: x[1].mark,
            chain.from_iterable(
                map(lambda x: zip(repeat(x.name), iter(x)),
                    map(lambda t: tg.getFirst(t), tiers)))):
        merged_tier.addInterval(
            Interval(
                minTime=interval.minTime,
                maxTime=interval.maxTime,
                mark=tier_name))

    tg.tiers.insert(1, merged_tier)

    with open(output_file, "w") as f:
        tg.write(f)


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


if __name__ == '__main__':
    merge_main()
