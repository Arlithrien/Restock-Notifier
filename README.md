# Restock-Notifier
A series of python scripts designed to monitor website marketplaces for particular online goods. A push notification is send to the user if a watched item is restocked under a designated price threshold. The BeautifulSoup library is used to scrape websites. Notify-run is used to send device notifications.

Ammoseek
----------
Scrapes prefiltered ammoseek search queries to find the current cheaper Cost Per Round (CPR) of the of a set firearms caliber. The current configuration parses lowest cpr of the .223 rifle caliber from BassPro and Cabela's. If an item is stocked at a CPR below the set threshold, a push notification will be sent to the user's device(s) displaying the supplying vendor and the cost. The script checks prices every 5 minutes, and upon notification will pause for an hour.


Winn Dixie
----------
Scrapes Winn Dixie's weekly ad for sales. Notifies the user when T-Bone steaks are on sale.
