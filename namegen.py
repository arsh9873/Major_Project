st=1
ed=1999
ss="virus"
output=[]
while(st<=ed):
    output.append("/kaggle/input/assemblymalware/"+ss+"/"+str(st)+".txt")
    st=st+1

print(output)
