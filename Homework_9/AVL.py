class Node:
    def __init__(self,val = None,left = None,right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

 
class BST:
    
    
    def __init__(self) -> None:
        self.root = None
    
    
    
             
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
    
    
        

        
    def search(self,val):
        it = self.root
        
        while it:
            if it.val == val:
                return True
            
            if it.val > val:
                it = it.left
            else:
                it = it.right
        
        return False
        
    

    def is_avl_tree(self):
        def is_balanced(node):
            if node is None:
                return True, 0

            left_balanced, left_height = is_balanced(node.left)
            right_balanced, right_height = is_balanced(node.right)

            if not left_balanced or not right_balanced:
                return False, 0

            if abs(left_height - right_height) > 1:
                return False, 0

            return True, max(left_height, right_height) + 1

        balanced, _ = is_balanced(self.root)
        
        return balanced 
        
        
    def print_tree(self):
    
        if self.root:
            self._print_tree(self.root, 0)
    
    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self._print_tree(node.left, level + 1)
            
    def _balance_factor(self, node):
        if not node:
            return 0
        return self._help_get_hight(node.left) - self._help_get_hight(node.right)
    
    
    
    def _balance_insert(self, node, val):
       
        if not node:
            return Node(val)
        if val < node.val:
            node.left = self._balance_insert(node.left, val)
        else:
            node.right = self._balance_insert(node.right, val)

        
        balance = self._balance_factor(node)

        if balance > 1:
            if val < node.left.val:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        if balance < -1:
            if val > node.right.val:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def insert(self, val):
        self.root = self._balance_insert(self.root, val)
        
        

    
    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    


tree = BST()

tree.insert(20)
tree.insert(10) 
tree.insert(30)
tree.insert(35)
tree.insert(15)
tree.insert(12)
tree.insert(36)
tree.insert(5)
tree.insert(25)
tree.insert(21)





print(tree.is_avl_tree())
tree.print_tree()

