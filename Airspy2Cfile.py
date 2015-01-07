#!/usr/bin/env python
##################################################
# Airspy2Cfile.py
# Airspy2CFile is a command line tool to convert Airspy_RX capture files to GnuRadio compatible CFile format. 
# This is very useful for example when you are capturing IQ files using an embedded machine like an Odroid with Airspy-RX tool and you want to
# process the files using GnuRadio.
# The tool aim is to support the 4 Airspy sample formats: (FLOAT32_IQ option generates a GnuRadio Cfile in Airspy_RX)
# 1=FLOAT32_REAL, 2=INT16_IQ(default), 3=INT16_REAL, 4=U16_REAL
# Currently INT16_IQ is supported which is default in Airspy_RX.
# Author: Luis Colunga (sinnet3000)
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
class Airspy2Cfile(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self)

        usage = "usage: %prog [options]"
        parser = OptionParser(option_class=eng_option, usage=usage)
        parser.add_option("-r", "", type="string", dest="filename_read",  help="Filename of Airspy_RX IQ sample to process")
        parser.add_option("-w", "", type="string", dest="filename_write", help="Filename of GnuRadio CFile to create")
        parser.add_option("-t", "", type="int", dest="sample_type", help="Set sample type/n 0=FLOAT32_IQ, 1=FLOAT32_REAL, 2=INT16_IQ(default), 3=INT16_REAL, 4=U16_REAL", default=2)
    
        (options, args) = parser.parse_args()

        if len(args) != 0:
            parser.print_help()
            exit(-1)

        if options.filename_read is None:
            print "Missing filename to read\n"
            parser.print_help()
            exit(-1)

        if options.filename_write is None:
            print "Missing filename to write\n"
            parser.print_help()
            exit(-1)


        self.filename_read = options.filename_read
        self.filename_write = options.filename_write
        self.sample_type = options.sample_type

        ##################################################
        # Blocks
        ##################################################
        self.blocks_short_to_float_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((.008, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((.008, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_short*1, self.filename_read, False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, self.filename_write, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_short*1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_short_to_float_0, 0))    
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_short_to_float_1, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_deinterleave_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_short_to_float_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))    



if __name__ == '__main__':
    tb = Airspy2Cfile()
    
try:
    tb.run()

except [[KeyboardInterrupt]]:
    pass
