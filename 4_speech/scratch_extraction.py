'''

'''
import re
 
# initializing list
test_list = ["all", "love", "and", "get", "educated", "by", "gfg"]
con_res= []
# printing original list
print("The original list is : " + str(test_list))

vow = "aeiou"
vow_res = [x for x in test_list if re.search(f"[{vow}]$", x, flags=re.IGNORECASE)]
con_res = [x for x in test_list if x not in vow_res]

# printing result
print("The extracted words w/ vowels: " + str(vow_res))
print("The extracted words w/ consonants: " + str(con_res))
