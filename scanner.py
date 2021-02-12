#!/usr/bin/env python3

import requests
import argparse
from queue import Queue
from threading import Thread, Lock

q = Queue()
list_lock = Lock()
discovered_domains = []

def scan_subdomains(domain):
    global q
    while True:
        subdomain = q.get()     # Get the subdomain from the queue
        url = f"http://{subdomain}.{domain}"    # Scan the subdomain
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("\033[32m[+] Discovered subdomain\033[0m --> ", url)
            # Add the subdomain to the global list
            with list_lock:
                discovered_domains.append(url)

        q.task_done()

def main(domain, n_threads, subdomains):
    global q
    # Fill the queue with all the subdomains
    for subdomain in subdomains:
        q.put(subdomain)

    for t in range(n_threads):
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Scanner using Threads")
    parser.add_argument("domain", help="Domain to scan for subdomains without protocol (e.g without 'http://' or 'https://')")
    parser.add_argument("-l", "--wordlist", help="File that contains all subdomains to scan, line by line. Default is subdomains.txt",
                        default="subdomains.txt")
    parser.add_argument("-t", "--num-threads", help="Number of threads to use to scan the domain. Default is 10", default=10, type=int)
    parser.add_argument("-o", "--output-file", help="Specify the output text file to write discovered subdomains")
    
    args = parser.parse_args()
    domain = args.domain
    wordlist = args.wordlist
    num_threads = args.num_threads
    output_file = args.output_file

    main(domain=domain, n_threads=num_threads, subdomains=open(wordlist).read().splitlines())
    q.join()

    # Save the file
    with open(output_file, "w") as f:
        for url in discovered_domains:
            print(url, file=f)