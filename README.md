# optimize-gain

**CONTRIBUTORS:** </br>
In chronological order: </br>
(1) Apr 26, 2016 - **BartJr :** Original Author, for use on dump1090-mutability / Python 2 </br>
(2) Apr 28, 2016 - **Lignumaqua:** Enhancement for use on dump1090-mutability / Python 2 </br>
(3) Aug 21, 2016 - **abcd567:** Adaptation for use on Piaware image / Python 2 </br>
(4) Oct 08, 2016 - **abcd567:** Adaptation for use on dump1090-fa / Python 2 on Raspbian </br>
(5) Dec 15, 2016 - **wittrup58:** Variant for use on Piaware image / Python 2 </br>
(6) Dec 19, 2021 - **abcd567:** Update/Upgrade for use on dump1090-fa ver 6.1 / **Python 3** / RaspiOS Bullseye </br>

## USAGE
</br>

```
wget https://raw.githubusercontent.com/abcd567a/optimize-gain/main/optimize-gain-dump1090-fa.py  
sudo chmod +x optimize-gain-dump1090-fa.py   
sudo ./optimize-gain-dump1090-fa.py  
```

### The script will start collecting data (Messages, Positions, Aircraft) from dump1090-fa port 30003, accumulated for 1 minute for each gain setting, and plot it like this:
</br>
READING AND SAVING SETTINGS BEFORE STARTING THE TEST </br>
THESE SETTINGS WILL BE RESTORRED AT THE END OF THE TEST </br>
</br>
RECEIVER_GAIN=60 </br>
ADAPTIVE_DYNAMIC_RANGE=yes </br>
 </br>
test 1 of 3 </br>
gain= 49.6 messages= 15355 positions= 2246 planes= 64 </br>
gain= 48.0 messages= 14567 positions= 2134 planes= 66 </br>
.... .... </br>
.... .... </br>
gain= 22.9 messages= 12550 positions= 1761 planes= 50 </br>
gain= 20.7 messages= 11623 positions= 1493 planes= 42 </br>
 </br>
test 2 of 3 </br>
gain= 49.6 messages= 14568 positions= 2303 planes= 75 </br>
gain= 48.0 messages= 16294 positions= 2527 planes= 83 </br>
.... .... </br>
.... .... </br>
gain= 22.9 messages= 6526 positions= 970 planes= 36 </br>
gain= 20.7 messages= 4939 positions= 716 planes= 29 </br>
 </br>
test 3 of 3 </br>
gain= 49.6 messages= 13931 positions= 2069 planes= 70 </br>
gain= 48.0 messages= 14354 positions= 2206 planes= 68 </br>
.... .... </br>
.... .... </br>
gain= 22.9 messages= 8225 positions= 1221 planes= 38 </br>
gain= 20.7 messages= 4584 positions= 744 planes= 31 </br>
 </br>
===Totals=== </br>
Gain, Messages, Positions, Aircraft </br>
49.6 62144 9687 223 </br>
48.0 62857 9809 225 </br>
44.5 59248 9281 233 </br>
43.9 57458 9058 221 </br>
43.4 58986 9212 227 </br>
42.1 61277 9380 234 </br>
40.2 61272 9640 223 </br>
38.6 60738 9487 217 </br>
37.2 61570 9359 213 </br>
36.4 59260 9004 210 </br>
33.8 60864 8987 214 </br>
32.8 59858 8921 212 </br>
29.7 57424 8505 199 </br>
28.0 55515 8273 187 </br>
25.4 51750 7437 169 </br>
22.9 46061 6549 158 </br>
20.7 37763 5143 131 </br>
 </br>
SETTINGS RESTORED AT END OF TEST: </br>
RECEIVER_GAIN=60 </br>
ADAPTIVE_DYNAMIC_RANGE=yes </br>



