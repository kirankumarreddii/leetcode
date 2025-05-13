class Struct_Tree:
    def __init__(self, start,end):
        self.start=start
        self.end=end
        self.sum=0
        self.left=None
        self.right=None
class NumArray:

    def __init__(self, nums: List[int]):
        def create(start,end):
            node=Struct_Tree(start,end)
            if start==end:
                node.sum=nums[start]
            else:
                mid=(start+end)//2
                node.left=create(start,mid)
                node.right=create(mid+1,end)
                node.sum=node.left.sum+node.right.sum
            return node
        self.root=create(0,len(nums)-1)

    def update(self, index: int, val: int) -> None:
        def update_node(node,index,val):
            if node.start==node.end:
                node.sum=val
                return 
            else:
                mid=(node.start+node.end)//2
                if index<=mid:
                    update_node(node.left,index,val)
                else:
                    update_node(node.right,index,val)
            node.sum = node.left.sum + node.right.sum
        update_node(self.root,index,val)


    def sumRange(self, left: int, right: int) -> int:
        def range_sum(node,l,r):
            if node.start>r or node.end<l:
                return 0
            if l<=node.start and node.end<=r:
                return node.sum
            return range_sum(node.left,l,r)+range_sum(node.right,l,r)


        return range_sum(self.root,left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)