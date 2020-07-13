class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if len(version1) == 1 and len(version2) == 1:
            if int(version1) > int(version2):
                return 1
            elif int(version1) < int(version2):
                return -1
            else:
                return 0
        v1 = version1.split(".")
        v2 = version2.split(".")
        i = 0
        output = 0
        if len(v1) > len(v2):
            while len(v1) != len(v2):
                v2.append("0")
        elif len(v2) > len(v1):
            while len(v1) != len(v2):
                v1.append("0")
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                output = 1
                break
            elif int(v1[i]) < int(v2[i]):
                output = -1
                break
            else:
                i += 1
        return output