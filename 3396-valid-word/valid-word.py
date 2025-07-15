class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """

        vf = cf = csf= 0
        s = 1
        vowels = "aeiou"
        symbols = "@#$"
        if len(word) > 2:
            for i in word:
                if i.isalnum():
                    cf+=1
                    if i.lower() in vowels:
                        vf = 1
                        print("vf. ",i)
                    elif not i.isdigit():
                        csf = 1
                        print("csf. ",i)
                if i in symbols:
                    s = 0
            print(cf)
            if vf and s and csf and cf >=3:
                return True
        return False

        