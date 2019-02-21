# Author(s) Jeanette Gowen
# Date 08/10/2018
# Title ReportedBlaine
# Used to calculate Reported Blaine
# Code version 1.00
# Type (Python Custom Module)

import System
from System import *

def calcreportedBlaine(stdSpecificSurface,stdDensity, stdConstant, stdPorosity,stdTime, samplePorosity,\
                       sampleConstant, reportedSpG, time):
    reportedBlaine = None
    if stdSpecificSurface and stdDensity and stdConstant and stdPorosity and stdTime and samplePorosity and\
            sampleConstant and reportedSpG and time:
        stdDiff = stdConstant - stdPorosity
        sqrte3 = Math.Sqrt(Math.Pow(samplePorosity,3))
        numerator = stdSpecificSurface * stdDensity * stdDiff * sqrte3 * Math.Sqrt(time)
        sampleDiff = sampleConstant - samplePorosity
        sqrtes3 = Math.Sqrt(Math.Pow(stdPorosity,3))
        denominator = reportedSpG * (sampleDiff) * sqrtes3 * Math.Sqrt(stdTime)
        reportedBlaine = numerator/denominator
    return reportedBlaine
