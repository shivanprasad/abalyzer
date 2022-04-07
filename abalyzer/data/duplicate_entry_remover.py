open('aba_lookup_table.csv', 'w')

with open('temp/unchecked_aba_lookup_table.csv', 'r') as in_file, open('aba_lookup_table.csv', 'w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)