# coding=utf-8
# Author : WenyuZheng
# Date : 2018/7/5 12:30

'''
LISP语言唯一的语法就是括号要配对。 形如 (OP P1 P2 ...)，括号内元素由单个空格分割
其中第一个元素OP为操作符，后续元素均为其参数，参数个数取决于操作符类型注意：参数 P1, P2 也有可能是另外一个嵌套的 (OP P1 P2 ...)
当前OP类型为 add / sub / mul / div（全小写），分别代表整数的加减乘除法
简单起见，所有 OP 参数个数均为 2。
举例:
输入：(mul 3 -7)
输出：-21

输入：(add 1 2)
输出：3

输入：(sub (mul 2 4) (div 9 3))
输出：5

输入：(div 1 0)
输出：error

题目涉及数字均为整数，可能为负；不考虑32位溢出翻转 除零错误时，输出 "error"，除法遇除不尽，取整，即 3/2 = 1
'''

def lisp(exp = ''):
    if exp == '':
        print('InvalidExpression')
        return
    op_stack = [] #运算符栈
    str_stack = [] #除运算符以外的字符栈
    i = 0
    flag = 0
    invalid_exp = 0
    result = 0

    # for循环必须下标i逐个遍历，不能跳
    # for i in range(len(exp)):

    while i<len(exp):
        if exp[i] == ' ':
            i = i + 1
            continue
        elif exp[i] == '(':
            str_stack.append(exp[i])
            while (1):
                next_space_index = exp.find(' ', i)
                if next_space_index == -1:
                    print('InvalidExpression')
                    return
                if next_space_index - i < 2:
                    i = i + 1
                    flag = 1
                    continue
                break
            if flag == 0:
                op_tmp = exp[i+1:next_space_index]
            else:
                op_tmp = exp[i:next_space_index]
            op_stack.append(op_tmp)
            i = next_space_index + 1
            flag = 0
        elif exp[i] == ')':
            if len(op_stack) == 0:
                print('InvalidExpression')
                return
            op = op_stack.pop()
            #pop out 2 number
            num1 = int(str_stack.pop())
            num2 = int(str_stack.pop())
            #pop out '('
            str_stack.pop()
            if op == 'add':
                result = num2 + num1
            elif op == 'sub':
                result = num2 - num1
            elif op == 'mul':
                result = num2 * num1
            elif op == 'div':
                if num1 == 0:
                    print('error')
                    return
                result = int(num2 / num1)
            else:
                print('InvalidExpression')
                return
            str_stack.append(result)
            i = i + 1
        else:
            space = exp.find(' ', i)
            paren = exp.find(')', i)
            if paren < space or space == -1:
                str_tmp = exp[i:paren]
            else:
                str_tmp = exp[i:space]
            str_stack.append(str_tmp)
            i = i + 1
    result = str_stack.pop()
    if len(str_stack) >0 or len(op_stack) >0 or invalid_exp == 1:
        print('InvalidExpression')
        return
    else:
        print(result)
        return



lisp()  #InvalidExpression
lisp('(')   #InvalidExpression
lisp(')')   #InvalidExpression
lisp('()')  #InvalidExpression
lisp('(sub (mul 2 4) (div 9 3))')   #5
lisp('( sub ( mul 2 4 ) ( div 9 3 ) ) ')
lisp('( sub ( mul 2 4 ) ( div 9 3 )  ')
lisp('(sub (mul 2 4 (div 9 3))')



