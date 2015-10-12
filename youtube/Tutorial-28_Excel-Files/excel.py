def CreateExcelFile(cache,project1='Reference',project2='ToBeUpdated',export_number=0):
    import os
    from arki.utils import arkiexcel
    excel = arkiexcel.Excel()
    excel.AddSheet( 'TreeViewsFolders', True )
    excel.SetCellText(1, 1, project1)
    excel.SetCellText(1, 2, project2)
    if export_number == 3:
        excel.SetCellText(2, 1, "Folder v1.0")
        excel.SetCellText(2, 2, "Folder v2.0")
    elif export_number == 5:
        excel.SetCellText(2, 2, "Folder")
    excel.AddSheet( 'TreeViews', True )
    excel.SetCellText(1, 1, project1)
    excel.SetCellText(1, 2, project2)
    if export_number == 3:
        excel.SetCellText(2, 1, "View v1.0")
        excel.SetCellText(2, 2, "View v2.0")
    elif export_number == 5:
        excel.SetCellText(2, 2, "View")
    excel.AddSheet( 'Attributes', True )
    excel.SetCellText(1, 1, project1)
    excel.SetCellText(1, 2, project2)
    if export_number == 3:
        excel.SetCellText(2, 1, "Attribute v1.0")
        excel.SetCellText(2, 2, "Attribute v2.0")
    elif export_number == 5:
        excel.SetCellText(2, 2, "Attribute")
    excel.AddSheet( 'Rules', True )
    excel.SetCellText(1, 1, project1)
    excel.SetCellText(1, 2, project2)
    if export_number == 3:
        excel.SetCellText(2, 1, "Rule v1.0")
        excel.SetCellText(2, 2, "Rule v2.0")
    elif export_number == 5:
        excel.SetCellText(2, 2, "Rule")
    excel.SaveAs(os.path.join(cache,'UpdateExcelFile.xls'))
    excel.Close()

def RemoveFiles(cache):
    import os
    os.remove(os.path.join(cache, 'UpdateExcelFile.xls'))
os.remove(os.path.join(cache, 'Update.xml'))
def testTypeProperties():
	testProject.Create('Reference')
    cache = Export1()
    testProject.Delete()
    #Project to be updated
    testProject.Create('ToBeUpdated')
    Import1(cache)
testProject.Delete()
def testTreeviewProperties():
testProject.Create('Reference')
    cache = Export2()
    testProject.Delete()
    #Project to be updated
    testProject.Create('ToBeUpdated')
    Import2(cache)
    testProject.Delete()
