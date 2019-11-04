import requests
import urllib.request
from lxml import html
import argparse


"""Wallpaper Downloader"""


def image_downloader(year, month, resolution):

    if month == "01":             # Update month to 12 bcs of Url
        updated_month = "12"
        updated_year = str(int(year)-1)
    else:
        updated_month = str(int(month)-1)
        if len(updated_month) == 1:   # Changing Url to fit in Url
            updated_month = "0" + updated_month
        updated_year = year



    month_name = {	'01' : 'january', '02' : 'february','03':'march',
	                '04': 'april', '05': 'may', '06': 'june', '07': 'july',
                    '08': 'august', '09': 'september', '10': 'october',
                    '11': 'november', '12': 'december'}                  # Easy way to put month name

    url = "https://www.smashingmagazine.com/{}/{}/desktop-wallpaper-calendars-{}-{}/"\
        .format(updated_year, updated_month, month_name[month], year)       # format Url based on SmashingMagazine

    resp = requests.get(url)

    content = html.fromstring(html=resp.text)

    current_url_selection = "//a[contains(text(),'{}')]/@href".format(resolution)   # Selecting Required Image Links

    wallpaper_links = content.xpath(current_url_selection)

    for i in range(0, len(wallpaper_links)):
        img_title = wallpaper_links[i].split("/")   # Splitting Url to get image name
        urllib.request.urlretrieve(wallpaper_links[i],img_title[-1])
        print("[*] Image Downloaded: {}".format(img_title[-1]))    # Printing Downloaded Image Name
    print("--------------------------------------------------------")
    print("------------Image Downloading COMPLETED ---------------")


# Python CLI Development
if __name__ == "__main__":

    parser = argparse.ArgumentParser\
        (prog="Wallpaper Downloader from www.smashingmagazine.com",
        usage="Provide three arguments(year month resolution) ex: 2019 06 800x600",
        description="Description : This program Automates Downloading Images with required Resolution",
        epilog="Developed by : Ganijon Toshtemurov \n\n\nExecution Example downloader.py 2019 04 800x600",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=True)
    parser.add_argument("year", type=str, help="Enter Year, ex: '2019' ", metavar="Year(yyyy)")
    parser.add_argument("month", type=str, help="Enter Month, ex: '06' ", metavar="Month(mm)")
    parser.add_argument("resolution", type=str, help="Enter Resolution, ex: '800x600' ", metavar="Resolution")

    args = parser.parse_args()

    image_downloader(args.year, args.month, args.resolution)











