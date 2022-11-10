import csv 
import requests
import json
def check(ip):
    result = requests.get("https://api.abuseipdb.com/api/v2/check", headers = {"Accept": "application/json","Key": apikey2}, params = {"ipAddress": ip}).json()
    try:
        if result["data"]["totalReports"] > 1:
            print(f'{result["data"]["ipAddress"]}','=',f'[{result["data"]["countryCode"]}]','-',f'Times Reported: {result["data"]["totalReports"]}','-',f'Confidace: {result["data"]["abuseConfidenceScore"]}%','-',f'Last Report: {result["data"]["lastReportedAt"]}',f'(https://www.abuseipdb.com/check/{ip})')
        else:
            print(ip, "=",f'[{result["data"]["countryCode"]}]'," Ip is clear!")
    except:
        pass
    try:
        if result["errors"][0]["detail"] == "The ip address must be a valid IPv4 or IPv6 address (e.g. 8.8.8.8 or 2001:4860:4860::8888).":
            print(ip,"="," Invalid IP!")
    except:
        pass
apikey = input("Please enter an API key\n")
if apikey == "":
    print(f"API key invalid")
    exit()
mode = input("Enable Bulk Check? (.csv file) [true,false]\n").lower()
if mode == "true":
    print("Bulk Mode")
    filepath = str(input("Please enter an filepath to .csv file\n"))
    filepath1 = "/home/ubuntu/PROJEKTY/ABUSEIP-BulkChecker/db.csv"
    rows = []
    with open(filepath1, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
            ip = str(row[0])
            check(ip)
else:
    print("Single Mode")
    ip = input("Enter an IP Adress\n")
    print("Checking an IP...\n-------------\n")
    check(ip)

#python3 run.py
