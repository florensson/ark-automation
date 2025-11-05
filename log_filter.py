input_file = "tp_log.txt"        # byt till rätt filnamn
output_file = "weight_only_log.txt"   # filen med bara [WEIGHT]-rader

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        if "[WEIGHT]" in line:
            outfile.write(line)