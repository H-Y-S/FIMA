# io methods for esrf data format (EDF) files 
import numpy as np

def read_edf_file(filename):
    hd = __read_edf_header(filename)
    dim1,dim2,datatype,endianness = __parse_header(hd)
    data = __read_edf_data(filename,len(hd),dim1,dim2,datatype,endianness)
    
    return data


# Reads the edf header. Length is multiple of 512,
# ends with }\n
# Returns the header as a string
def __read_edf_header(filename):
    hd = ''

    with open(filename,'rb') as f:
        hd = f.read(512)
        tmp = hd
        while not tmp[510:512] == '}\n':
            tmp = f.read(512)
            hd = hd + tmp

    return hd



def __read_edf_data(filename,headersize,dim1,dim2,datatype,endianness):
    if datatype == 'UnsignedLong':
        dt = np.dtype(endianness+'I')
    elif datatype == 'Float':
        dt = np.dtype(endianness+'f')

    with open(filename,'rb') as f:
        f.seek(headersize)
        data = np.fromfile(f,dt)

    data = np.reshape(data,(dim2,dim1))
        
    return data

        
# parse dimensions and datatype
def __parse_header(hd):
    vals = hd.split(';')
    dim1 = int([s for s in vals if 'Dim_1' in s][0].split('=')[1])
    dim2 = int([s for s in vals if 'Dim_2' in s][0].split('=')[1])
    datatype = [s for s in vals if 'DataType' in s][0].split('=')[1].strip()
    endianness = [s for s in vals if 'ByteOrder' in s][0].split('=')[1].strip()
    if endianness == 'LowByteFirst':
        endianness = '<'
    else:
        endianness = '>'
            
    return dim1,dim2,datatype,endianness
