import argparse

def delete_file(Ukey):
    f = open('url.txt', 'r')
    lines = f.readlines()
    f.close()
    f = open('url.txt', 'w')
    for line in lines:
        if Ukey not in line:
            f.write(line)
    
    f.close()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--add", help="Add URL", action='store_true')
    parser.add_argument("-d","--delete", help="Remove URL", action='store_true')
    parser.add_argument("-k","--key", help="Folder")
    parser.add_argument("-u","--url", help="File")
    args = parser.parse_args()

    if args.add:
        f = open('url.txt', 'a')
        f.write(f'{args.key}|{args.url}\n')
    if args.delete:
        find_key = args.key + "|"
        delete_file(find_key)

main()
