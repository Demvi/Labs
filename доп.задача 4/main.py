import csv

p = 0
o = []

with open('jjj.csv',"r",) as csvfile:
    x = list(csv.reader(csvfile,delimiter = ";"))
    #print(x)
    for i in x:
        p = p+1
        if p>57:
            q = i[7]
            if "in  Word" in q:
                z = q.split(" ")


                if len(z)==6:
                    if int(z[1]) >= 8:
                        z[1] = str(int(z[1]) - 8)

                        l = int(z[5][2:5])
                        l = l * 2
                        z[5] = z[5].replace(z[5][2:5], str(l))
                    else:
                        l = int(z[5][2:5])
                        l = l * 2 + 1
                        z[5] = z[5].replace(z[5][2:5], str(l))

                else:
                    if int(z[0]) >= 8:
                        z[0] = str(int(z[0]) - 8)

                        l = int(z[4][2:5])
                        l = l * 2
                        z[4] = z[4].replace(z[4][2:5], str(l))
                    else:
                        l = int(z[4][2:5])
                        l = l * 2 + 1
                        z[4] = z[4].replace(z[4][2:5], str(l))
                #print(z)

                q = " ".join(z)

            elif "DW" in q or "DB" in q or "DD" in q:
                l = int(q[2:5])
                l = l * 2
                q = q.replace(q[2:5], str(l))

                q = q.replace("DW","DBW")
                q = q.replace("DD", "DBD")

            i[7] = q
            d=i
            print(q)
            #print(i)
        else:
            d = i

        o.append(d)

with open("finally.csv","w",newline='') as t:
    write = csv.writer(t, delimiter =';')
    for i in o:
        write.writerow(i)

 