# Copy database registries to backup / analytics tables
#!/usr/bin/python3
import pypyodbc
import BagTMDBBAGMSGS
import BagTMDBPAXMSGS
import BagTMDBBAGINTEG
import BagTMDBH2H
import BagTMDBFLTINFO
import BagTMDBPTMH2H

from datetime import datetime

year = str(datetime.now().year)
day = str(datetime.now().day-2)
print ("Year: ", year, "Day: ", day)
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=ICEREKAS296\sqlexpress;'
                              'Database=outsystems;'
                              'uid=osadmin;pwd=adminoutsystems', autocommit=False)

maxFLTINFOSTD = day

#Create BAGMSGS table
cursor = connection.cursor() 
queryStmt = "SELECT count(1) FROM OSUSR_UUK_BAGMSGS" + year
print ("BAGMSGS - Query Stmt: "+queryStmt)
try:
    cursor.execute(queryStmt)
    results = cursor.fetchone()
except:
    createStmt = BagTMDBBAGMSGS.BAGMSGS(year)
    cursor.execute(createStmt)

#Create PAXMSGS table
cursor = connection.cursor() 
queryStmt = "SELECT count(1) FROM OSUSR_UUK_PAXMSGS" + year
print ("PAXMSGS - Query Stmt: "+queryStmt)
try:
    cursor.execute(queryStmt)
    results = cursor.fetchone()
except:
    createStmt = BagTMDBPAXMSGS.PAXMSGS(year)
    cursor.execute(createStmt)

#Create BAGINTEG table
cursor = connection.cursor() 
queryStmt = "SELECT count(1) FROM OSUSR_UUK_BAGINTEG" + year
print ("BAGINTEG - Query Stmt: "+queryStmt)
try:
    cursor.execute(queryStmt)
    results = cursor.fetchone()
except:
    createStmt = BagTMDBBAGINTEG.BAGINTEG(year)
    cursor.execute(createStmt)

#Create FLTINFO table
cursor = connection.cursor() 
queryStmt = "SELECT MAX(STD) FROM OSUSR_UUK_FLT_INFO" + year
print ("FLT-INFO - Query Stmt: "+queryStmt)
try:
    cursor.execute(queryStmt)
    results = cursor.fetchone()
    maxFLTINFOSTD = str(results[0].day)
except:
    createStmt = BagTMDBFLTINFO.FLTINFO(year)
    cursor.execute(createStmt)

#Create H2H table
cursor = connection.cursor() 
queryStmt = "SELECT count(1) FROM OSUSR_UUK_H2H" + year
print ("H2H - Query Stmt: "+queryStmt)
try:
    cursor.execute(queryStmt)
    results = cursor.fetchone()
except:
    createStmt = BagTMDBH2H.H2H(year)
    cursor.execute(createStmt)

#Create PTM_H2H table
cursor = connection.cursor() 
queryStmt = "SELECT count(1) FROM OSUSR_UUK_PTM_H2H" + year
print ("PTM-H2H - Query Stmt: "+queryStmt)
try:
    cursor.execute(queryStmt)
    results = cursor.fetchone()
except:
    createStmt = BagTMDBPTMH2H.PTMH2H(year)
    cursor.execute(createStmt)

cursor.commit()

#Copy BAGMSGS registers
copyStmt = "INSERT INTO OSUSR_UUK_BAGMSGS" + year + " SELECT * FROM OSUSR_UUK_BAGMSGS WHERE year(TIMESTAMP) = "+ year + " AND datepart(dd, TIMESTAMP) < " + day
print ("BAGMSGS - Copy Stmt: "+copyStmt)
try:
    cursor.execute(copyStmt)
    cursor.commit()
except ValueError:
    print ("Ex: ", ValueError)
    cursor.rollback()
    exit

#Copy PAXMSGS registers
copyStmt = "INSERT INTO OSUSR_UUK_PAXMSGS" + year + " SELECT * FROM OSUSR_UUK_PAXMSGS WHERE year(TIMESTAMP) = "+ year + " AND datepart(dd, TIMESTAMP) < " + day
print ("PAXMSGS - Copy Stmt: "+copyStmt)
try:
    cursor.execute(copyStmt)
    cursor.commit()
except ValueError:
    print ("Ex: ", ValueError)
    cursor.rollback()
    exit

#Copy BAGINTEG registers
copyStmt = "INSERT INTO OSUSR_UUK_BAGINTEG" + year + " SELECT * FROM OSUSR_UUK_BAGINTEG WHERE year(TIMESTAMP) = "+ year + " AND datepart(dd, TIMESTAMP) < " + day
print ("BAGINTEG - Copy Stmt: "+copyStmt)
try:
    cursor.execute(copyStmt)
    cursor.commit()
except ValueError:
    print ("Ex: ", ValueError)
    cursor.rollback()
    exit

#Copy FLT_INFO registers
copyStmt = "INSERT INTO OSUSR_UUK_FLT_INFO" + year + " SELECT * FROM OSUSR_UUK_FLT_INFO WHERE year(STD) = "+ year + " AND datepart(dd, STD) BETWEEN " + maxFLTINFOSTD + " AND " + day 
print ("FLT-INFO - Copy Stmt: "+copyStmt)
#try:
#    cursor.execute(copyStmt)
#    cursor.commit()
#except ValueError:
#    print ("Ex: ", ValueError)
#    cursor.rollback()
#    exit

#Copy H2H registers
copyStmt = "INSERT INTO OSUSR_UUK_H2H" + year + " SELECT * FROM OSUSR_UUK_H2H WHERE year(ODATE) = "+ year + " AND datepart(dd, ODATE) < " + day
print ("H2H - Copy Stmt: "+copyStmt)
try:
    cursor.execute(copyStmt)
    cursor.commit()
except ValueError:
    print ("Ex: ", ValueError)
    cursor.rollback()
    exit

#Copy PTM_H2H registers
copyStmt = "INSERT INTO OSUSR_UUK_PTM_H2H" + year + " SELECT * FROM OSUSR_UUK_PTM_H2H WHERE year(ODATE) = "+ year + " AND datepart(dd, ODATE) < " + day
print ("PTM-H2H - Copy Stmt: "+copyStmt)
try:
    cursor.execute(copyStmt)
    cursor.commit()
except ValueError:
    print ("Ex: ", ValueError)
    cursor.rollback()
    exit

#Delete H2H registers
deleteStmt = "DELETE FROM OSUSR_UUK_H2H WHERE year(ODATE) = "+ year + " AND datepart(dd, ODATE) < " + day
print ("H2H - Delete Stmt: "+deleteStmt)
try:
    cursor.execute(deleteStmt)
    cursor.commit()
except:
    cursor.rollback()
    exit

#Delete PTM_H2H registers
deleteStmt = "DELETE FROM OSUSR_UUK_PTM_H2H WHERE year(ODATE) = "+ year + " AND datepart(dd, ODATE) < " + day
print ("PTM-H2H - Delete Stmt: "+deleteStmt)
try:
    cursor.execute(deleteStmt)
    cursor.commit()
except:
    cursor.rollback()
    exit

#Delete BAGINTEG registers
deleteStmt = "DELETE FROM OSUSR_UUK_BAGINTEG WHERE year(TIMESTAMP) = "+ year + " AND datepart(dd, TIMESTAMP) < " + day
print ("BAGINTEG - Delete Stmt: "+deleteStmt)
try:
    cursor.execute(deleteStmt)
    cursor.commit()
except:
    cursor.rollback()
    exit

#Delete PAXMSGS registers
deleteStmt = "DELETE FROM OSUSR_UUK_PAXMSGS WHERE year(TIMESTAMP) = "+ year + " AND datepart(dd, TIMESTAMP) < " + day
print ("PAXMSGS - Delete Stmt: "+deleteStmt)
try:
    cursor.execute(deleteStmt)
    cursor.commit()
except:
    cursor.rollback()
    exit

#Delete BAGMSGS registers
deleteStmt = "DELETE FROM OSUSR_UUK_BAGMSGS WHERE year(TIMESTAMP) = "+ year + " AND datepart(dd, TIMESTAMP) < " + day
print ("BAGMSGS - Delete Stmt: "+deleteStmt)
try:
    cursor.execute(deleteStmt)
    cursor.commit()
except:
    cursor.rollback()
    exit

#Delete FLT_INFO registers
deleteStmt = "DELETE FROM OSUSR_UUK_FLT_INFO WHERE year(STD) = "+ year + " AND datepart(dd, STD) < " + day
print ("FLT-INFO - Delete Stmt: "+deleteStmt)
#try:
#    cursor.execute(deleteStmt)
#    cursor.commit()
#except:
#    cursor.rollback()
#    exit

reorganizeStmt = """ALTER INDEX OSPRK_OSUSR_UUK_BAGMSGS ON OSUSR_UUK_BAGMSGS REORGANIZE;
ALTER INDEX OSPRK_OSUSR_UUK_BAGINTEG ON OSUSR_UUK_BAGINTEG REORGANIZE;
ALTER INDEX OSPRK_OSUSR_UUK_H2H ON OSUSR_UUK_H2H REORGANIZE;
ALTER INDEX OSIDX_OSUSR_UUK_H2H_10IFLTINFOID ON OSUSR_UUK_H2H REORGANIZE;
ALTER INDEX OSIDX_OSUSR_UUK_H2H_10OFLTINFOID ON OSUSR_UUK_H2H REORGANIZE;
ALTER INDEX OSPRK_OSUSR_UUK_PAXMSGS ON OSUSR_UUK_PAXMSGS REORGANIZE;
ALTER INDEX OSPRK_OSUSR_UUK_PTM_H2H ON OSUSR_UUK_PTM_H2H REORGANIZE;
ALTER INDEX OSIDX_OSUSR_UUK_PTM_H2H_10IFLTINFOID ON OSUSR_UUK_PTM_H2H REORGANIZE;
ALTER INDEX OSIDX_OSUSR_UUK_PTM_H2H_10OFLTINFOID ON OSUSR_UUK_PTM_H2H REORGANIZE;"""
print ("Reorganize Stmt: "+reorganizeStmt)
try:
    cursor.execute(reorganizeStmt)
    cursor.commit()
except:
    cursor.rollback()
    exit

connection.close()
exit