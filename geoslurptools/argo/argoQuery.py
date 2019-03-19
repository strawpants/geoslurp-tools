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
from sqlalchemy import text
# from geoslurptools.aux.ogrgeom import lonlat2ogr
from sqlalchemy import select,func,asc,and_,literal_column

def argoQuery(dbcon,polyWKT,tspan=None):
    tbl=dbcon.getTable('argo','oceanobs')
    qry=select([tbl.c.uri, tbl.c.profnr,tbl.c.tprofile,literal_column('geom::geometry').label('geom')])
    
    if tspan:
        qry=qry.where(and_(tbl.c.tprofile > tspan[0],tbl.c.tprofile < tspan[1]))
    

    qry=qry.where(func.ST_within(literal_column('geom::geometry'),func.ST_GeomFromText(polyWKT,4326)))

    qry=qry.order_by(asc(tbl.c.tprofile))

    return dbcon.dbeng.execute(qry)

def queryMonthlyArgo(dbcon, polyWKT, tstart, tend):
    """Query the database for lists of monthly Argo profiles within a certain polygon and time span"""
    
    # ogrpoly = lonlat2ogr(polygon)
    # import pdb;pdb.set_trace()
    out = {}
    qry = text(
        "SELECT uri,profnr,extract(year from tprofile) as year,extract(month from tprofile) as month, ST_X(geom::geometry) as lon,ST_Y(geom::geometry) as lat from oceanobs.argo where tprofile > '%s' and tprofile < '%s' and ST_within(geom::geometry,ST_GeomFromText('%s',4326)) ORDER BY tprofile ASC;" % (
        tstart, tend, polyWKT))

    # gather results in monthly batches
    for uri, iprof, year, month, lon, lat in dbcon.dbeng.execute(qry):
        epoch = (int(year), int(month))
        tmpdict = {"uri": uri, "iprof": int(iprof), "lonlat": (lon, lat)}
        if not epoch in out:
            out[epoch] = [tmpdict]
        else:
            out[epoch].append(tmpdict)

    return out
