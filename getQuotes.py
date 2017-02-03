#Evan Garcia
#Professor Tindall
#CSC 4800
#February 1st, 2017
#This program accesses the Yahoo Finance stock database, and converts a symbol's data into XML format.


import urllib.request, re, string, sys




def ProcessQuotes(strSymbols):
    #Accesses the Yahoo Finance stock database for the stock symbols entered

    strUrl = "http://finance.yahoo.com/d/quotes.csv?f=sd1t1l1bawmc1vj2&e=.csv"
    strUrl = strUrl + strSymbols
    try:
        f = urllib.request.urlopen(strUrl)
    except:
        print("URL access failed:\n" + strUrl + "\n")
        return

    for line in f.readlines():
        line = line.decode().strip()
    print (line + '\n')
    
    formatData(line)


def formatData(data):
   #Accesses certain sections of the string, and prints them out in xml format

   
    print("<stockquote>")
    
    qSymbol = re.search("(?<=\")[a-zA-Z]{1,5}(?=\",)", data)

    if qSymbol != None:
        print("\t<qSymbol>{}</qSymbol>".format(qSymbol.group()))

    qDate = re.search("(?<=,\")[1]?[0-9]/[0-3]?[0-9]/[1-2][09][0-9][0-9](?=\",\")", data)

    if qDate != None:
        print("\t<qDate>{}</qDate>".format(qDate.group()))

    qTime = re.search("(?<=\")[[1]?[0-9]:[0-5][0-9](am)?(pm)?(?=\",)", data)

    if qTime != None:
        print("\t<qTime>{}</qTime>".format(qTime.group()))

    qLastSalePrice = re.search("(?<=\"\,)[1-9]?[0-9]*\.[0-9]+(?=,)", data)

    if qLastSalePrice != None:
        print("\t<qLastSalePrice>{}</qLastSalePrice>".format(qLastSalePrice.group()))
    
    qBidPrice = re.search("(?<=[0-9A]\,)[1-9]?[0-9]*\.[0-9]+(?=,[0-9N])", data)

    if qBidPrice != None:
        print("\t<qBidPrice>{}</qBidPrice>".format(qBidPrice.group()))

    qAskPrice = re.search("(?<=[0-9A]\,)[1-9]?[0-9]*\.[0-9]+(?=,\")", data)

    if qAskPrice != None:
        print("\t<qAskPrice>{}</qAskPrice>".format(qAskPrice.group()))

    q52WeekLow = re.search("(?<=[0-9A]\,\")[1-9]?[0-9]*\.[0-9]+(?= - )", data)

    if q52WeekLow != None:
        print("\t<q52WeekLow>{}</q52WeekLow>".format(q52WeekLow.group()))
    
    q52WeekHigh = re.search("(?<=\- )[1-9]?[0-9]*\.[0-9]+(?=\",[\"N])", data)

    if q52WeekHigh != None:
        print("\t<q52WeekHigh>{}</q52WeekHigh>".format(q52WeekHigh.group()))

    qTodaysLow = re.search("(?<=\",\")[1-9]?[0-9]*\.[0-9]+(?= - )", data)

    if qTodaysLow != None:
        print("\t<qTodaysLow>{}</qTodaysLow>".format(qTodaysLow.group()))
    
    qTodaysHigh = re.search("(?<=\- )[1-9]?[0-9]*\.[0-9]+(?=\",[+-])", data)

    if qTodaysHigh != None:
        print("\t<qTodaysHigh>{}</qTodaysHigh>".format(qTodaysHigh.group()))

    qNetChangePrice = re.search("(?<=,)[+-][1-9]?[0-9]*\.[0-9]+(?=,)", data)

    if qNetChangePrice != None:
        print("\t<qNetChangePrice>{}</qNetChangePrice>".format(qNetChangePrice.group()))

    qShareVolumeQty = re.search("(?<=,)[1-9]?[0-9, ]*(?=,)", data)

    if qShareVolumeQty != None:
        print("\t<qShareVolumeQty>{}</qShareVolumeQty>".format(qShareVolumeQty.group()))
    
    qTotalOutstandingSharesQty = re.search("(\".*\",[+-][^,]*,[^,]*,)([1-9][0-9\, ]*)", data)
    

    #If there is whitespace or commas in the string, remove them.
    if qTotalOutstandingSharesQty != None:
        qTotalOutstandingSharesQty = qTotalOutstandingSharesQty.group(2)

        if ' ' in qTotalOutstandingSharesQty:
            qTotalOutstandingSharesQty = qTotalOutstandingSharesQty.replace(" ", "")

        if ',' in qTotalOutstandingSharesQty:
            qTotalOutstandingSharesQty = qTotalOutstandingSharesQty.replace(",", "")

        print("\t<qTotalOutstandingSharesQty>{}</qTotalOutstandingSharesQty>".format(qTotalOutstandingSharesQty))



    print("</stockQuote>")
    



#Main Function: Have users enter stock symbols
def main():
    while True:
        print("Enter a Stock Symbol: ")
        symbol = sys.stdin.readline().strip()
        if(len(symbol) == 0):
            break
        strSymbols = '&s=' + symbol
        ProcessQuotes(strSymbols)



if __name__ == "__main__":
    main()