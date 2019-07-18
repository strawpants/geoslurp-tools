# This file is part of geoslurp-tools.
# geoslurp-tools is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.

# geoslurp-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with geoslurp-tools; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# Author Roelof Rietbroek (roelof@geod.uni-bonn.de), 2019

from sqlalchemy import create_engine, MetaData, Table,select,and_
from sqlalchemy.orm import sessionmaker
import getpass 
import keyring


class geoslurpConnection:
    def __init__(self,user,host,usekeyring=True,verbose=False):
        """Initiate a database connection to a geoslurp database"""
        password=None

        if usekeyring:
            #try to retrieve the password using python keyring
            password=keyring.get_password("geoslurp",user)
        
        if not password:
            password=getpass.getpass(prompt='Please enter geoslurp password for user %s: '%(user))
            
            if usekeyring:
                #Also store in the keyring for later reuse
                keyring.set_password("geoslurp",user,password)

        #compose the url to connecto to 
        dburl="postgresql+psycopg2://"+user+":"+password+"@"+host+"/geoslurp"
        #initiate a connection
        self.dbeng = create_engine(dburl, echo=verbose)
        # self.Session = sessionmaker(bind=self.dbeng)
    
    def getTable(self,tname,scheme):
        mdata=MetaData(bind=self.dbeng,schema=scheme)
        return Table(tname, mdata, autoload=True, autoload_with=self.dbeng)

    def getInvent(self,tname,scheme):
        mdata=MetaData(bind=self.dbeng,schema='admin')
        tbl=Table('inventory', mdata, autoload=True, autoload_with=self.dbeng)
        qry=select([tbl]).where(and_((tbl.c.scheme == scheme) & (tbl.c.dataset == tname)))
        return self.dbeng.execute(qry).first()




