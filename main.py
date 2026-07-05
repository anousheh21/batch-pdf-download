import argparse
from getUrls import getUrls
from selectWindow import selectWindow
from singlePdfDownload import downloadPdf

parser = argparse.ArgumentParser(
    description="A macOS tool for downloading PDFs from Google Chrome in bulk"
)
parser.add_argument('downloadDestination', help="Directory where PDFs will be downloaded")
args = parser.parse_args()

def main():
    selectedWindow = selectWindow()
    urls = getUrls(selectedWindow)

    for url in urls:
        downloadPdf(url, args)


if __name__ == "__main__":
    main()