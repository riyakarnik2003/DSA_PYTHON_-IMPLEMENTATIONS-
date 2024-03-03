class BinaryTrees:
    def __init__(self,n):
        
        self.list=[None]*n

    def root(self,rootNode):
        if(self.list[0] == None):
            self.list[0]=rootNode

    def left_child(self,rootNode,parentNode_idx):
        if(self.list[parentNode_idx]!=None):
            if(self.list[2*(parentNode_idx)+1]==None):
                self.list[2*(parentNode_idx)+1]=rootNode

            else:
                print("No parent node is present")

    def right_child(self,rootNode,parentNode_idx):
        if(self.list[parentNode_idx]!=None):
            if(self.list[2*(parentNode_idx)+2]==None):
                self.list[2*(parentNode_idx)+2]=rootNode

            else:
                print("No parent node is present")


    def printTree(self):
        if(self.list==None):
            print("Empty binary tree")

        else:
            for i in self.list:
                if(i!=None):
               
                    print(i,end=" ")
                else:
                    print(" - ", end=" ")

Bt=BinaryTrees(7)
Bt.root(1)
Bt.left_child(2, 0)
Bt.right_child(3, 0)
Bt.left_child(4, 1)
Bt.right_child(5, 1)
Bt.right_child(6, 2)
Bt.printTree()