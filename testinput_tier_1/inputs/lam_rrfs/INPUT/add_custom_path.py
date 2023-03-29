import netCDF4

# Add a gridfiles_path to the file
nc = netCDF4.Dataset('C403_mosaic.halo3.nc', 'r+', format='NETCDF4')
v = nc.createVariable('gridfiles_path', 'S1', ('ntiles','string'))
v._Encoding = 'ascii'
v[:]='Data/inputs/lam_rrfs'
nc.close()
