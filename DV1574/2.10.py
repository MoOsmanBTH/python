def find_and_replace(find_str, replace_str, infile, outfile):
    replace_from = open(infile).read()
    replace_from = replace_from.replace(find_str, replace_str)
    replace_to = open(outfile, "w+")
    replace_to.write(replace_from)
    replace_to.close()

find_and_replace("of", "Aladdin", "Alice.txt", "Exempel.txt")