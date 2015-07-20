import os
import re
import glob
from contextlib import contextmanager

from EDFIO import edfio


# Fluorescence imaging dataset
# The data is stored in numpy ndarray (3-dimensional)
# each detector, projection angle, and timestep is stored
# as a separate 3d array into a dictionary, indexed by a tuple of
# [det #, proj #, timestep #]
class FluoDataset:
    def __init__(self):
        mDataDictionary = {}
        pass

    # reads all files corresponding to the given
    # filename (all xia## files, all lines, all projections)
    def populate_dataset(filename):        
        p,filename = os.path.split(filename)
        basename,ext = os.path.splitext(filename)

        # test which xia## files exist
        xiapattern = re.sub(r'(xia.._)',r'xia??_',filename)
        with working_diretory(p):
            tmp = glob.glob(xiapattern)

        xialist = []
        for l in tmp:
            g = re.search('(?<=_)xia..(?=_)',l)
            xialist.append(g.group(0))
            
        # test which scan lines exist
        linepattern = basename[0:-4] + "????" + ext
        with working_diretory(p):
            tmp = glob.glob(linepattern)

        linelist = []
        for l in tmp:
            linelist.append(int(l[-8:-4]))
    
        linelist.sort()
        xialist.sort()

        # Test which projections exist
        pass
                
        # Then load the files
        with working_directory(p):
            for x in xialist:
                files = glob.glob('*'_+x+"_*_????"+ext)

                data_list = []
                for f in files:
                # Read the first file to determine dimensions and data type
                    a = edfio.read_edf_file(f)
                    data_list.append(a)

                data_tuple = tuple(a)
                data_array = np.dstack(data_tuple)


                mDataDictionary[(x,0,0)] = data_array
                                                    

    def get_fluo_data(self,detno,projno,timestepno):
        pass

    def get_det_count(self):
        pass

    def get_proj_count(self):
        pass


    def get_timestep_count(self):
        pass



        
@contextmanager
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_dir)
