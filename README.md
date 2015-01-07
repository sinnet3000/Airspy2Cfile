# Airspy2CFile

Airspy2CFile is a command line tool to convert Airspy_RX capture files to GnuRadio compatible CFile format. 

This is very useful for example when you are capturing IQ files using an embedded machine like an Odroid with Airspy-RX tool and you want to
process the files using GnuRadio.

The tool aim is to support the 4 Airspy sample formats: (FLOAT32_IQ option generates a GnuRadio Cfile in Airspy_RX)

1=FLOAT32_REAL, 2=INT16_IQ(default), 3=INT16_REAL, 4=U16_REAL

Currently INT16_IQ is supported.

## Usage: Airspy2Cfile.py [options]

### Options:
  -h, --help         show this help message and exit<br>
  -r FILENAME_READ   Filename of Airspy_RX IQ sample to process<br>
  -w FILENAME_WRITE  Filename of GnuRadio CFile to create<br>
  -t SAMPLE_TYPE     Set sample type/n 0=FLOAT32_IQ, 1=FLOAT32_REAL,<br>
                     2=INT16_IQ(default), 3=INT16_REAL, 4=U16_REAL<br>

