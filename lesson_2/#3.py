def anagram(text):
   return text[::-1]

def recursive_anagram(text):
   if len(text) <= 1:
      return text
   return recursive_anagram(text[1:]) + text[0]


if __name__ == '__main__':
   print(recursive_anagram('3486'))
   print(anagram('3486'))