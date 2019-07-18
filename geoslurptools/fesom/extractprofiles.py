from netCDF4 import Dataset
def getprofiles(ncfile,var,tspan,surfaceids):
    """Generator which extracts profiles for a certain variable from a fesom netcdf file"""
    with Dataset(ncfile,'r') as nc:
        # extract valid time nodes
        nc["time"]
        #loop over time
        
        #loop over nodes
