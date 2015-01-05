# Airspy2Cfile

This project contains legacy Python 2 code and is primarily for archival or historical reference.

Airspy2Cfile is a command line tool to convert Airspy capture files to the GnuRadio complex file format.

This is useful when you are capturing IQ files using an embedded machine like an Odroid with `airspy_rx` tool and you want to process the files using GnuRadio.

**Note:** This script is written in **Python 2**.

## Dependencies

*   [GnuRadio](https://www.gnuradio.org/)

## Installation

To use this tool, you need to have GnuRadio installed. If you don't have it, you can find installation instructions on the [GnuRadio website](https://www.gnuradio.org/blog/installation-guide/).

## Usage

```bash
./Airspy2Cfile.py -r your_airspy_capture.iq -w gnuradio_output.cfile
```

### Options

| Flag | Argument | Description |
|---|---|---|
| `-h`, `--help` | | Show the help message and exit. |
| `-r` | `FILENAME_READ` | The filename of the Airspy IQ sample to process. |
| `-w` | `FILENAME_WRITE` | The filename of the GnuRadio complex file to create. |
| `-t` | `SAMPLE_TYPE` | Set the sample type. |

## Supported Formats

The tool aims to support the 4 Airspy sample formats:

*   `0`: `FLOAT32_IQ` (Note: `airspy_rx` with the `-t 0` option generates a GnuRadio complex file directly)
*   `1`: `FLOAT32_REAL`
*   `2`: `INT16_IQ` (default)
*   `3`: `INT16_REAL`
*   `4`: `U16_REAL`

**Currently, only `INT16_IQ` is supported.**

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

Copyright (C) 2015 Luis Colunga (@sinnet3000). All rights reserved.

See the LICENSE file for full details.
