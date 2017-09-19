import sys
def isHeader(s):
	if "#include<" in s and ".h>" in s:
		s=s.replace(">","")
		lh=s.split("<")
		if lh[1] in headercheck:
			return True
		else:
			return False
	else:
		return False
	
	
def isMain(s):
	se=s.find("main",0,len(s))
	if se!=-1:
		if s[se+4]=="(" or s[se+5]=="(" :
			if s[len(s)-2]==")" :
				if "{" in s:
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	

def bracketChecker(li):
	v=0
	for i in li:
		if "{" in i:
			v+=1
		if "}" in i:
			v-=1
		if v<0:
			return False
	return True if v==0 else False
		


def endofLineChecker(s):
	if "<" in s or ">" in s or "while" not in s or "for" not in s:
		return False if s[-1]!=";" else True
	else:
		return True
		
def checkVar(s,var):
	g=s.split(" ")
	if g[0] in vartype:
		lvar=[]
		x=g[1].split(",")
		x[-1]=x[-1].strip(";")
		for i in x:
			if i in keyword:
				return False
			elif i[0].isalpha()==False:
				return False
			elif i[0]=="_" :
				lvar.append(i)
			else:
				lvar.append(i)
		var[g[0]]=lvar
		return True
	else:
		return True
			

		
				
def isFunction(s,function):
	for i in range (len(function)):
		if function[i] in s:
			if "(" in s:
				if ")" in s:
					return True 
				else:
					return False
			else:
				return False
		
		
def isVarOrKey(s,var,keyword):
	for i in keyword:
		if i in keyword:
			return True
	if "(" in s:
		return False
	elif s=="{"  or s=="}" :
		return True
	else:
		if "=" in s:
			g=s.split("=")
			if g[0] in var:
				return True
			else:
				return False
		
		

def varToType(s,var):
	if "=" in s:
		g=s.split("=")
		if g[0] in var['int'] or g[0] in var['long']:
			g[1]=g[1].strip(";")
			try:
				q=int(g[1])
			except:
				return False
		elif g[0] in var['float'] or g[0] in var['double']:
			g[1]=g[1].strip(";")
			try:
				q=float(g[1])
			except ValueError:
				return False
		elif g[0] in var['char']:
			g[1]=g[1].strip(";")
			try:
				q=str(g[1])
			except ValueError:
				return False
		else:
			return False
	
	else:
		return True
def isLoop(s):
		if "for" in s:
			if "(" in s:
				if ")" in s:
					lexp=s.split(";")
					if len(lexp)==3:
						return True
					else:
						return False
				else:
					return False
			else:
				return False
		elif "while" in s:
				lexp=s.split("(")
				if len(lexp)==2:
					return True
				else:
					return False
		else:
			return True			
		


def checkPar(s,header):
		if "printf" in s:
				if s[6]=="(" :
					if s[len(s)-2]==")":
						if "#include<stdio.h>" in header:
							
							s=s.replace(")","")
							s=s.strip(";")
							lexp=s.split("(")
							if "" in lexp:
								q=lexp.remove("")
							
							k=len(lexp)
							if k>1:
								return True
							else:
								return False
						else:
							return False
					else:	
						return False
				else:
					return False
		elif "scanf" in s:
				if s[5]=="(" :
					if s[len(s)-2]==")":
						if "#include<stdio.h>" in header:
							s=s.replace(")",";")
							s=s.strip(";")
							lexp=s.split("(")
							if "" in lexp:
								q=lexp.remove("")
							
							k=len(lexp)
							if k>1:
								return True
							else:
								return False
						else:
							return False
					else:	
						return False
				else:
					return False
						
		
			
		elif "if" in s:
				s=s.replace(" ","")
				if s[2]=="(" or s[3]=="(" :
					if s[len(s)-2]==")":
						if s[len(s)-1]=="{":
							s=s.replace(")","")
							s=s.replace("{","")
							s=s.strip(";")
							lexp=s.split("(")
							if "" in lexp:
								q=lexp.remove("")
						
							k=len(lexp)
							if k>1:
								return True
							else:
								return False	
						else:
							return False
					else:
						return False
				else:	
					return False
		else:
			return True
				
def exprchecker(s):
    stack1=[]
    stack2=[]
    
    i=0
    while(i<len(s)):
        if s[i] in operation:
            while len(stack2)!=0 and incomingprec(s[i])>instackprec(stack2[-1]):
                stack2.pop()
                if len(stack1)>=2:
                    stack1.pop()
                else:
                    return False
            i=i+1   
            stack2.append(s[i])
        else:
            num=""
            while i<len(s) and s[i] not in operation :
                num=num+s[i]
                i=i+1;
            stack1.append(num)
           
    while len(stack2)!=0 and len(stack1)!=0:
        stack2.pop()
        stack1.pop()
    if len(stack1)!=1 or len(stack2)!=0:
        return False

			
	
filename=input("enter file name:")
f1= open(filename,'r')
l=f1.readlines()
head=0
main=0
global a
global b
global c
global d
global e
global f
global h
global m
global n
h=True
a=True
b=True
c=True
d=True
e=True
f=True
m=True
n=True
vartype=["int","char","float","double","long"]
keyword=["while","for","if","else","do","goto","void","static","return","extern","switch","case","sizeof","printf","scanf"]
headercheck=["stdio.h","math.h","string.h"]
operation=["+","/","-","*",">=","<=","<",">","^"]
header=[]
var={"int":[],"float":[],"long":[],"double":[],"char":[]}

for i in range(len(l)):
	l[i]=l[i].strip()
	#checking for header files
	if isHeader(l[i]):
		if main>0:
			
			h=False
		else:
			head+=1
			header.append(l[i])
	#checking for main
	elif isMain(l[i]):
		main+=1
		a=bracketChecker(l[i:len(l)]) #checking for brackets
		for j in range (i+1, len(l)):
			l[j]=l[j].strip()
			
			if l[j][-1]=="{" or l[j][-1]=="}":
				continue
			if "while" in l[j] or "for" in l[j] or "if" in l[j] or "else" in l[j]:
				continue
			else:
				b=endofLineChecker(l[j])
				if not b:
					break
		
		for j in range (i+1, len(l)):
			c=checkVar(l[j],var) #checking for variables
			if not c:
				break
		
		for j in range (i+1, len(l)):
			d=isVarOrKey(l[j],var,keyword) #checking for keywords or variables
			if not d:
				print(l[j])
				break
		
		for j in range (i+1, len(l)):
			e=varToType(l[j],var)
			if not e:
				print(l[j])
				break
		for j in range (i+1, len(l)):
			if "=" in l[j]:
				g=l[j].split("=")
				if g[0] in var:
					n=exprchecker(g[1])
			else:
				n=exprchecker(l[j])
			if not n:
				break
		for j in range (i+1, len(l)):
			f=isLoop(l[j])
			if not f:
				break
		for j in range (i+1, len(l)):
			m=checkPar(l[j],header)
			if not m:
				break
			

if not h or head==0:
	print("Header file not included or not in the right place")
if main!=1:
	print("one main function is needed")
if not a:
	print("{ or } missing ")
if not b:
	print("; missing")
if not c:
	print("invalid syntax of variable")
if not d:
	print("variable not declared")
if not e:
	print("type error")
if not n:
	print("error in expression")
if not f:
	print("invalid syntax of loop")
if not m:
	print("invalid syntax of printf or scanf or if")
if h and main==1 and a and b and c and d and e and f and m: 
	print("correct syntax")
			
		
	
