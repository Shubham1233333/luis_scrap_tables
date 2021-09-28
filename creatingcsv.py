import csv



def csv_making(new):
    print(new,"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    with open('f11111.csv', 'a') as f:

        write = csv.writer(f, delimiter = ','  )
        
        write.writerow(new)
        f.close()
        new.clear()