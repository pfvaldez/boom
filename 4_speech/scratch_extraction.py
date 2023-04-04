'''

'''
import re
 
# # initializing list
# test_list = ["all", "love", "and", "get", "educated", "by", "gfg"]
# con_res= []
# # printing original list
# print("The original list is : " + str(test_list))

# vow = "aeiou"
# vow_res = [x for x in test_list if re.search(f"[{vow}]$", x, flags=re.IGNORECASE)]
# con_res = [x for x in test_list if x not in vow_res]

# # printing result
# print("The extracted words w/ vowels: " + str(vow_res))
# print("The extracted words w/ consonants: " + str(con_res))


def extract_keywords(text):
    keyword_extracted = text.split()
    return keyword_extracted


def vowel_consonant(transcript, keywords):
    con_res= []
    # printing original list
    print("The original keywords are: " + str(keywords))

    vow = "aeiou"
    vow_res = [x for x in keywords if re.search(f"[{vow}]$", x, flags=re.IGNORECASE)]
    con_res = [x for x in keywords if x not in vow_res]
    
    for keyword in con_res:
        transcript= re.sub(keyword, keyword + "-c", transcript) #appends -c for each keyword with consonant

    for keyword in vow_res:
        transcript= re.sub(keyword, keyword + "-v", transcript) #appends -v for each keyword

    return transcript


def main():
    transcript = "The quick brown fox"
    print(transcript)
    keywords= extract_keywords(transcript)
    transcript= vowel_consonant(transcript, keywords)
    print("keywords:\t {}" .format(keywords))
    print("result transcript:\t {}" .format(transcript))

if __name__ == '__main__':
    main()