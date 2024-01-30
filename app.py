import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# Authorize editing via Google API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope) # type: ignore
gc = gspread.authorize(credentials) # type: ignore

# url worsheet
url_worksheet = "https://docs.google.com/spreadsheets/d/1H82dsamDTJp_I5jgYXVQBratIR-wknJOoWrxP_G9UIo/edit#gid=0"
worksheets1 = gc.open_by_url(url_worksheet).sheet1

# Get all values ​​from the table
data = worksheets1.get_all_values()
# Store all table values ​​in a DataFrame
pandasDF = pd.DataFrame(data)
# Delimit the table
student = pandasDF[3:30]

for i in range(0, 24):
    studentAbsences = int(student.iloc[i, 2]) # type: ignore
    absenceCollum = i + 4
    if studentAbsences > 15:
        worksheets1.update_cell(absenceCollum, 7, "Reprovado por falta")
        worksheets1.update_cell(absenceCollum, 8, "0")
    else:
        p1 = int(student.iloc[i, 3]) # type: ignore
        p2 = int(student.iloc[i, 4]) # type: ignore
        p3 = int(student.iloc[i, 5]) # type: ignore
        avgScore = round((p1 + p2 + p3) / 30)
        if avgScore >= 7:
            worksheets1.update_cell(absenceCollum, 7, "Aprovado")
            worksheets1.update_cell(absenceCollum, 8, "0")
        elif avgScore >= 5 or avgScore < 7:
            gradeFin = 10 - avgScore
            worksheets1.update_cell(absenceCollum, 7, "Exame Final")
            worksheets1.update_cell(absenceCollum, 8, gradeFin)
        else:
            worksheets1.update_cell(absenceCollum, 7, "Reprovado por nota")
            final_grade = round(avgScore) + 1  
            worksheets1.update_cell(absenceCollum, 8, final_grade)
