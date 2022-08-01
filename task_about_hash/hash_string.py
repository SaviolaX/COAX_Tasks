import hashlib

s = "Python Bootcamp"
def hashlib_algor_sha_two_five_six(s):
    """
    Hashing with algorithm sha256() from hashlib
    1 - convert string in bytes by .encode('utf-8')
    2 - hashing by sha256()
    3 - convert result into hexadecimal format
    """
    result = hashlib.sha256(s.encode('utf-8')).hexdigest()
    return result

def python_built_in_hash_algor(s):
    """
    Python function hash()
    get => string obj
    return => integer value
    """
    result = hash(s)
    return result

print(hashlib_algor_sha_two_five_six(s))
print(python_built_in_hash_algor(s))