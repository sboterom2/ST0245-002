from matplotlib import pyplot as plt
import numpy as np
class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

data= np.loadtxt('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/datasets/csv/enfermo_csv/00000004_66324407_ver1.csv', skiprows=0, delimiter=',')
def compp(m, dst_h, dst_w):
    ori_h, ori_width = m.shape
    ratio_h = ori_h / dst_h
    ratio_w = ori_width / dst_w
    dst = np.zeros((dst_h, dst_w), np.uint8)
    for h in range(dst_h):
        for w in range(dst_w):
            x_ori = int(w * ratio_w)
            y_ori = int(h * ratio_h)          
            dst[h, w] = m[y_ori, x_ori]       
    return dst    


img= compp(data,150,150)    
print(img)
l,a=img.shape
size=l*a
ld=img.flatten().tolist() 
for i in range(len(ld)):
    ld[i]=str(ld[i])  
print (ld)
freq = {}
for c in ld:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1      
frec = sorted(freq.items(), key=lambda x: x[1], reverse=False)        



class HuffmanTree(object):
    
    def arbol(self, char_Weights):
        self.char_Weights=char_Weights
        self.Leaf = [Node(k,v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node:node.value, reverse=False)
            n = Node(value=(self.Leaf[0].value + self.Leaf[1].value))
            n.left = self.Leaf.pop(0)
            n.right = self.Leaf[0]
            self.Leaf[0]=n
        self.root = self.Leaf[0]
        self.Buffer = list(range(800))


    def Hu_generate(self, tree, length,dic):
        x=''
        self.dic=dic
        node = tree
        if (not node):
            return
        elif node.name:  
            for i in range(length):
                x=x+str(self.Buffer[i])               
            dic[node.name]=x
            
        self.Buffer[length] = 0
        self.Hu_generate(node.left, length + 1, dic)
        self.Buffer[length] = 1
        self.Hu_generate(node.right, length + 1, dic)

    def get_code(self):
        self.Hu_generate(self.root, 0, freq)
        
        
    def comp(self,data,dic):
        
        for i in range(len(data)):
            x=data[i]
            y=dic.get(x)
            data[i]=y
        k=''.join(data)
        print(k)  
        return k
        
    def decomp(self,textcomp, tree):
        txt=textcomp
        tl=list()
        temp = tree
        result = ''
        for i in (txt):
            if int(i) == 0:
                temp = temp.left
            else:
                temp = temp.right
            if temp.left == None and temp.right == None:
                result += temp.name
                tl.append(temp.name)
                temp = tree
        print (result) 
        print(tl)
        decompimg=np.zeros((l,a), np.uint8)
        x=0
        for m in range(l):
            for j in range(a):
                decompimg[m,j]=tl[x]
                x=x+1
        print(decompimg)        
        return tl
          

    def getdecomp(self):
        self.decomp(self.comp(ld,self.dic),self.root,)

arbol=HuffmanTree()
arbol.arbol(freq)   
arbol.get_code()
arbol.getdecomp()