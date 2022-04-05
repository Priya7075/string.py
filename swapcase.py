# p="python proGRAMming"
# print(p.swapcase())#python  proGRAMming
# a=4; b=66
# print(a)#4
# del  a,b
# print(a,b)#nameerror=name is 'a' not find
# print("buy this for Rs.{d} or for Rs{ed}".format(d=11,ed=50))#buy this for Rs.11 or for Rs50
# a='R\tS\tV'
# print(a.expandtabs(0))#RSv
# print(a.expandtabs(1))# R S V
# print(a.expandtabs(2))#  R  s  v
# print(a.expandtabs(3))#R   s   v
# print(a.expandtabs(4))#R    s    v
# print(a.expandtabs(5))#R     s     v
# print(a.expandtabs(6))#R      s      v
# print(a.expandtabs(7))#R       s        v
# print(a.expandtabs(8))#R        s        v
# print(a.expandtabs())#R        s         v
# print(a.expandtabs(-1))#RSV
# v='indu','priya','vamsi'
# n='priya'
# print(('-'.join(v)))#indu-priya-vamsi
# print(('*'.join(n)))#p*r*i*y*a
# print('*'.join("Hello"))#H*e*l*l*o
# r="vamsy vamsi"
# a=r.maketrans("y",'r')
# print(a,type(a))#dict
# print((r.translate(a)))#vamsr vamsi
# r="vamsy vamsi"
# a=r.maketrans("y",'aa')
# print(a,type(a))#dict
# # print(r.translate(a))#valueeror
# r="vamsy vamsy"
# a=r.maketrans("ym",'ab')
# print(a,type(a))#dict
# print(r.translate(a))#vabsa vabsa
# r={}
# print(r,type(r))
# v={1:'hello', 2:'python'}
# print(v[2])#python
# a="hello\ncore python\nprogramming"
# print(a)#hello nextline core pythonnextlineprogramming
# g=a.splitlines()
# print(g,type(g))#['hello','core','python','programming']
# print(g[0])#hello
# print(g[2])#programming
# print(g[8])#indexerroe :list index out of range
# h="HelloWelcome to josh Innovations"
# print(h.split(" "))#['Hellowelcome','to', 'Innovations']
# print(h.split())#['HelloWelcome','to','Innovations']
# print(h.split(""))#valueeror empty separator
# a=5.6,7
# print(a,type(a))#tuple
# a=[int(x) for x in input().split()]
# print(a,type(a))#valueeror
# print(sum(a))#28
# print("the sum is"+' '+str(sum(a)))#the sum is 28
# print("the sum is",sum(a))#the sum is 28
# v="Hello welcome to joshInnovatoins"
# print(v.split())#['Hello' ,'Welcome','to','joshInnovations']
# b="hello: welcome: To: josh:Innovatoins"
# print(b.split(":"))#['Hello','Welcome','To','josh','Innovations']
# v=r"hello\nollywood"#str
# print(v,type(v))#hello\nollywood
# k="Hello!\nWelcome to \njoshInnovations" 
# print(k.splitlines(True))#['Hello!\n','Welcome to \n','joshInnovations]
# f="hello"
# print(f.zfill(6))#0hello
# j="Hey! How are you Doing?"
# print(j.partition("are"))#'Hey! How','are','you Doing'
# t="Hey! How are you Doing?"
# r=t.partition("you")#'Hey! How are','you','Doing'
# print(r)
# print(r[2])#Doing
# m="We are learning python programming , python is Basic need \
    # for ML,DS,AI,DL,Bigdata..etc"
# print(m.partition("python"))
# print(m.partition("python"))
# c="python"
# # print(c.ljust(8),"programming Basic")#python  programming Basic
# c="python"
# print(c.rjust(8),"programming Basic")#  python programming Basic
# z="vamsy"
# print(z.rjust(10,'R'))#RRRRvamsy
# v="vamsy"
# # print(v.ljust(10,'R'))#vamsyRRRR
# W="vamsy, indu, priya"
# d=W.rsplit(",",0)
# t=W.rsplit(", ",  1)
# r=W.split(", ", 1)
# print(d)#['vamsy,indu,priya']
# print(t)#['vamsy, indu', 'priya']
# # print(r)#['vamsy', 'indu, priya']