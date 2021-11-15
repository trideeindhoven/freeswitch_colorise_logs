# freeswitch_colorise_logs
Extremely simple script to colorise the freeswitch.log for easy analysis

The script uses line-by-line regular expressions to color complete lines. This is the same effect as fs_cli does, but then on an already existing logfile.

## Usage
./colorise_logfile.py \<options\>  
Options:  
-h            Print this message  
-f [--file]   freeswitch log full file path  

E.g.:
```$ ./colorise_logfile.py -f /var/log/freeswitch/freeswitch.log```
