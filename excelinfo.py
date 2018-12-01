# Stefan Norling
# sfn2mc

# Reading an excel file using Python
import xlrd
import re
import csv
import sys

def firstway():
    # To open Workbook
    wb = xlrd.open_workbook("tweets.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)

    users = []
    edges = []

    rows = sheet.nrows

    j = 0
    maxtags = 0
    counter = 0

    for line in range(100):
        name = sheet.cell_value(line,1)
        users.append(name)
        #hashtags = re.findall(r"#(\w+)", sheet.cell_value(line,7))
        temp = sheet.cell_value(line,10)
        temp = temp[1:]
        temp = temp[:-1]
        hashtags = temp.split(",")
        print(counter)
        counter += 1
        if len(temp) > 0:
            for each in hashtags:
                q = line
                while q < rows:
                    k = 0
                    subhts = sheet.cell_value(q,10)
                    subhts = subhts[1:]
                    subhts = subhts[:-1]
                    subhts = subhts.split(",")
                    lensub = len(subhts)
                    while k < lensub:
                        othername = sheet.cell_value(q,1)
                        if each == subhts[k] and name != othername:
                            edges.append([name, othername, each.encode('utf8')])
                        k += 1
                    q += 1
                #print("second part")

    users.sort()

    i = 0
    lenusers = len(users)

    if lenusers > 1:
        while i + 1 < lenusers:
            if users[i] == users[i + 1]:
                del users[i + 1]
                lenusers -= 1
            else:
                i += 1


    for user in range(lenusers):
        users[user] = [users[user]]
    del users[0]

    print("third part")

    # for line in range(rows):
    #     i = 0
    #     tempdata = []
    #     #user = sheet.cell_value(line,0)
    #     name = sheet.cell_value(line,1)
    #     hashtags = re.findall(r"#(\w+)", sheet.cell_value(line,7))
    #     numtags = len(hashtags)
    #     if numtags > maxtags:
    #         maxtags = numtags
    #     #tempdata.append(name)
    #     #while i < numtags:
    #      #   tempdata.append(hashtags[i])
    #       #  i += 1
    #     if numtags > 0:
    #         data.append([name,hashtags])
    #         j += 1
    #
    # #print(maxtags)
    # #print(data)
    #
    # edges = []
    #
    # person = 0
    # # j is the people in the file
    # while person < 500:
    #     hashindex = 0
    #     peopleleft = person + 1
    #     # hashes is how many hashtags are in a persons tweet
    #     hashes = len(data[person][1])
    #     while hashindex < hashes:
    #         while peopleleft < j:
    #             hashindex2 = 0
    #             hashes2 = len(data[peopleleft][1])
    #             while hashindex2 < hashes2:
    #                 if data[person][1][hashindex] == data[peopleleft][1][hashindex2] and data[person][0] != data[peopleleft][0] and len(data[person][1][hashindex]) > 2:
    #                     edges.append([data[person][0],data[peopleleft][0],data[person][1][hashindex]])
    #                 hashindex2 += 1
    #             peopleleft += 1
    #         hashindex += 1
    #     person += 1
    #     print(person)

    nodes = open("users_way1.csv", "w")
    with nodes:
        writer = csv.writer(nodes)
        writer.writerows(users)

    edgesfile = open("edges_way1.csv", "w")
    with edgesfile:
        writer = csv.writer(edgesfile)
        writer.writerows(edges)

def secondway():
    # To open Workbook
    # oof
    wb = xlrd.open_workbook("tweets.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)

    users = []
    data = []
    edges = []
    rows = sheet.nrows

    for line in range(rows):
        name = sheet.cell_value(line,1)
        users.append([name, 1])
        #hashtags = re.findall(r"#(\w+)", sheet.cell_value(line,7))
        temp = sheet.cell_value(line,10)
        temp = temp[1:]
        temp = temp[:-1]
        hashtags = temp.split(",")
        # if hashtags:
        #     for each in hashtags:
        #         if len(each) > 1:
        #             data.append([each])
        #             edges.append([name, each])
        if len(temp) > 0:
            for each in hashtags:
                each = each.encode('utf8')
                data.append([each, 2])
                #users.append([each, 2])
                edges.append([name, each, 1])

    users.sort()
    data.sort()

    i = 0
    lenusers = len(users)
    lendata = len(data)

    if lenusers > 1:
        while i + 1 < lenusers:
            if users[i][0] == users[i + 1][0]:
                del users[i + 1]
                lenusers -= 1
            else:
                i += 1
    del users[0]

    i = 0
    if lendata > 1:
        while i + 1 < lendata:
            if data[i][0] == data[i + 1][0]:
                del data[i + 1]
                lendata -= 1
            else:
                i += 1

    for moi in data:
        users.append(moi)

    nodesfile = open("users_way2.csv", "w")
    with nodesfile:
        writer = csv.writer(nodesfile)
        writer.writerows(users)

    #nodesfile2 = open("hashtags_way2.csv", "w")
    #with nodesfile2:
    #    writer = csv.writer(nodesfile2)
    #    writer.writerows(data)

    edgesfile = open("edges_way2.csv", "w")
    with edgesfile:
        writer = csv.writer(edgesfile)
        writer.writerows(edges)

#firstway()
#secondway()