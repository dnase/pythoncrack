import sys
import ssha_tools

if len(sys.argv) == 3:
    hash_file = sys.argv[1]
    dict_file = sys.argv[2]
else:
    sys.exit("Usage: " + sys.argv[0] + " [hash_file] [dictionary_file]")

print("Loading hashes...")
with open(hash_file) as hfp:
    hashes = [l.strip() for l in hfp]

print(str(len(hashes)) + " hashes loaded.")

for my_hash in hashes:
    print("-----Attempting to crack hash: " + my_hash + "-----")
    with open(dict_file) as dfp:
        for my_string in [l.strip() for l in dfp]:
            if ssha_tools.try_pw(my_string, my_hash):
                print("Password for hash " + my_hash + " is " + my_string)
                fop = open("found.out", 'a+')
                fop.write("Password for hash " + my_hash + " is " + my_string)
                fop.close
                break

sys.exit("Done.")