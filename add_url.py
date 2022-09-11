import argparse

def delete_link(Ukey):
    f = open('url.txt', 'r')
    lines = f.readlines()
    f.close()
    f = open('url.txt', 'w')
    for line in lines:
        if Ukey not in line:
            f.write(line)
    f.close()

def add_link(link):
    f = open('url.txt', 'a')
    f.write(f'{link}\n')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--add", help="Add URL", action='store_true')
    parser.add_argument("-d","--delete", help="Remove URL", action='store_true')
    parser.add_argument("-k","--key", help="Key for link")
    parser.add_argument("-u","--url", help="URL")
    args = parser.parse_args()

    if args.add:
        add_link(f'{args.key}|{args.url}')
    if args.delete:
        delete_link(args.key + "|")

main()
