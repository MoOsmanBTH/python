def mRNA_transcript(template):
    mRNA = {"A": "U", "T": "A", "C": "G", "G": "C"}
    ret_transcript = ""
    for a in template:
        ret_transcript += mRNA[a]

    return ret_transcript

print(mRNA_transcript("ATCGATTG"))