#!/home/mikepartain/GIT/python/bin/python
import os, sys, pprint
from openpyxl import *
os.system('clear')

wb = load_workbook('workbook.xlsx')
ws_list = {}
def select_sheet():
    ws_check = 'False'
    ws_range=[]
    print 'Please select the worksheet you would like to work with:'
    for i in range(len(wb.get_sheet_names())):
        ws_count = i+1
        if ws_count not in ws_range:
            ws_range.append(ws_count)

    # This section enumerates the worksheets and assigns a number to each sheet
    # and displays a list of the sheets and the number.  At this point the user
    # can select the worksheet they are interested in.
    for (ws_num, ws) in zip(range(len(wb.get_sheet_names())), wb.get_sheet_names()):
        print ws_num+1, ws
        ws_list[ws_num+1] = ws

    selected_ws = raw_input('Select Sheet number: ')
    for wsnum, wsname in ws_list.items():
        if int(selected_ws) == wsnum:
            ws_check = 'True'
            get_rows_from_sheet(wsname)

    if ws_check == 'False':
        print 'Error %s, not a valid selection. Please try again.' % (selected_ws)
        select_sheet()
    
def get_rows_from_sheet(wsname):
    rows_data = []
    ws_range=[]
    ws=wb.get_sheet_by_name(wsname)
    print '%s has %s rows.' % (wsname,ws.max_row)
    for i in range(ws.max_row):
        i = i+1
        if i not in ws_range:
            ws_range.append(i)
    for column in ws.iter_cols(min_row=2, min_col = 1, max_col=4):
        print column[0].value, column[1].value, column[2].value
        #for cell in column:
            #print(cell.value)

'''

    #for row in ws.iter_rows(min_row=2, max_col=5, max_row=2):
    for row in ws.iter_rows(min_row=2, max_col=4):
        for cell in row:
            print cell.value,

'''




'''
    for row in ws.iter_rows():
        yield [cell.value for cell in row] 
    pprint(list(iter_rows(ws)))



    for index, row in enumerate(ws.iter_rows()):
        print row
        for cell in row:
            print(ws.cell(row=index + 1, column=1).value, cell.value)



    #    for (ws_num, ws) in zip(range(len(wb.get_sheet_names())), wb.get_sheet_names()):

    for row in ws.iter_rows():
        for column in row:
            print column.value

    for rows in ws.rows:
        for columns in rows:
            print columns.value,
            if columns.value not in rows_data:
                rows_data.append(columns.value)

    for host in rows_data:
        print host, 
'''



def get_row_from_sheet(wsname):
    row_data = []
    print 'Thank you for selecting %s.' % (wsname)
    ws=wb.get_sheet_by_name(wsname)
    #print ws.max_row 
    data = [ws.cell(row=9,column=i).value for i in range(1,9)]
    print data[0], data[1], data[2], data[3]
    for host_items in row_data:
        print host_items,


select_sheet()

