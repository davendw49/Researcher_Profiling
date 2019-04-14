import pymysql
import config

def get_conf_citation():
    db = pymysql.connect(host=config.ip, port=13306, user="readonly", passwd="readonly", db="mag-new-160205", charset='utf8')
    cursor = db.cursor()
    sql = "SELECT PaperID, CitationCount, PaperPublishYear, ConferenceSeriesIDMappedToVenueName FROM `Papers` WHERE ConferenceSeriesIDMappedToVenueName in (SELECT ConferenceSeriesID FROM ConferenceSeries WHERE UnderCS=1);"
    citation = {}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            # print(row)
            if row[3] not in citation.keys():
                citation[row[3]] = {}
            else:
                if row[2] not in citation[row[3]]:
                    citation[row[3]][row[2]] = int(row[1])
                else:
                    citation[row[3]][row[2]] += int(row[1])
    except:
        print("Error: unable to fetch data")
    db.close()
    return citation
    # for i in citation.keys():
    #     print(citation[i])

# get_conf_citation()

def get_jour_citation():
    db = pymysql.connect(host=config.ip, port=13306, user="readonly", passwd="readonly", db="mag-new-160205", charset='utf8')
    cursor = db.cursor()
    sql = "SELECT PaperID, CitationCount, PaperPublishYear, JournalIDMappedToVenueName FROM `Papers` WHERE JournalIDMappedToVenueName in (SELECT JournalID FROM Journals WHERE UnderCS=1);"
    citation = {}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            # print(row)
            if row[3] not in citation.keys():
                citation[row[3]] = {}
            else:
                if row[2] not in citation[row[3]]:
                    citation[row[3]][row[2]] = int(row[1])
                else:
                    citation[row[3]][row[2]] += int(row[1])
    except:
        print("Error: unable to fetch data")
    db.close()
    return citation
    # for i in citation.keys():
    #     print(citation[i])

# get_jour_citation()

# factor = \sum [(2019-year) * 1/100 * citation]
def get_impact(year=2019, l=0.1):
    jcitation = get_jour_citation()
    ccitation = get_conf_citation()
    jimpact = {}
    cimpact = {}
    for key in jcitation.keys():
        tmp = jcitation[key]
        factor = 0
        for y in tmp.keys():
            factor += l * tmp[y]/(year - int(y) + 1) 
        jimpact[key] = factor

    for key in ccitation.keys():
        tmp = ccitation[key]
        factor = 0
        for y in tmp.keys():
            factor += l * tmp[y]/(year - int(y) + 1) 
        cimpact[key] = factor

    f1 = open("jimpact.txt", 'w', encoding='utf8')
    f2 = open("cimpact.txt", 'w', encoding='utf8')

    for item in jimpact.keys():
        print(item, jimpact[item], file=f1)
    for item in cimpact.keys():
        print(item, cimpact[item], file=f2)

    f1.close()
    f2.close()

get_impact()