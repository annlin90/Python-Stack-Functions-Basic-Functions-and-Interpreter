#Ann Lin 11443855

import numpy as np
import re

opStack = []
dictStack = []
tempStack = []
scopingLinks = []
debug_level = 0

def debug(*s):
    if debug_level>0:
        print(s)


def opPop():
    if len(opStack)>0:
        return opStack.pop(len(opStack)-1)
    else:
        debug("Error: opPop - Operand stack is empty")

def opPush(value):
    opStack.append(value)

def tempPop():
    if len(tempStack)>0:
        return tempStack.pop(len(tempStack)-1)
    else:
        debug("Error: opPop - Operand stack is empty")

def tempPush(value):
    opStack.append(value)


def define(name, value):
    if len(dictStack) > 0:
        dictStack[len(dictStack) - 1][1][name] = value
    else:
        tupleDict = (0, {})
        tupleDict[1][name] = value
        dictPush(tupleDict)

def dictPop(): #the basic functions for dictStack like opStack
    if len(dictStack)>0:
        return dictStack.pop(len(dictStack)-1)
    else:
        debug("Error: opPop - Dictionary stack is empty")


def dictPush(value): 
    dictStack.append(value)

def lookOther(chain):
    if chain == 0:
        return scopingLinks.append(chain)
    scopingLinks.append(chain)
    lookOther(dictStack[chain][0])

def lookup(name, scope):
    if scope == 'static':
        if len(dictStack) == 0:
            return False
        elif name in dictStack[len(dictStack) - 1][1]:
            return dictStack[len(dictStack) - 1][1][name]
        else:
            lookOther(dictStack[len(dictStack) - 1][0])
            for chain in scopingLinks:
                if name in dictStack[chain][1].keys():
                    return dictStack[chain][1][name]
        return None
    elif scope == 'dynamic':
         if len(dictStack) == 0:
            return False
         for d in reversed(dictStack):
            if name in d[1].keys():
                return d[1][name]
         return None
####################### Arithmetic operators #######################################

def add(): #add two top stack vals
    if(len(opStack)>1):
        op1=opPop()
        op2 = opPop()
        opPush(op1+op2)
    else:
        debug("There's an Error!")


def sub(): #subtract two top stack vals
    if(len(opStack)>1):
        op1=opPop()
        op2 = opPop()
        opPush(op2-op1)
    else:
        debug("There's an Error!")


def mul(): #multiply two top stack values
    if(len(opStack)>1):
        op1=opPop()
        op2 = opPop()
        opPush(op1*op2)
    else:
        debug("There's an Error!")

def div(): #divides two top stack values
    if(len(opStack)>1):
        op1=opPop()
        op2 = opPop()
        opPush(op2/op1)
    else:
        debug("There's an Error!")

def eq(): #see if two numbers are equal
    if(len(opStack)>1):
        op1=opPop()
        op2 = opPop()
        if(op1==op2):
            opPush(True)
        else:
            opPush(False)
    else:
        debug("There's an Error!")
        

def lt(): #less than operator
    if(len(opStack)>1):
        op1=opPop()
        op2 =opPop()
        if(op2<op1):
            opPush(True)
        else:
            opPush(False)
    else:
        debug("There's an Error!")


def gt(): #greater than operator
    if(len(opStack)>1):
        op1=opPop()
        op2 =opPop()
        if(op2>op1):
            opPush(True)
        else:
            opPush(False)
    else:
        debug("There's an Error!")

###############################################################################

####################### String operators ########################################

def length(): #gets length of string
    if len(opStack)>0:
        value = opPop()
        strings = value
        strings= re.sub('[(){}<>]', '', strings)
        lengths = len(strings)
        opPush(lengths)
    else:
        debug("There's an Error!")


def get(): #according to slides, get() gets the string and index value from stack
    if len(opStack)>0: #then pushes the ASCII value of the character at the position of the index value
        op1 = opPop() #onto the stack
        op2 = opPop()
        op3 = ord(op2[op1+1])
        opPush(op3)
    else:
        debug("There's an Error!")

def getinterval(): #gets string, index, and count from the stack
    if len(opStack)>0: #returns the substring of the string starting from index to count
        count = opPop() #pushes the substring onto the stack
        index = opPop()
        inputStrings = opPop()
        inputStrings = re.sub('[(){}<>]', '', inputStrings)
        intervals = inputStrings[count+1:(index+count)]
        opPush('('+intervals+')')
    else:
        debug("There's an Error!")
#############################################################################

#################### Boolean operators ######################################

def psAnd(): #and operator 
    if(len(opStack)>1):
        op1=opPop()
        op2=opPop()
        if(op1==False):
            opPush(False)
        elif(op2==False):
            opPush(False)
        else:
            opPush(True)
    else:
        debug("There's an Error!")


def psOr(): # or operator
    if(len(opStack)>1):
        op1=opPop()
        op2=opPop()
        if(op1==False and op2==True):
            opPush(True)
        elif(op2==False and op1==True):
            opPush(True)
        elif(op1==False and op2==False):
            opPush(False)
        else:
            opPush(True)
    else:
        debug("There's an Error!")


def psNot(): #!False = True, it does that
    global opStack
    if(len(opStack)>0):
        op1=opPop()
        if(op1==False): #get rid of op2 isinstance and check if its boolean not integer
            opPush(True)
        else:
            opPush(False)
    else:
        debug("There's an Error!")
###############################################################################

#################### stack manipulation and print operators ###################

def dup(): #duplicates top stack value
    if(len(opStack)>0):
        op1 = opPop()
        opPush(op1)
        opPush(op1)
    else:
        debug("There's an Error!")

def rollhelper(opStacking, opStack2, lengths, listss, rolling):
    opStacking = opStack2[lengths - listss:]  # values for rolling
    opStacking = opStacking[-rolling:]+opStacking[:-rolling]#rolls values that are given by user
    opStack2 = opStack2[:lengths - listss]  
    opStack2 = opStack2 + opStacking  #puts new values in another list
    clear()
    for value in opStack2:
        opPush(value)
                
def roll():
    if (len(opStack) !=0 or len(opStack)>0):
        rolling = opPop()  #number of rolls
        listss = opPop()  #list
        lengths = len(opStack)
        opStack2 = opStack
        opStacking = 0
        if rolling > 0:
             rollhelper(opStacking, opStack2, lengths, listss, rolling)
                
        if rolling < 0:
             rollhelper(opStacking, opStack2, lengths, listss, rolling)
    else:
        debug("There's an Error!")
        

def exch(): #switches top two values with each other
    if len(opStack)>0:
         op1 = opPop()
         op2 = opPop()
         opPush(op1)
         opPush(op2)
    else:
        debug("Error: opPop - Operand stack is empty")

def pop(): #pop function which is the same as the opPop() function
    if len(opStack)>0:
        return opStack.pop(len(opStack)-1)
    else:
        debug("Error: opPop - Operand stack is empty")

def copy(): #copies first n items and pushes onto stack
    opList = []
    n = opPop()
    for i in range(n):
            opList.insert(i, opPop())
    opList.reverse()
    for a in opList:
        opPush(a)
    for b in opList:
        opPush(b)

def clear(): #clears stack
    if(len(opStack) == 0): #global opStack for each function
        debug("Error")
    elif (len(opStack)>0):
        while(len(opStack)>0):
             del opStack[:]
    else:
        debug("There's an Error!")


def stack():
    print("")
    print("Output: ")
    for x in reversed(opStack):
        print(x)


######################## Dictionary operators #############################################		


def begin(): #according to slide, begin operator takes a dictionary from the top of the
    if len(opStack)>0: #operand stack and pushes it on the dictionary stack
        op1 = opPop()
        dictPush(op1)
    else:
        debug("There's an Error!")

def end():
    if len(dictStack)>0: #according to slide, end operator pops the top dict from dict stack
         dictPop() #and throws it away
    else:
        debug("There's an Error!")


def psDict(): #PUSHES empty dictionary onto operand stack
    if len(dictStack)>=0:
        opPop()
        opPush({})
    else:
        debug("There's an Error!")


def psDef(): #makes a dictionary
    if len(opStack)> 1:
        valuing = opPop()
        naming = opPop()
        others = naming[1:]
        define(others, valuing)
    else:
        debug("There's an Error!")
     

###### this function is not in hw just to help me with it ################# 
def clearDict(): #clears stack
    if(len(dictStack) == 0): #global dictStack for each function
        debug("There's an Error!")
    else:
        while(len(dictStack)>0):
             del dictStack[:]

def clearStatic(): #clears stack
    if(len(scopingLinks) == 0): #global dictStack for each function
        debug("There's an Error!")
    else:
        while(len(scopingLinks)>0):
             del scopingLinks[:]


def staticFind(index, token):
    print(dictStack[index])
    if (token in dictStack[index][1]) or index !=0:
        print(token)
        return index
    return staticFind(dictStack[index+1][0], token)


########################################################################

def psIf():
    helps = opPop()
    choice = opPop()
    if bool(choice):
        interpretHelper(helps)

def psIfelse():
    elseing= opPop()
    ifs= opPop()
    choice = opPop()
    if bool(choice):
        interpretHelper(ifs)
    else:
        interpretHelper(elseing)

##################################################################

########################################################################################################################################
    #PART 2 BEGIN
##############################################################################################################################################    

def tokenize(s):
  return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def groupMatching(values):
    rest2 = iter(values) #puts each seperate character/word in a list
    other = []
    for tokens in rest2:
        if tokens == '}':
            return other 
        elif tokens == '{': #seperates the brackets
            other.append(groupMatching(rest2))
        else:
            other.append(tokens)
    return False

def parse(values):
    throughVal = iter(values)
    other = []
    for tokens in throughVal: #takes a string of tokens, looks for {}, recursively converts tokens between 
        if tokens == '}': #{} into a code arrays
            return False
        elif tokens == '{':
            other.append(groupMatching(throughVal))
        else:
            other.append(tokens)
    return other

operations = {'add': add, 'sub': sub, 'mul': mul, 'div': div, 'eq': eq, 'lt': lt, 'gt': gt, 'length': length,
      'get': get, 'getinterval': getinterval, 'and': psAnd, 'or': psOr, 'not': psNot, 'roll': roll,
      'dup': dup, 'exch': exch, 'copy': copy, 'pop': pop, 'clear': clear,
      'def': psDef, 'stack': stack, 'if': psIf, 'ifelse': psIfelse}

def interpretHelper(tokens, scope):
    for token in tokens:
        try:
            opPush(int(token))
        except:
            try:
                operations[token]()
            except:
                if token == "true":
                    opPush(True)
                elif token == "false":
                    opPush(False)
                elif token[0] is '/' or token[0] is '(':
                    opPush(str(token))
                else:
                    defn = lookup(str(token), scope)
                    staticChain = []
                    if defn != None:
                        if type(defn) is type([]):
                            dictPush((staticFind(len(dictStack)-1, token), {}))
                            interpretHelper(defn, scope)
                            
                        else:
                            opPush(defn)
                    else:
                        opPush(token)

def interpreter(s): #s is a string
    print("dynamic")
    interpretHelper(parse(tokenize(s)), "dynamic")
    clear()
    clearDict()
    print("")
    print("static")
    interpretHelper(parse(tokenize(s)), "static")
    print("")


input1 = """
/m 50 def
/n 100 def
/egg1 {/m 25 def n} def
/chic {
 /n 1 def
 /egg2 { n } def
 m n
 egg1
 egg2
 stack } def
n
chic"""

input2 = """
/x 10 def
/A { x } def
/C { /x 40 def A stack } def
/B { /x 30 def /A { x } def C } def
B"""

input3 = """
/x 4 def
/g { x stack } def
/f { /x 7 def g } def
f"""

print("")
print("======")

print("Interprator:")

interpreter(input2)
clear()
clearDict()
clearStatic()
interpreter(input1)
clear()
clearDict()
clearStatic()
interpreter(input3)

input() #so prompt doesn't close automatically

