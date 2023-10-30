import pandas
get_info=input()  #input information from terminal
Area=None
total_geo_count=0
fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()
for line in info_list:
    Description=line[1]
    Description=Description[0:]
    if Description==get_info:
        Area=line[0]
        break
with open("data.csv","r") as f:
    next(f)
    for Line in f:
        row=Line.rstrip().split(",")
        l=len(row)
        if l==5:
            geo_count=int(row[3])
            if Area==row[1]:
                total_geo_count += geo_count
print(total_geo_count)