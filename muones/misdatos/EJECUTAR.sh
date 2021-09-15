gzip -d unweighted_events.lhe.gz 
cat unweighted_events.lhe | grep "13  " > datos_raw.csv
python3 datos.py
python3 juntarmumu.py
