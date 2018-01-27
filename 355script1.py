#Ann Lin 11443855

import numpy as np
import re

opStack = []
dictStack = []

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


def define(name, value):
        if name[0] =='/': #sakire help
                name = name[1:]
        if(len(dictStack)>0):
                dictStack[len(dictStack)-1][name]= value
        else:
                d = {name: value}
                dictStack.append(d)


def dictPop(): #the basic functions for dictStack like opStack
    if len(dictStack)>0:
        return dictStack.pop(len(dictStack)-1)
    else:
        debug("Error: opPop - Dictionary stack is empty")


def dictPush(value): 
    dictStack.append(value)

def lookup(name):
    if len(dictStack) == 0:
        return False
    for d in dictStack:
        if name in d.keys():
            return d[name]
    else: return False
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



def isNumber(x):
    if type(x)==int or type(x)==float:
        return True
    return False

def isBool(x):
    if type(x)==bool:
        return True
    return False

def convert(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            if x == 'true':
                return True
            elif x == 'false':
                return False
            else:
                return x


def _GET(x,linker, mode):
    print("looking for: " + x)
    found = False
    foundLink = linker
    #dynamic linking mode (top->down searching through all dictionaries)
    if mode == "-d":
        temp = []
        for D in dictStack:
            if x in D[0].keys():
                try:
                    temp = D[0][x].copy()
                except:
                    temp = D[0][x]
                found = True

    #Static linking mode (searching through latest *related* dictionaries
    else:
        temp = []
        searching = True
        link = linker
        while searching == True:
            print("Link: " +  str(link))
            print(str(dictStack[link][1]))
            if x in dictStack[link][0].keys():
                try:
                    temp = dictStack[link][0][x].copy()
                except:
                    temp = dictStack[link][0][x]
                foundLink = link
                found = True
                searching = False
            else:
                link = dictStack[link][1]
                if link == None:
                    searching = False

    # if we've found a value for x, then lets use it!
    if found == True:
        if len(temp) > 1:
            print("interpreting...new link: " + str(len(dictStack) - 1))
            interpretHelper(temp, mode)
        else:
            z = convert(temp[0])
            if isNumber(z) == True or isBool(z) == True:
                print("pushing...")
                opPush(z)
            else:
                print("getting...")
                _GET(temp[0],foundLink, mode)
    else:
        return False
    return True

########################################################################

def psIf():
    helps = opPop()
    choice = opPop()
    if bool(choice):
        interpretHelper(helps, "-s")

def psIfelse():
    elseing= opPop()
    ifs= opPop()
    choice = opPop()
    if bool(choice):
        interpretHelper(ifs, "-s")
    else:
        interpretHelper(elseing, "-s")

##################################################################

############# Test functions/Cases ####################


def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testEq():
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        return False
    return True

def testLt():
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        return False
    return True

def testGt():
    opPush(3)
    opPush(6)
    gt()
    if opPop() != False:
        return False
    return True

#String operator tests
def testLength():
    opPush("(CptS355)")
    length()
    if opPop() != 7:
        return False
    return True

def testGet():
    opPush("(CptS355)")
    opPush(3)
    get()
    if opPop() != 83:
        return False
    return True

def testGetinterval():
    opPush("(CptS355)")
    opPush(4)
    opPush(3)
    getinterval()
    if opPop() != '(355)':
        return False
    return True

#boolean operator tests
def testPsAnd():
    opPush(True)
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsOr():
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True:
        return False
    return True

def testPsNot():
    opPush(True)
    psNot()
    if opPop() != False:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opStack)
    opPush(10)
    pop()
    l2= len(opStack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-3)
    roll()
    if opPop()==4 and opPop()==3 and opPop()==2 and opPop()==5 and opPop()==1:
        return True
    return False

def testRoll2():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(6)
    opPush(4)
    opPush(-1)
    roll()
    if opPop()==3 and opPop()==6 and opPop()==5 and opPop()==4 and opPop()==2 and opPop()==1:
        return True
    return False

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opStack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True


def main_partA():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv),  ('eq', testEq), \
                 ('lt', testLt),  ('gt', testGt),('length', testLength),('get', testGet), ('getinterval', testGetinterval),
                 ('psAnd', testPsAnd), ('psOr', testPsOr), ('psNot', testPsNot),
                 ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll), ('copy', testCopy),
                 ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests != []:
        return ('Some tests failed', failedTests)
    else:
        return ('All tests OK')



if __name__ == '__main__':
    print(main_partA())

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

def interpretHelper(values, linkers, mode):
    for value in values:
        try:
            opPush(int(value))
        except:
            if value == "add":
                add()
            elif value == "sub":
                sub()
            elif value == "mul":
                mul()
            elif value == "div":
                div()
            elif value == "eq":
                eq()
            elif value == "lt":
                lt()
            elif value == "gt":
                gt()
            elif value == "length":
                length()
            elif value == "get":
                get()
            elif value == "getinterval":
                getinterval()
            elif value == "and":
                psAnd()
            elif value == "or":
                psOr()
            elif value == "not":
                psNot()
            elif value == "dup":
                dup()
            elif value == "roll":
                roll()
            elif value == "exch":
                exch()
            elif value == "pop":
                pop()
            elif value == "copy":
                copy()
            elif value == "clear":
                clear()
            elif value == "stack":
                stack()
            elif value == "begin":
                begin()
            elif value == "end":
                end()
            elif value == "dict":
                psDict()
            elif value == "def":
                psDef()
            elif value == "if":
                psIf()
            elif value == "ifelse":
                psIfelse()
            elif value == "ifelsee":
                print("doesn't work")
            elif value == "true":
                opPush(True)
            elif value == "false":
                opPush(False)
            elif value[0] == '/':
                opPush(str(value))
            elif value[0] == '(':
                opPush(str(value))
            else:
                findingFunc = lookup(str(value))
                if findingFunc != False:
                    if type(findingFunc) == type([]):
                        interpretHelper(findingFunc, linkers, mode)
                    else:
                        opPush(findingFunc)
                else:
                    opPush(value)
                    _GET(value, linkers, mode)

def interpreter(n):
    a = "-s"
    interpretHelper(parse(tokenize(n)), opStack, a)


input1 = """
/square {
 dup mul
} def
(square)
4 square
dup 16 eq true and
{(pass)} {(fail)} ifelse
"""

input2 ="""
(facto) dup length /n exch def
/fact {
 0 dict begin
 /n exch def
 n 2 lt
 { 1}
 {n 1 sub fact n mul }
 ifelsee
 end
} def
n fact stack
"""

input3 = """
/lt6 { 6 lt } def
1 2 3 4 5 6 4 -3 roll
dup dup lt6 exch 3 gt and {mul mul} if
stack
clear
"""


input4 = """
(CptS355_HW5) 4 3 getinterval
(355) eq
{(You_are_in_CptS355)} if
 stack
 """



def Part_Two():
    print("Input_1 Test:")
    interpreter(input1)
    a = stack()
    clear()
    clearDict()

    print("\n Input_2 Test:")
    b = interpreter(input2)
    clear()
    clearDict()

    print("\n Input_3 Test:")
    c = interpreter(input3)
    clear()
    clearDict()

    print("\n Input_4 Test:")
    d = interpreter(input4)


Part_Two()
input() #so prompt doesn't close automatically

