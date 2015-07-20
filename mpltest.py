import pygtk
pygtk.require('2.0')
import gtk
import gobject

from numpy import arange, sin, pi

# imports needed for matplotlib to embed in gtk
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas



class MPLTest:
    def __init__(self):
        # Minimal gtk initialization
        self.builder = gtk.Builder()
        self.builder.add_from_file("mpltest.glade")
        self.builder.connect_signals(self)

        # Create a matplotlib figure with a plot        
        self.figure = Figure(figsize=(5,4), dpi=100)
        self.a = self.figure.add_subplot(111)
        f,y = self.gen_1dist()
        self.a.plot(f,y)

        # Place the matplotlib figure into a container
        self.canvas = FigureCanvas(self.figure)  # a gtk.DrawingArea
        self.builder.get_object('viewport1').add(self.canvas)



        
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


    def gen_1dist(self):
        f = arange(0.0,3.0,0.01)
        y = sin(2*pi*f*f)
        return f,y

    def gen_2dist(self):
        f = arange(0.0,3.0,0.01)
        y = sin(2*pi*f*f) + sin(1.1*2*pi*f*f)
        return f,y

    def singleDistanceClicked(self, widget, data = None):
        print 'single distance clicked'
        f,y = self.gen_1dist()
        self.a.clear()
        self.a.plot(f,y)
        self.canvas.draw()
                
    def twoDistanceClicked(self, widget, data = None):
        print 'two distance clicked'
        f,y = self.gen_2dist()
        self.a.clear()
        self.a.plot(f,y)
        self.canvas.draw()

        
    def run(self):
        self.builder.get_object("window1").show_all()
        gtk.main()
        
if __name__ == "__main__":
    mpltest = MPLTest()
    mpltest.run()
            





    
                            
