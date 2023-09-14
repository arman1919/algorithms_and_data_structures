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
    
    def _h_delete(self,node,key):
        
        if not node: return None
        if node.val < key:
            node.right = self._h_delete(node.right,key)
            
        elif node.val > key:
            node.left = self._h_delete(node.left,key)
        else:
            
            if not node.left:
                tmp = node.right
                node = None
                return tmp
            if not node.right:
                tmp = node.left
                node = None
                return tmp
            
            tmp = self.get_min(node.right)
            node.val = tmp.val
            self._h_delete(node.right, tmp.val)
        
        return node
            
            
        
    def delete(self,key):
        return self._h_delete(self.root,key)
    
    
    
    def get_predecessor(self,node):
        
        if not node:
            return None
        if node.left:
            return self.get_max(node.left)
        else:
            pred = None
            anestor = self.root
        
            while anestor is not  node:
                
                if(anestor.val < node.val):
                    pred = anestor
                    anestor = anestor.right
                else:
                    anestor = anestor.left
        
            return pred
    
    
        
    def get_subecessor(self,node):
        if not node:
            return None
        if node.right:
            return self.get_min(node.right)
        else:
            pred = None
            anestor = self.root
        
            while anestor != node:
                if(anestor.val > node.val):
                    pred = anestor
                    anestor = anestor.left
                else:
                    anestor = anestor.right
        
        return pred
    
    
    def get_min(self,node):
        
        it  = node
        while  it.left:
            it = it.left
        return it
    
    def get_max(self,node):
        it  = node
        while  it.right:
            it = it.right
        return it
    
    def _h_search(self,node,val):
        if not node:
            return False
        if node.val == val:
            return True
        
        if node.val < val:
            return self._h_search(node.right,val)
        else:
            return self._h_search(node.left,val)
        
        
    def search(self,val):
        return self._h_search(self.root,val)
    
    def _h_pre_order_traversal(self, node):
        if not node:
            return 
        print(node.val, end=" ")
        
        self._h_pre_order_traversal(node.left)
        self._h_pre_order_traversal(node.right)

    def pre_order_traversal(self):
        self._h_pre_order_traversal(self.root)
    
    
    
    
    def _h_in_order_traversal(self, node):
        if node:
            self._h_in_order_traversal(node.left)
            print(node.val, end=" ")
            self._h_in_order_traversal(node.right)

    def in_order_traversal(self):
        self._h_in_order_traversal(self.root)





    def _h_post_order_traversal(self, node):
        if node:
            self._h_post_order_traversal(node.left)
            self._h_post_order_traversal(node.right)
            print(node.val, end=" ")

    def post_order_traversal(self):
        self._h_post_order_traversal(self.root)
    
        
    
    
    # es print-y es chem grel 
    
    def print_tree(self):
        if self.root:
            self._print_tree(self.root, 0)
    
    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self._print_tree(node.left, level + 1)


tree = BST()


tree.insert(20)
tree.insert(1) 
tree.insert(15)
tree.insert(10)
tree.insert(5)
tree.insert(2)
tree.insert(4)



tree.print_tree()

tree.in_order_traversal()
print()
tree.pre_order_traversal()
print()
tree.post_order_traversal()

print()

print(tree.get_predecessor(tree.root.left.right).val)


