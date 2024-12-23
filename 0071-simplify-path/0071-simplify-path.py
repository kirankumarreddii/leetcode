class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths = path.split('/')
        print(paths) 
        for p in path.split("/"):
            if p != "" and p != "." and p!="..":
                stack.append(p)
            if p ==".." and len(stack)>0:
                stack.pop()
        return "/"+"/".join(stack)


