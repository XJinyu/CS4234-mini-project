INPUT:
columns(1-11):
"FL_DATE","FL_NUM","ORIGIN_AIRPORT_ID","DEST_AIRPORT_ID","CRS_DEP_TIME","DEP_TIME","DEP_DELAY","CRS_ARR_TIME","ARR_TIME","ARR_DELAY","CANCELLED",

File names MUST be formatted as: yyyy-mm.csv
(for processing)

First row (columns) of downloaded file should be deleted

OUTPUT:
file name: day-airportid.csv
colums(1-4):
"fl_num","departure(0)/arrival(1)","crs_time","real_time","delay"
