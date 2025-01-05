# coding=utf-8
import os

import xlrd
import xlwt  # 操作excel模块
from xlrd import open_workbook
from xlutils.copy import copy

def excel_export():
    root = r'C:\Users\perlicue\Desktop\spacial_feature\multi_seq_train'
    dir = r'C:\Users\perlicue\Desktop\spacial_feature\multi_seq_train\match_label_dicom'
    file_path = root + '\\map_name_number_list.xlsx'
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = f.add_sheet('sheet1')
    pathDir = os.listdir(dir)

    i = 0
    for s in pathDir:
        if s.__contains__(''):
            sheet.write(i, 0, s)
            # if i<60:
            #     s = s.split('_')[1] + '_' + s.split('_')[2] + '_' + s.split('_')[3]
            # s = s.split('_')[0] + '_' + s.split('_')[1] + '_' + s.split('_')[2]
            # sheet.write(i, 0, s)
            sheet.write(i, 1, i + 1)
            i = i + 1

    print(file_path)
    print(i)  # 显示文件名数量
    f.save(file_path)

def excel_match_add_category():
    output = r'C:\Users\perlicue\Desktop\spacial_feature\multi_seq_train\new_MRI_dicom_name_list.xlsx'
    input = r'C:\Users\perlicue\Desktop\spacial_feature\pathology_name_list.xlsx'
    workbook2 = xlrd.open_workbook(input)
    table2 = workbook2.sheet_by_name('Sheet1')
    rows2 = table2.nrows

    rexcel = open_workbook(output, formatting_info=True)

    rows = rexcel.sheets()[0].nrows

    excel = copy(rexcel)

    table3 = rexcel.sheet_by_name('sheet1')
    table = excel.get_sheet(0)
    for i in range(0, rows):
        for j in range(0, rows2):
            if table3.cell(i, 0).value.strip().__contains__(table2.cell(j, 1).value.strip()):
                table.write(i, 3, table2.cell(j, 7).value.strip())
                table.write(i, 4, table2.cell(j, 8).value.strip())

    excel.save(output)

if __name__ == '__main__':
    excel_match_add_category()