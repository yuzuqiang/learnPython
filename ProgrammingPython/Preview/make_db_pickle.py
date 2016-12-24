#from initdata import db
import initdata
import pickle
dbfile = open('people-pickle', 'wb')
#pickle.dump(db, dbfile)
pickle.dump(initdata.db,dbfile)
dbfile.close()
