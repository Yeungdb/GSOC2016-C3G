#!/usr/bin/python

import subprocess

def loadDelly(inputBam, outputFile):
    subprocess.call("delly2 -i {inputBam} -o {outputFile}".format(inputBam=inputBam, outputFile=outputFile))


