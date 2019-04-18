import researcher_paper
import config

f_j = open("D:/Github/Researcher_Profiling/data/jimpact.txt", "r", encoding="utf8")
f_c = open("D:/Github/Researcher_Profiling/data/cimpact.txt", "r", encoding="utf8")
j_dict = {}
c_dict = {}
for line in f_j:
    line = line[:len(line)-1]
    # print(line)
    c = line.split(' ')
    factor = float(c[1])
    j_dict[c[0]] = factor

for line in f_c:
    line = line[:len(line)-1]
    # print(line)
    c = line.split(' ')
    factor = float(c[1])
    c_dict[c[0]] = factor

def get_work_profile(sname):
    j_year2factor = {}
    c_year2factor = {}
    sum=0
    error=0
    for paper in researcher_paper.get_researcher_papers(researcher_paper.get_researcher_id(researcher_paper.get_pinyin(sname))):
        tmp = researcher_paper.get_researcher_poapers_cj(paper)
        if tmp != ("None", "None", "None"):
            sum+=1
            # print(tmp[0], tmp[1], tmp[2])
            if tmp[0] == "journal":
                if tmp[2] not in j_year2factor.keys():
                    j_year2factor[tmp[2]] = []
                    if tmp[1] not in j_dict.keys():
                        error+=1
                    else:
                        j_year2factor[tmp[2]].append(j_dict[tmp[1]])
                else:
                    if tmp[1] not in j_dict.keys():
                        error+=1
                    else:
                        j_year2factor[tmp[2]].append(j_dict[tmp[1]])
            elif tmp[0] == "conference":
                if tmp[2] not in c_year2factor.keys():
                    c_year2factor[tmp[2]] = []
                    if tmp[1] not in c_dict.keys():
                        error+=1
                    else:
                        c_year2factor[tmp[2]].append(c_dict[tmp[1]])
                else:
                    if tmp[1] not in c_dict.keys():
                        error+=1
                    else:
                        c_year2factor[tmp[2]].append(c_dict[tmp[1]])
    # get_researcher_poapers_cj("1")
    print("finish", sum, "with", error, "errors.")
    print("jy", j_year2factor)
    print("cy", c_year2factor)
    return j_year2factor, c_year2factor

if __name__ == "__main__":
    get_work_profile("傅洛伊")