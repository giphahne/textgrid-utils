# TextGrid Utilities

Installation:
```bash
$ pip install textgrid-utils
```

Add (optional) auto-complete for CLI usage:
```bash
$ eval "$(register-python-argcomplete merge-and-mark-textgrid-tiers)"
$ eval "$(register-python-argcomplete tg-copy-tiers)"
$ eval "$(register-python-argcomplete tg-remove-tiers)"
$ eval "$(register-python-argcomplete tg-list-tiers)"
```

Command line usage:
```bash
$ merge-and-mark-textgrid-tiers \
	  -i trial_data.TextGrid \
	  -o trial_data_merged.TextGrid \
	  --tiers Phonological Lexical
```


Library usage:

```python
from textgrid_utils import merge_and_mark_tiers

merge_and_mark_tiers(
	tg_file="<path/to/input/file>",
	output_file="<path/to/output/file>",
	tiers=('Phonlogical', 'Lexical'))
```

