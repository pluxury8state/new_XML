

def sort_and_top10(ob):
    new_mas = sorted(ob, key=lambda mas: mas[1])

    a = int(len(new_mas)) - 1

    p = 0

    print('top 10')

    while p != 10:
        print(new_mas[a])
        a -= 1
        p += 1


def counter(ob):
    mas4 = []

    for ind in ob:
        p = 0
        for i in mas4:
            if ind[0] != i[0]:
                continue
            else:
                p = 1
                break
        if p != 0:
            continue
        else:
            mas4.append(ind)

    sort_and_top10(mas4)


def add(ob):

    mas3 = []

    for ind in ob:
        a = [ind]
        a.append(ob.count(ind))
        mas3.append(a)

    counter(mas3)


def more_then_6(ob):
    mas2 = []
    for ind in ob:
        if len(ind) > 6:
             mas2.append(ind)


    add(mas2)









import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
describe = []
root = tree.getroot()

#begin

xml_items = root.findall("channel/item")

for item in xml_items:
   des = item.find("description")
   describe += des.text.split(" ")

more_then_6(describe)
























