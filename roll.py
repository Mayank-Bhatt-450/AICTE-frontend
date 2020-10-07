l1=[]
l2=[]
l3=[]
l4=[]
stack=[[" roll no. ","   Aadhar no.  ","NAME","D/O/B", "FATHER'S NAME","  Pan no. ","NAME","D/O/B", "FATHER'S NAME","  Account no.  ","Aadhar no."]]
sk=["   ---    ",    "     ###       "," -- "," --  ","       ----     ","   ###    "," -- ","  -- ","        --      ","Aadhar no.","    --    "]
aicte=open("aicte.csv","r")#poen .csv read data and close for ex:- "123,123\n23,34\n"=[[123 , 123],[23,34],[]]
tem=aicte.read()
for i in tem.split('\n'):
    l1.append(i.split(','))
aicte.close()
aicte=open("pan.csv","r")
tem=aicte.read()
for i in tem.split('\n'):
    l3.append(i.split(','))
aicte.close()
aicte=open("adhar.csv","r")
tem=aicte.read()
for i in tem.split('\n'):
    l2.append(i.split(','))
aicte.close()
aicte=open("bank.csv","r")
tem=aicte.read()
for i in tem.split('\n'):
    l4.append(i.split(','))
aicte.close()
#print l1,'\n',l2,'\n',l3,'\n',l4,'\n',
def roll(code):
    for i in range(1,len(l1)-1):
        #print(int(code),"-------",int(l1[i][1][2:5]))
        if str(code)==str(l1[i][1]):
            tem=[]
            tem.append(l1[i][1])
            flg=0
            for j in range(1,len(l2)):
                #print l1[i][6],"<-l1|l2->",l2[j][0]
                if l1[i][6]==l2[j][0]:
                    flg=1
                    tem.append(l2[j][0])
                    F=2
                    for k in range (1,len(l2[j])):
                        #print l1[i][k+1],"<-l1|l2->",l2[j][k]
                        if l1[i][k+1]==l2[j][k]:
                            tem.append(sk[F])
                        else:
                            tem.append(l2[0][k])
                        F+=1
            if flg==0:
                ws=[]
                for i2 in range(1,5):
                    
                    ws.append(sk[i2])
                print ws
                tem.extend(ws)
                    
            flg = 0
            for j in range(1,len(l3)):
                #print l1[i][5],"------------",l3[j][0]
                if l1[i][5]==l3[j][0]:
                    flg=1
                    f=6
                    tem.append(l3[j][0])
                    for k in range (1,len(l3[j])):
                        #print l1[i][k+1],"<-l1|l3->",l3[j][k]
                        if l1[i][k+1]==l3[j][k]:
                            tem.append(sk[f])
                        else:
                            tem.append(l3[0][k])
                        f+=1
            if flg==0:
                ws=[]
                for i2 in range(5,9):
                    ws.append(sk[i2])
                print ws
                tem.extend(ws)
                    #print"------------------------------------------"
            #print i,"=>",tem
            flg=0
            for j in range(1,len(l4)):
                #print l1[i][7],"<-l1|l4->",l4[j][0]
                if l1[i][7]==l4[j][0]:
                    flg=1
                    f=9
                    tem.append(l4[j][0])
                    #print tem
                    #print l1[i][6],"<-",[i],[6],"l1|l4",[j],[1],"->",l4[j][1]
                    if l1[i][6]==l4[j][1]:
                        tem.append(sk[f+1])
                    else:
                        #print "enter wrong"
                        tem.append(sk[9])
                    #print"----------------------------"
                    f+=1
            if flg==0:
                tem.extend(["      ###      ","    --    "])
            #print len(tem)
            if tem[2]==" -- " and tem[3]==" --  "and tem[4]=="       ----     " and tem[6]==' -- ' and tem[7]=="  -- "and tem[8]=="        --      "and tem[10]=="    --    "and tem[1]!="     ###       "and tem[5]!="   ###    "and tem[9]!="      ###      " :
                pass
            else:
                #pass
                stack.append(tem)
    df=""
    l=stack
    for i in range(len(l)):
        df+=str(l[i]).strip('[').strip(']').replace("',", ",").replace(", '", ",").lstrip("'").rstrip("'").strip('"')+"\n"
    return(df)
    #print stack,"\n",len(stack)
###########################################################################################################################


##########################################################################################################################

