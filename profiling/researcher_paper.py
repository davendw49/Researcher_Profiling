from pypinyin import lazy_pinyin
import pymysql

def get_pinyin(word):
    result = lazy_pinyin(word, errors="ignore")
    if len(result) == 0:
        return word
    else:
        fn_ = result[1:len(result)]
        ln = result[0]
        # print(fn, ln)
        fn = ''.join(fn_)
        name = str(fn) + " " + str(ln)
        return name

# print(get_pinyin("王新兵"))

def get_researcher_id(name):
    db = pymysql.connect(host="202.120.36.29", port=13306, user="readonly", passwd="readonly", db="mag-new-160205", charset='utf8')
    # SELECT * FROM `Authors` where AuthorName = 'xinbing wang' ORDER BY PaperCount DESC LIMIT 1;
    cursor = db.cursor()
    sql = "SELECT AuthorID FROM `Authors` where AuthorName = '" + name + "' ORDER BY PaperCount DESC LIMIT 1;"
    # print(sql)
    id = 0
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
    except:
        print("Error: unable to fetch data")
    db.close()
    return id

# get_researcher_id(get_pinyin("傅洛伊"))

def get_researcher_papers(id):
    db = pymysql.connect(host="202.120.36.29", port=13306, user="readonly", passwd="readonly", db="mag-new-160205", charset='utf8')
    # SELECT * FROM `Authors` where AuthorName = 'xinbing wang' ORDER BY PaperCount DESC LIMIT 1;
    cursor = db.cursor()
    sql = "SELECT PaperID FROM PaperAuthorAffiliations WHERE AuthorID = '" + id + "';"
    papers = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            if row[0] not in papers:
                papers.append(row[0])
    except:
        print("Error: unable to fetch data")
    db.close()
    print("total paper of researcher", id, "is", len(papers))
    return papers

# get_researcher_papers("80008266")  

def get_researcher_poapers_cj(paperid):
    # print(paperid)
    db = pymysql.connect(host="202.120.36.29", port=13306, user="readonly", passwd="readonly", db="mag-new-160205", charset='utf8')
    cursor = db.cursor()
    sql = "SELECT ConferenceSeriesIDMappedToVenueName, JournalIDMappedToVenueName, PaperPublishYear FROM Papers WHERE PaperID = '" + paperid + "' LIMIT 1;"
    conference = []
    journal = []
    year = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            conference.append(row[0])
            journal.append(row[1])
            year.append(row[2])
    except:
        print("Error: unable to fetch data")

    if str(conference[0]) != "None":
        return "conference", conference[0], year[0]
    elif str(journal[0]) != "None":
        return "journal", journal[0], year[0]
    else:
        return "None", "None", "None"
