class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths = path.split('/')
        print(paths) 
        for p in path.split("/"):
            if p != "" and p != "." and p!="..":
                stack.append(p)
            elif p ==".." and stack:
                stack.pop()

        return "/"+"/".join(stack)


