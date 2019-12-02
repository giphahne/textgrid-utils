# TextGrid Utilities

Installation:
```bash
$ pip install textgrid-utils
```

Add (optional) auto-complete for CLI usage:
```bash

$ eval "$(register-python-argcomplete tg-add-type-tier)"
$ eval "$(register-python-argcomplete tg-add-merged-tier)"
$ eval "$(register-python-argcomplete tg-copy-tiers)"
$ eval "$(register-python-argcomplete tg-remove-tiers)"
$ eval "$(register-python-argcomplete tg-list-tiers)"
$ eval "$(register-python-argcomplete tg-rename-tier)"

```

Command line usage (optionally: install jq for pretty-printing):
```bash

$ tg-list-tiers orig.TextGrid | jq .

$ tg-add-type-tier \
	-i tg_file.TextGrid \
	--tiers Phonological Lexical \
	--new-tier-name "Type"

$ tg-list-tiers orig.TextGrid | jq .

$ tg-add-merged-tier \
	-i tg_file.TextGrid \
	--tiers Phonological Lexical \
	--new-tier-name "Merged"

$ tg-list-tiers orig.TextGrid | jq .

```


Library usage:

```python
from textgrid_utils import add_type_tier

add_type_tier(
	tg_file="<path/to/input/file>",
	tiers=('Phonlogical', 'Lexical'),
	inplace=True,
	new_tier_name="Type")
	
```

