#-*-coding: utf-8-*-
icerik=(open("toşti.py","r").read()).split()
a=[float(icerik[i])for i in range(len(icerik))]
for i in range(len(a)):
    for q in range(len(a)-1):
        if(a[q]>a[q+1]):
            b=a[q]
            
            a[q]=a[q+1]
            a[q+1]=b           
a=(open("tastan.py","w").write(str(a)))
