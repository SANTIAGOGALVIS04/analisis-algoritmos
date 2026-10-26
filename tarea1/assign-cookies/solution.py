class Solution(object):
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()

        nino = 0
        galleta = 0
        satisfechos = 0

        while nino < len(g) and galleta < len(s):
            if s[galleta] >= g[nino]:
                satisfechos += 1
                nino += 1

            galleta += 1

        return satisfechos