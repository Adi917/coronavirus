from bs4 import BeautifulSoup
import requests

def main():
    result = requests.get("https://www.worldometers.info/coronavirus/country/us/")
    src =  result.content
    soup = BeautifulSoup(src, "lxml")

    urls = []
    for number in soup.findAll("div", {"class":"maincounter-number"}):
        urls.append(number.find('span').text)
    # urls[0] = Cases
    # urls[1] = Deaths
    # urls[2] = Recovered

    print("[1] Number of COVID-19 Cases in the United States")
    print("[2] Number of Deaths caused by COVID-19 in the United States")
    print("[3] Number of Recoveries from COVID-19 in the United States")
    print("[4] Quit")
    selection = input("What data would you like to receive today? ")
    if selection == "1":
        print(urls[0])
    elif selection == "2":
        print(urls[1])
    elif selection == "3":
        print(urls[2])
    elif selection == "4":
        exit()
    else:
        print("Incorrect Selection, Try Again.")
    print("\n")

while True:
    main()
