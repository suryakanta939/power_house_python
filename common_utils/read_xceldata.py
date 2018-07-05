import xlrd
import os


class ReadXcelData():

    def readData(self,fileName,sheetName):

        workingDir=os.path.dirname(__file__)
        destinationDir="../test_data/"
        file=destinationDir+fileName+".xlsx"
        desitinationFile=os.path.join(workingDir,file)
        wb=xlrd.open_workbook(desitinationFile)
        sheet=wb.sheet_by_name(sheetName)
        rows=sheet.nrows
        print("total no of rows: "+str(rows))
        cols=sheet.ncols
        print("total no of rows: " + str(cols))
        datas=[]

        for row in range(1,rows):
            rowdata=[]
            datas.append(rowdata)
            for col in range(0,cols):
                cellValue=sheet.cell_value(row,col)
                rowdata.append(cellValue)
        return datas

