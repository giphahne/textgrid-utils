import argparse
from io import BytesIO

import argcomplete

from textgrid_utils.textgrid_functions import add_type_tier
from textgrid_utils.textgrid_functions import merge_and_mark_tiers
from textgrid_utils.textgrid_functions import copy_tiers
from textgrid_utils.textgrid_functions import remove_tiers
from textgrid_utils.textgrid_functions import list_tiers
from textgrid_utils.textgrid_functions import rename_tier


def add_type_tier_main():
    """Entry point for the application script"""

    description = ("Add tier to given TextGrid file.  The Marks of this new "
                   "will be created from the names of the given ``--tiers''")
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument(
        "-i", "--file", dest="tg_file", type=str, help=("input file"))
    parser.add_argument(
        "--in-place",
        action="store_true",
        dest="inplace",
        default=False,
        help=("change specified "
              "file in-place"))
    parser.add_argument(
        "--tiers",
        type=str,
        nargs="+",
        metavar="Tier",
        help=("tiers to use for creating "
              "the type tier."))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    add_type_tier(tg_file=args.tg_file, tiers=args.tiers, inplace=args.inplace)


def merge_main():
    """Entry point for the application script"""

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

    description = ""
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("file", type=str, help=("textgrid file"))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    list_tiers(tg_file=args.file)


def rename_tier_main():
    """Entry point for the application script"""

    description = ""
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("--file", type=str, help=("textgrid file"))
    parser.add_argument("--current-name", type=str, help=("tier name"))
    parser.add_argument("--new-name", type=str, help=("tier name"))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    rename_tier(
        tg_file=args.file,
        current_name=args.current_name,
        new_name=args.new_name)
