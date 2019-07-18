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
# License along with geoslurp; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# Author Roelof Rietbroek (roelof@geod.uni-bonn.de), 2019
from sqlalchemy import select,func,asc,and_,literal_column

def gravitystaticQuery(dbcon, gravitytable, ):
    """queries the geoslurp database for  static gravity datasets"""
            
    #retrieve/reflect the table
    tbl=dbcon.getTable('icgem_static','gravity')
    qry=select([tbl])
    qry=qry.where(tbl.c.data["name"].astext == gravitytable)
    # print(qry)
    return dbcon.dbeng.execute(qry)

