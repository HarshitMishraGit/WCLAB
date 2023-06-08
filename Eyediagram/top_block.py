#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun  8 14:31:59 2023
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from harshit_plot_b1 import harshit_plot_b1  # grc-generated hier_block
from optparse import OptionParser
import numpy


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.numpoints = numpoints = 500
        self.cutoff = cutoff = 10000

        ##################################################
        # Blocks
        ##################################################
        self._cutoff_range = Range(10000, 50000, 1000, 10000, 200)
        self._cutoff_win = RangeWidget(self._cutoff_range, self.set_cutoff, "cutoff", "counter_slider", float)
        self.top_layout.addWidget(self._cutoff_win)
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, cutoff, 100, firdes.WIN_HAMMING, 6.76))
        self.harshit_plot_b1_1 = harshit_plot_b1()
        self.top_layout.addWidget(self.harshit_plot_b1_1)
        self.harshit_plot_b1_0 = harshit_plot_b1()
        self.top_layout.addWidget(self.harshit_plot_b1_0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bf((-1,1), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, numpoints)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.harshit_plot_b1_1, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.harshit_plot_b1_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, 100, firdes.WIN_HAMMING, 6.76))

    def get_numpoints(self):
        return self.numpoints

    def set_numpoints(self, numpoints):
        self.numpoints = numpoints

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, 100, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
