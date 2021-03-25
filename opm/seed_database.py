import shelve 
import _gdbm 

def gdbm_shelve(filename, flag="c"): 
    return shelve.Shelf(_gdbm.open(filename, flag)) 

from input.read_document import Sample
document = 'util/12thGrade-informationExplanatory.txt'

report = Sample(document)
db = gdbm_shelve('shelve.db')

db['example'] = report

db.close()
