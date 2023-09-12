class Node:
    def __init__(self,val = None,left = None,right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BST:
    
    
    def __init__(self) -> None:
        self.root = None
    
    def _help_inster(self,root,val):
        if root is None:
            return Node(val)
        if root.val < val:
            root.right = self._help_inster(root.right,val)
        else:
            root.left = self._help_inster(root.left,val)
        
        return root
        
        
    def insert(self,val):
        self.root = self._help_inster(self.root,val)
            
            
    def _help_get_hight(self,node):
        if not node:
            return -1
        return max(self._help_get_hight(node.left),self._help_get_hight(node.right))+1
    
    
    def get_hight(self):
        return self._help_get_hight(self.root)
    
    
    def get_predecessor(self):
        pass

    
    def get_subecessor(self):
        pass
    
    def get_min(self):
        pass
    
    def get_max(self):
        pass
    
    def delete(self):
        pass
    
    
    def pre_traversal(self):
        pass
    
    def in_traversal(self):
        pass
    
    def post_traversal(self):
        pass
    
        
    


tree = BST()

tree.insert(5)
tree.insert(15) 
tree.insert(25)
tree.insert(4)
tree.insert(56)
  

print(tree.root.right.val)
print(tree.get_hight())

