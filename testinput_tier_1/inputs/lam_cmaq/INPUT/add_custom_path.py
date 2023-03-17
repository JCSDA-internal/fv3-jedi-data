import netCDF4

# Add a gridfiles_path to the file
nc = netCDF4.Dataset('grid_spec.nc', 'r+', format='NETCDF4')
v = nc.createVariable('gridfiles_path', 'S1', ('ntiles','string'))
v._Encoding = 'ascii'
v[:]='Data/inputs/lam_cmaq'
nc.close()
