fname = input("Enter file name: ")
a = open(fname)

counts = dict()
#count = 0
for line in a:
    if line.startswith("From"):
        line = line.rstrip()
        b = line.split()
        if(len(b) == 2):
            continue
        else:
            counts[b[1]] = counts.get(b[1], 0) + 1

bigcount = None
bigwword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


#Idea: lấy file, lấy các dòng có from mail => split => lấy các dòng có from mail giờ => lưu các giá trị của mail là key, số lần là value vào dict
                



