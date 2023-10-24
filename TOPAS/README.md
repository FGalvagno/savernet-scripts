# TOPAS-to-CSV
Two simple python scripts to convert TurnKey AIRQ32 databases to csv without having to export the data manually.

## pxtocsv
This script is used for simple one to one file conversion. It only detects .DB files on the *sample* folder. This is done in order to prevent the use directly on the *Series* folder of AIRQ32, since the program generates a lot of empty databases that clutters the output of the script.

## bulk-pxtocsv
Makes a conversion of all the data from the *Series* folder into monthly files and yearly folders. **Warning:** when working with large amounts of data the script can take some time to complete the parsing of al DB files.

## TODO
- [x] Cleanup output .csv names
- [ ] Add .csv naming scheme (date and time, TOPAS serial n°). (necessary?)
- [x] Add a warning for the empty databases.
- [x] Fix datetime format of the TimeStamp (to comply with UTC time format)
