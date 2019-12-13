{ 10011 } - EXIF Cleanser: "Who's a clever dick now?" 

    Thought it'd be neat to be able to strip EXIF data out of pictures at the command line 

    And snarky to replace a few select lines with "Who's a clever dick now?" for stalkers 

usage: EXIF_Dick [-h] [-v] [-s SNARK] [--verbose] file 

positional arguments: 

  file                  Filename(s) to process. 

optional arguments: 

  -h, --help            show this help message and exit 

  -v, --version         show program's version number and exit 

  -s SNARK, --snark SNARK 

                        snarky message to replace default. 

  --verbose             verbose progress output. 

 

    Compiled using: 
        (Note the -F flag was needed!) 
        From the terminal within PyCharm 
        pyinstaller -F EXIF_Dick.py
