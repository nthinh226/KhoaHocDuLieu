import openpyxl
def getValueExcel(fileName, cellName):
    wB = openpyxl.load_workbook(fileName)
    trang_tinh_1 = wB['Trang tính 1']    wB.close
    return trang_tinh_1[cellName].valuedef
updateValueExcel(fileName, cellName, value):
    wB = openpyxl.load_workbook(fileName)
    trang_tinh_1 = wB['Trang tính 1']
    trang_tinh_1[cellName].value = value
wB.close()
wB.save(fileName)
fileName = "D:\\xyz.xlsx"
tongList = []
for i in range(2, 8 + 1):
tongList.append(getValueExcel(fileName, 'D' + str(i))
getValueExcel(fileName, 'E' + str(i)))
for i in range(len(tongList)):
updateValueExcel(fileName, 'F' + str(i + 2), tongList[i])








