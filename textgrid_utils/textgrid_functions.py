from io import BytesIO
from itertools import chain
from itertools import repeat
from itertools import combinations
from functools import partial

import textgrid
from textgrid import IntervalTier
from textgrid import Interval
from textgrid.exceptions import TextGridError


def _validate_overlapping_tiers(t1, t2):
    for i1 in filter(lambda x: x.mark, t1):
        for i2 in filter(lambda x: x.mark, t2):
            if i1.overlaps(i2):
                raise TextGridError(
                    "{t1name} {i1} overlaps {t2name} {i2}".format(
                        t1name=t1.name, i1=i1, t2name=t2.name, i2=i2))


def add_type_tier(tg_file="", tiers=(), inplace=False):
    """
    Creates a new TextGrid file with an added IntervalTier.
    """
    tg = textgrid.TextGrid()
    tg.read(f=tg_file)

    for t1_name, t2_name in combinations(tiers, 2):
        _validate_overlapping_tiers(tg.getFirst(t1_name), tg.getFirst(t2_name))

    # merged_tier = IntervalTier(
    #     name="Merged",
    #     minTime=min(map(lambda x: tg.getFirst(x).minTime, tiers)),
    #     maxTime=min(map(lambda x: tg.getFirst(x).maxTime, tiers)))

    marked_tier = IntervalTier(
        name="Type",
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

        # merged_tier.addInterval(
        #     Interval(
        #         minTime=interval.minTime,
        #         maxTime=interval.maxTime,
        #         mark=interval.mark))

    tg.tiers.insert(1, marked_tier)
    #    tg.tiers.insert(2, merged_tier)

    if inplace:
        with open(tg_file, "w") as f:
            tg.write(f)
    else:
        pass


def merge_and_mark_tiers(tg_file="", output_file="", tiers=()):
    """
    Creates a new TextGrid file with an added IntervalTier.
    """
    tg = textgrid.TextGrid()
    tg.read(f=tg_file)

    for t1_name, t2_name in combinations(tiers, 2):
        _validate_overlapping_tiers(tg.getFirst(t1_name), tg.getFirst(t2_name))

    merged_tier = IntervalTier(
        name="Merged",
        minTime=min(map(lambda x: tg.getFirst(x).minTime, tiers)),
        maxTime=min(map(lambda x: tg.getFirst(x).maxTime, tiers)))

    # marked_tier = IntervalTier(
    #     name="Marked",
    #     minTime=min(map(lambda x: tg.getFirst(x).minTime, tiers)),
    #     maxTime=min(map(lambda x: tg.getFirst(x).maxTime, tiers)))

    for tier_name, interval in filter(
            lambda x: x[1].mark,
            chain.from_iterable(
                map(lambda x: zip(repeat(x.name), iter(x)),
                    map(lambda t: tg.getFirst(t), tiers)))):
        # marked_tier.addInterval(
        #     Interval(
        #         minTime=interval.minTime,
        #         maxTime=interval.maxTime,
        #         mark=tier_name))

        merged_tier.addInterval(
            Interval(
                minTime=interval.minTime,
                maxTime=interval.maxTime,
                mark=interval.mark))

    #tg.tiers.insert(1, marked_tier)
    tg.tiers.insert(1, merged_tier)

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
