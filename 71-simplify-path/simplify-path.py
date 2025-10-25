class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        res = ['/']
        for i in path:
            if i == "..":
                if res:
                    res.pop()
            elif i == ".":
                continue
            elif i:
                res.append("/"+i)


        res = "".join(res).replace("//","/")

        if not res:
            return "/"
        else:
            return res