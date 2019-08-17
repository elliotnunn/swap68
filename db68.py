# This might grow into a MainCode function-matching system?

import binascii

# ,ABCD,EF01,
def commastring(binary):
    ugly = binascii.hexlify(binary).upper()
    num = len(ugly) + len(ugly) // 4 + 1
    fugly = bytearray(b',' * num)
    fugly[1::5] = ugly[0::4]
    fugly[2::5] = ugly[1::4]
    fugly[3::5] = ugly[2::4]
    fugly[4::5] = ugly[3::4]
    while fugly.endswith(b',,'): fugly.pop(-1)
    return fugly.decode('ascii')

# import sys
# print(commastring(sys.argv[1].encode('utf-8')))
