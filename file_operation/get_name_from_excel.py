# 改文件名为序号,报错重复运行
import os
import xlwt  # 操作excel模块
import xlrd
import sys
import numpy as np
def get_excel():
    root = r'C:\joey\master\resource\lymphoma\tag'
    dir = r'C:\joey\master\resource\lymphoma\dataset\third_label_data\rename_t2_dicom3'
    file_path = root + '\\ti_weilai_num_list.xlsx'
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = f.add_sheet('sheet1')
    pathDir = os.listdir(dir)

    i = 0
    for s in pathDir:
        s = s.split('.')[0]
        if s.__contains__('MRI'):
            sheet.write(i, 0, s)
            sheet.write(i, 1, i)
            i = i + 1

    print(file_path)
    print(i)  # 显示文件名数量
    f.save(file_path)




input_file_name = r"C:\Users\perlicue\Desktop\master_lecture\xiaowen\wjq\wjq_num_list.xlsx"

dir_path = r"C:\Users\perlicue\Desktop\master_lecture\xiaowen\volume_cal2\output_fold"
def read_excel(input_file_name, path):

    workbook = xlrd.open_workbook(input_file_name)
    print(workbook)

    print(workbook.sheet_names())

    # table = workbook.sheet_by_index(0)
    # print(table)
    table = workbook.sheet_by_name('sheet1')
    print(table)

    rows = table.nrows
    cols = table.ncols
    print(cols)
    fileList = os.listdir(path)
    n = 0
    for file in fileList:

        oldname = path + os.sep + file
        print(oldname)
        for i in range(rows):
            if str(table.cell(i, 0).value) == file:
                newname = path + os.sep + str(int(table.cell(i, 1).value))
                os.rename(oldname, newname)
                print(oldname, '======>', newname)

        n += 1

def find_number_of_file(input_file_name, path):

    workbook = xlrd.open_workbook(input_file_name)
    print(workbook)

    print(workbook.sheet_names())

    # table = workbook.sheet_by_index(0)
    # print(table)
    table = workbook.sheet_by_name('sheet1')
    print(table)

    rows = table.nrows
    cols = table.ncols
    print(cols)
    fileList = os.listdir(path)
    n = 0
    for file in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + file  # os.sep添加系统分隔符
        for i in range(rows):
            if str(table.cell(i, 0).value) == file:
                # newname = path + os.sep + str(int(table.cell(i, 1).value))
                # os.rename(oldname, newname)
                newname = table.cell(i, 2).value
                print(oldname, '======>', newname)
        # 设置新文件名
        n += 1

def read_excel_trainData(input_file_name, path):
    """
    从xls文件中读取数据
    """
    workbook = xlrd.open_workbook(input_file_name)
    print(workbook)

    print(workbook.sheet_names())

    # table = workbook.sheet_by_index(0)
    # print(table)
    table = workbook.sheet_by_name('sheet1')
    print(table)

    rows = table.nrows
    cols = table.ncols
    print(cols)
    fileList = os.listdir(path)
    n = 0
    for file in fileList:

        oldname = path + os.sep + file
        for i in range(rows):
            # print("file:" + file)
            # print("excel:" + table.cell(i, 0).value)
            if table.cell(i, 0).value == file:
                newname = path + os.sep + str(int(table.cell(i, 1).value))
                os.rename(oldname, newname)
                print(oldname, '======>', newname)

        n += 1

def get_ful_name(c1, c2):
    workbook = xlrd.open_workbook(c1)
    table = workbook.sheet_by_name('Sheet1')
    rows = table.nrows
    workbook2 = xlrd.open_workbook(c2)
    table2 = workbook2.sheet_by_name('Sheet1')
    rows2 = table2.nrows

    root = r'C:\Users\perlicue\Desktop\spacial_feature'
    file_path = root + '\\tempName.xlsx'
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
    sheet = f.add_sheet('sheet1')

    for i in range(rows):
        for j in range(rows2):
            if table2.cell(j, 0).value.__contains__(table.cell(i, 0).value):
                # table.cell(i, 3).value = table2.cell(j, 0).value
                sheet.write(i,3,table2.cell(j, 0).value)
                print(table.cell(i, 0).value)

    f.save(file_path)
def contract_excel(file1, file2):
    workbook = xlrd.open_workbook(file1)
    table = workbook.sheet_by_name('new sheet')
    rows1 = table.nrows
    workbook2 = xlrd.open_workbook(file2)
    table2 = workbook2.sheet_by_name('Sheet1')
    rows2 = table2.nrows

    root = r'C:\Users\perlicue\Desktop\spacial_feature'
    file_path = root + '\\tempName.xlsx'
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = f.add_sheet('sheet1', cell_overwrite_ok=True)
    # sheet.write("infoPlist", cell_overwrite_ok = True)
    for i in range(rows1):
        for j in range(rows2):
            # print(table2.cell(j, 0).value)
            # print(table.cell(i, 1).value)
            if table2.cell(j, 0).value.strip().__contains__(table.cell(i, 1).value):

                sheet.write(i, 3, table2.cell(j, 0).value)


    f.save(file_path)
if __name__ == '__main__':
    c1 = r'C:\Users\perlicue\Desktop\spacial_feature\lymphoma20230330_mr_prooperative.xlsx'
    c2 = r'C:\joey\master\resource\lymphoma\patient_name_seq.xlsx'
    # contract_excel(c1, c2)
    # print(name1.__contains__(name2))
    input_file_name = r'C:\Users\perlicue\Desktop\spacial_feature\multi_seq_train\new_MRI_dicom_name_list.xlsx'
    path = r'C:\joey\master\resource\lymphoma\tag\58例'
    find_number_of_file(input_file_name, path)






