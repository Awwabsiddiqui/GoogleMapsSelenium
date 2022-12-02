from openpyxl import load_workbook


def append2XLSX(row_data):
    wb = load_workbook("output/output.xlsx")
    ws = wb.worksheets[0]
    ws.append(row_data)
    wb.save("output/output.xlsx")


def dict2List(dictionary):
    oplist = [dictionary.get("City", "NoCity"), dictionary.get("SearchKeywords", "NoSearchKeywords"),
              dictionary.get("BusinessName", "NoBusinessName"), dictionary.get("TagLine", "NoTagLine"),
              dictionary.get("Address", "NoAddress"), dictionary.get("URL", "NoURL"),
              dictionary.get("Phone", "NoPhone"),
              dictionary.get("bucketURL", "NoBucketURL"), dictionary.get("Longitude", "NoLongitude"),
              dictionary.get("Latitude", "NoLatitude"), dictionary.get("MapURL", "NoMapURL")]
    # print(oplist)
    append2XLSX(oplist)
