import sys
import ssha_tools
import itertools

if len(sys.argv) == 4:
    hash_file = sys.argv[1]
    min_length = int(sys.argv[2])
    max_length = int(sys.argv[3])
else:
    sys.exit("Usage: " + sys.argv[0] + " [hash_file] [min_length] [max_length]")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

print("Loading hashes...")
with open(hash_file) as hfp:
    hashes = [l.strip() for l in hfp]

print(str(len(hashes)) + " hashes loaded.")

for my_hash in hashes:
    print("-----Attempting to brute force hash: " + my_hash + "-----")
    for i in range(min_length, max_length):
        print("Trying strings of length " + str(i))
        perms = [''.join(c) for c in itertools.permutations(chars, i)]
        for my_string in perms:
            if ssha_tools.try_pw(my_string, my_hash):
                print("Password for hash " + my_hash + " is " + my_string)
                fop = open("found.out", 'a+')
                fop.write("Password for hash " + my_hash + " is " + my_string)
                fop.close
                break

sys.exit("Done.")