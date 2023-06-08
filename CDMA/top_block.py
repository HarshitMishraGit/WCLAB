#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun  8 15:03:35 2023
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


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
        self.samp_rate = samp_rate = 32000
        self.na = na = 0

        ##################################################
        # Blocks
        ##################################################
        self._na_range = Range(0, 10, 0.1, 0, 200)
        self._na_win = RangeWidget(self._na_range, self.set_na, "na", "counter_slider", float)
        self.top_layout.addWidget(self._na_win)
        self.qtgui_vector_sink_f_1 = qtgui.vector_sink_f(
            4,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "ch in",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_1.set_update_time(0.10)
        self.qtgui_vector_sink_f_1.set_y_axis(-10, 10)
        self.qtgui_vector_sink_f_1.enable_autoscale(False)
        self.qtgui_vector_sink_f_1.enable_grid(False)
        self.qtgui_vector_sink_f_1.set_x_axis_units("")
        self.qtgui_vector_sink_f_1.set_y_axis_units("")
        self.qtgui_vector_sink_f_1.set_ref_level(0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_1.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_1.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_1.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_1_win = sip.wrapinstance(self.qtgui_vector_sink_f_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_1_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            4,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "ch out",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-10, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("user 2")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -10)
            self.qtgui_number_sink_0_0.set_max(i, 10)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(10)
        self.qtgui_number_sink_0.set_title("user 1")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -10)
            self.qtgui_number_sink_0.set_max(i, 10)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.blocks_vector_to_streams_0_0 = blocks.vector_to_streams(gr.sizeof_float*1, 4)
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_float*1, 4)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, 4)
        self.blocks_stream_to_vector_1_0 = blocks.stream_to_vector(gr.sizeof_float*1, 4)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_float*1, 4)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, 4)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((0.25, ))
        self.blocks_multiply_const_vxx_0_0_2 = blocks.multiply_const_vff(((1,1,-1,1)))
        self.blocks_multiply_const_vxx_0_0_0_3 = blocks.multiply_const_vff(((-1,1,1,1)))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff(((-1,1,1,1)))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff(((1,1,-1,1)))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.25, ))
        self.blocks_add_xx_2 = blocks.add_vff(1)
        self.blocks_add_xx_1_1 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(4)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, na, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 6)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 2)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_stream_to_vector_1_0, 0))    
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_stream_to_vector_1, 0))    
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_2, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_vector_sink_f_1, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_add_xx_1_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_add_xx_2, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_3, 0), (self.blocks_vector_to_streams_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_2, 0), (self.blocks_vector_to_streams_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.qtgui_number_sink_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_multiply_const_vxx_0_0_0_3, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_multiply_const_vxx_0_0_2, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.qtgui_vector_sink_f_0, 0))    
        self.connect((self.blocks_stream_to_vector_1, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_1_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_add_xx_2, 0))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_add_xx_1, 1))    
        self.connect((self.blocks_vector_to_streams_0, 2), (self.blocks_add_xx_1, 2))    
        self.connect((self.blocks_vector_to_streams_0, 3), (self.blocks_add_xx_1, 3))    
        self.connect((self.blocks_vector_to_streams_0_0, 0), (self.blocks_add_xx_1_1, 0))    
        self.connect((self.blocks_vector_to_streams_0_0, 1), (self.blocks_add_xx_1_1, 1))    
        self.connect((self.blocks_vector_to_streams_0_0, 2), (self.blocks_add_xx_1_1, 2))    
        self.connect((self.blocks_vector_to_streams_0_0, 3), (self.blocks_add_xx_1_1, 3))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_na(self):
        return self.na

    def set_na(self, na):
        self.na = na
        self.analog_noise_source_x_0.set_amplitude(self.na)


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
