import xml.etree.ElementTree as ET
//Uer foodMenu.xml file from Python directory
tree = ET.parse('foodMenu.xml')
root = tree.getroot();
print(root.tag);
print("Food\tPrice\tSize\tCalories")
for child in root:
    print(child[0].text+'\t'+child[1].text+'\t'+child[2].text+'\t'+child[3].text);
    
