def findObjectId(textString):
    import re
    return re.findall("([a-f\d]{24})",textString)
