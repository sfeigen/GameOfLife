'''
#   One method for optimizing is to flag tiles
#   untouched by default, and to not calculate
#   tile with this flag that borders alive.
# __ __ __ __ __ __           __ __ __ __ __ __
#|UT|__|__|__|UT|UT|         |__|__|__|__|UT|UT|
#|__|__|[]|__|__|__|         |__|[]|[]|__|__|__|
#|__|[]|[]|[]|[]|__|         |__|[]|##|##|[]|__|
#|__|__|__|[]|__|__|   ->    |__|__|__|[]|[]|__|
#|UT|UT|__|__|__|UT|         |UT|UT|__|__|__|__|
#|UT|UT|UT|UT|UT|UT|         |UT|UT|UT|UT|UT|UT|
#
# Eg    : Seed = 6, stable pattern.
# Normal: 6 x 6 * 2           = 72  check() calls.
# Smart : 6 x 6 * 2 = 72 - 24 = 48  check() calls.
#
# 1. Iterate sequentially through all tiles that:
#   != UT and have Neighbor
#
'''

# __ __ __ __ __ __           __ __ __ __ __ __
#|UT|__|__|__|__|UT|         |__|__|__|__|__|__|
#|__|__|[]|[]|__|__|         |[]|[]|##|##|[]|[]|
#|__|[]|[]|[]|[]|__|         |##|##|##|##|##|##|
#|__|__|[]|[]|__|__|   ->    |[]|[]|##|##|[]|[]|
#|UT|__|__|__|__|UT|         |__|__|__|__|__|__|
#|UT|UT|UT|UT|UT|UT|         |UT|UT|UT|UT|UT|UT|
# Gen.: 1                     Gen.: 4
# Try and find a way to regenerate UT tiles after
# they're killed.
