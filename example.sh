inputfile="049PR_Vidal_Covas_QP1_Trial.TextGrid"
tiers="Lexical Phonological"

echo "input file: ${inputfile}"
tg-merge-and-mark-tiers \
	-i "${inputfile}" \
	-o "new_${inputfile}" \
	--tiers "${tiers}"
