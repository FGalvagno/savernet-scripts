# TOPAS-to-CSV
A simple python script to convert TurnKey AIRQ32 databases to csv without having to export the data manually.

## Listing databases
The script only detects .DB files on the sample folder. This is done in order to prevent the use directly on the Series folder of AIRQ32, since the program generates a lot of empty databases that clutters the output of the script.

## TODO
- [ ] Cleanup output .csv names
- [ ] Add .csv naming scheme (date and time, TOPAS serial n°).
- [ ] Add a warning for the empty databases.
- [ ] Fix datetime format of the TimeStamp (to comply with UTC time format)
