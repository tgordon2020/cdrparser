# cdrparser
Cleans up Cisco UCM CDR export.

Simple script to clean up cisco UCM CDR export.  Rename cdr export to cdr.csv.  Run script from same directory as cdr file.  Script generates a new csv file call cdrupdated.csv.  This file contains only 4 columns.  Date/Time, Calling Party, Called Party, and Duration.  Date time is converted from EPOCH time to GMT.
