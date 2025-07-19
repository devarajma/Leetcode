class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort(key = len)
        res = set()

        for dr in folder:
            d_parts = dr.split('/')
            parent = ''
            for part in d_parts[1:]:
                parent += "/" + part
                if parent in res:
                    break
            else:
                res.add(parent)
        return list(res)
