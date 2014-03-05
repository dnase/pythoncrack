import base64, hashlib

def _get_salt(rawhash):
    #strip off {SSHA} if it's there
    if rawhash[0:6] == '{SSHA}' or rawhash[0:6] == '{ssha}':
        myhash = rawhash[6:]
    else:
        myhash = rawhash
    #base64 decode hash
    hash_decoded = base64.b64decode(myhash)
    return hash_decoded[20:]

def _hash_string(my_string, salt):
    return base64.b64encode(hashlib.sha1(my_string + salt).digest() + salt)

def try_pw(my_string, my_hash):
    my_salt = _get_salt(my_hash)
    th = _hash_string(my_string, my_salt)
    return (my_hash == th or my_hash == ('{SSHA}' + th) or my_hash == ('{ssha}' + th)) 