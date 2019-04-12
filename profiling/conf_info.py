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
    for i in citation.keys():
        print(citation[i])

# get_conf_citation()

def get_jour_citation():
    db = pymysql.connect(host=config.ip, port=13306, user="readonly", passwd="readonly", db="mag-new-160205", charset='utf8')
    cursor = db.cursor()
    sql = "SELECT PaperID, CitationCount, PaperPublishYear, JournalIDMappedToVenueName FROM `Papers` WHERE JournalIDMappedToVenueName in (SELECT JournalID FROM Journals WHERE UnderCS=1) LIMIT 10;"
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
    for i in citation.keys():
        print(citation[i])

get_jour_citation()