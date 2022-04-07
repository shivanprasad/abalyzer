import os

script_dir = os.path.dirname(__file__)  # Script directory
aba_lookup_table_path = os.path.join(script_dir, 'data/aba_lookup_table.csv')

open(aba_lookup_table_path, 'w')

with open('temp/unchecked_aba_lookup_table.csv', 'r') as in_file, open(aba_lookup_table_path, 'w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)