import matplotlib.pyplot as plt

f_j = open("D:/Github/Researcher_Profiling/data/jimpact.txt", "r", encoding="utf8")
f_c = open("D:/Github/Researcher_Profiling/data/cimpact.txt", "r", encoding="utf8")
j_dict = {}
c_dict = {}
jn = []
cf = []
for line in f_j:
    line = line[:len(line)-1]
    # print(line)
    c = line.split(' ')
    factor = float(c[1])
    j_dict[c[0]] = factor
    jn.append(factor)
    
for line in f_c:
    line = line[:len(line)-1]
    # print(line)
    c = line.split(' ')
    factor = float(c[1])
    c_dict[c[0]] = factor
    cf.append(factor)
    
print(max(jn), min(jn))
print(max(cf), min(cf))

# jn1 = sorted(jn)

sum=0
for i in jn:
    sum+=1

plt.subplot(111)
plt.plot(range(0,sum), jn, color='r')
plt.show()