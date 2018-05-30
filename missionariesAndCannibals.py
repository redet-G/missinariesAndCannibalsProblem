from collections import deque

class Node():
	def __init__(self, ML,CL,MR,CR,boat):
		self.ML = ML
		self.CL = CL
		self.MR = MR
		self.CR = CR
		self.boat = boat
		self.parent = None
		self.child = []
	
	def isValid(self):
		if (self.ML < 0 or self.MR <0 or self.CL < 0 or self.CR < 0):
			return False;# negative numbers
		if(self.ML>0 and self.ML<self.CL):
			return False
		elif(self.MR>0 and self.MR<self.CR):
			return False
		return True
	
	def isGoleNode(self):
		if self.MR==0 and self.CR==0:
			return True
		else:
			return False
	def __eq__(self, other):
		return self.CL == other.CL and self.ML == other.ML and self.CR == other.CR and self.MR == other.MR and self.boat == other.boat
	def __hash__(self):
		return hash((self.CL,self.CR,self.ML,self.MR,self.boat))
	def __str__(self):
		return "ML:"+str(self.ML)+"CL:"+str(self.CL)+"MR:"+str(self.MR)+"CR:"+str(self.CR)+"boat:"+str(self.boat)
	def showDiff(self,other):
		CML = 0
		CCL = 0
		if(self.ML < other.ML):
			CML = other.ML - self.ML
		else:
			CML = self.ML - other.ML
		
		if(self.CL < other.CL):
			CCL = other.CL - self.CL
		else:
			CCL = self.CL - other.CL
		if(CML==0):
			print("C: "+str(CCL)+" to the "+other.boat)
		elif(CCL==0):
			print("M: "+str(CML)+" to the "+other.boat)
		else:
			print("M: "+str(CML)+" and C: "+str(CCL)+" to the "+other.boat)
	def nextNode(self):
		nextNodes = []
		if(self.boat == 'R'):
			# two M
			newNode = Node(self.ML+2,self.CL,self.MR-2,self.CR,'L')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			# two C
			newNode = Node(self.ML,self.CL+2,self.MR,self.CR-2,'L')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			# one M one C
			newNode = Node(self.ML+1,self.CL+1,self.MR-1,self.CR-1,'L')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			# one M
			newNode = Node(self.ML+1,self.CL,self.MR-1,self.CR,'L')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			# one C
			newNode = Node(self.ML,self.CL+1,self.MR,self.CR-1,'L')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
					
			
		else:
			# two M
			newNode = Node(self.ML-2,self.CL,self.MR+2,self.CR,'R')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			# two C
			newNode = Node(self.ML,self.CL-2,self.MR,self.CR+2,'R')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			# one M one C
			newNode = Node(self.ML-1,self.CL-1,self.MR+1,self.CR+1,'R')
			if(newNode.isValid()):
				newNode.parent = self
				newNode.parent = self
				newNode.parent = self
				newNode.parent = self
				nextNodes.append(newNode)		
			# one M
			newNode = Node(self.ML-1,self.CL,self.MR+1,self.CR,'R')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			# one C
			newNode = Node(self.ML,self.CL-1,self.MR,self.CR+1,'R')
			if(newNode.isValid()):
				newNode.parent = self
				nextNodes.append(newNode)
			
		return nextNodes;
def search(first):
	discoverd = set()
	queue = deque()
	queue.append(first)
	while queue:
		node = queue.popleft()
		# print(node)
		discoverd.add(node)
		if node.isGoleNode():
			return node
		
		nextNodes = node.nextNode()
		for n in nextNodes:
			if n not in discoverd: # or n not in queue:
				queue.append(n)
				discoverd.add(n)
				node.child.append(n)
	return None
# queue = deque([])
# def bridthFirstSearch():
#name = [[1,2,1],[3,1,0]]
#print(str(isValid(name)))
def display(node):
	if node and node.parent:
		node.showDiff(node.parent)
		display(node.parent)
def toNwric(node):
	if not node.child:
		print("\""+str(node)+"\"",end='')
	else:
		for n in node.child:
			if n == node.child[0]:
				print("(",end='');
			toNwric(n)
			if(n != node.child[-1]):
				print(",",end='')
			else:
				print(")\""+str(node)+"\"",end='')

class n:
	def __init__(self,name,child):
		self.name = name
		self.child = child
	def __str__(self):
		return str(self.name)
	def __eq__(self, other):
		return self.name == other.name
	def __hash__(self):
		return hash((self.name))
def main():
	first = Node(0,0,3,3,'R')
	search(first)
	#nodes = first.nextNode()
	# display(search(first))
	# first = n('A',[n('B',None),n('C',None)]) 
	toNwric(first)
	# for n in first.child:
		# print(n)
	# print(first.child)
	# for n in nodes:
		# print(n)
if __name__ == "__main__":
	main()