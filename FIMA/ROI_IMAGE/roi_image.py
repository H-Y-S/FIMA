import pygtk
pygtk.require('2.0')
import gtk
import gobject
import os.path
import re
import glob

#from numpy import arange, sin, pi

# imports needed for matplotlib to embed in gtk
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas



class ROIImage:
    def __init__(self):
        # Minimal gtk initialization
        self.builder = gtk.Builder()
        self.builder.add_from_file("roi_image.glade")
        self.builder.connect_signals(self)

        # Create a matplotlib figure for the image        
        self.imageFigure = Figure(figsize=(5,4), dpi=100)
        self.a = self.imageFigure.add_subplot(111)

        # Place the matplotlib figures into a container
        self.imageCanvas = FigureCanvas(self.imageFigure)  # a gtk.DrawingArea
        self.builder.get_object('imageViewPort').add(self.imageCanvas)

        # Create a matplotlib figure for the plot       
        self.plotFigure = Figure(figsize=(5,4), dpi=100)
        self.a = self.plotFigure.add_subplot(111)

        # Place the matplotlib figures into a container
        self.plotCanvas = FigureCanvas(self.plotFigure)  # a gtk.DrawingArea
        self.builder.get_object('plotViewPort').add(self.plotCanvas)

                
    # This one is called when the main window is destroyed (i.e. when  
    # delete_event returns null)
    def on_main_window_destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()


    # This one is called when the main window close-button is clicked
    def on_main_window_delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False


    def openDataButtonClicked(self,widget,data = None):
        # Open file chooser to choose a single file
        1
        chooser = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
            buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK)) 
        resp = chooser.run()
        if resp == gtk.RESPONSE_OK:
            filename = chooser.get_filename()
            print "selected file: " + filename

            # parse the filename
            self.list_matching_files(filename)
            # read all the files (including xiast files)
                                    
            # display the new data
        elif resp == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
			
        chooser.destroy()

                

    # This lists matching xia-files from ID22NI style data layout.
    # there can be xia## for different detectors and xiast for stats
    def list_matching_files(self,filename):
        p,filename = os.path.split(filename)
        basename,ext = os.path.splitext(filename)

        # test which xia## files exist
        xiapattern = re.sub(r'(xia.._)',r'xia??_',filename)
        xialist = glob.glob(xiapattern)

        
        # Then load the files
        


        
    
#    def singleDistanceClicked(self, widget, data = None):
#        print 'single distance clicked'
#        f,y = self.gen_1dist()
#        self.a.clear()
#        self.a.plot(f,y)
#        self.canvas.draw()
                
#    def twoDistanceClicked(self, widget, data = None):
#        print 'two distance clicked'
#        f,y = self.gen_2dist()
#        self.a.clear()
#        self.a.plot(f,y)
#        self.canvas.draw()

        
    def run(self):
        self.builder.get_object("window1").show_all()
        gtk.main()
        
if __name__ == "__main__":
    roiimage = ROIImage()
    roiimage.run()
            





    
                            
