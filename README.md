# Subdomain Scanner
[![Python3.x](https://img.shields.io/badge/python-3.x-FADA5E.svg?logo=python)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/)
* This is simple script for scan subdomain of a website written Python 3
* I created and used this tool for educational purposes only.

## Installation
```
git clone https://github.com/CyberCommands/Subdomains.git
```
```
cd Subdomains/
```
```
pip install -r requirements.txt
```
```
python3 scanner.py --help
```
**Output**
```
usage: scanner.py [-h] [-l WORDLIST] [-t NUM_THREADS] [-o OUTPUT_FILE] domain

Subdomain Scanner using Threads

positional arguments:
  domain                Domain to scan for subdomains without protocol (e.g
                        without 'http://' or 'https://')

optional arguments:
  -h, --help            show this help message and exit
  -l WORDLIST, --wordlist WORDLIST
                        File that contains all subdomains to scan, line by
                        line. Default is subdomains.txt
  -t NUM_THREADS, --num-threads NUM_THREADS
                        Number of threads to use to scan the domain. Default
                        is 10
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Specify the output text file to write discovered
                        subdomains
```
For example to scan hackthissite.com for subdomains using only 10 threads with a word list of 100 subdomains (`subdomains.txt`):
```
python3 scanner.py hackthissite.com  -t 10
```
After a while, it **outputs:**
```
[+] Discovered subdomain -->  http://www.hackthissite.com
[+] Discovered subdomain -->  http://ns2.hackthissite.com
[+] Discovered subdomain -->  http://mail.hackthissite.com
[+] Discovered subdomain -->  http://localhost.hackthissite.com
[+] Discovered subdomain -->  http://webmail.hackthissite.com
[+] Discovered subdomain -->  http://webdisk.hackthissite.com
[+] Discovered subdomain -->  http://ftp.hackthissite.com
[+] Discovered subdomain -->  http://pop.hackthissite.com
...
```
If you want to output the discovered URLs to a file:
```
python3 scanner.py hackthissite.com  -t 10 -o discove.txt
```
This will create a new file `discove.txt` that includes the discovered subdomains.
