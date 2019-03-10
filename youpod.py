import argparse

def main():

    parser = argparse.ArgumentParser(
        prog = 'youpod.py',
    	description = 'A lightweight CLI based tool to turn YouTube channels you like \
    	into downloadable podcasts.',
    	epilog = 'There are lots of YouTube videos you could enjoy listening to right \
    	in your terminal!')
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s v0.1.0',  help = 'display version')
    parser.add_argument('-d', dest = 'url', action = 'store', help = 'download audio directly from given URL')
    parser.add_argument('-l', '--list', dest = 'list_podcasts' ,action = 'store_true', help = 'list all downloaded podcasts')
    parser.add_argument('-rm', dest = 'name', action = 'store', help = 'delete podcast (use "all" to delete all podcasts)')
    
    args = parser.parse_args()
    url = args.url
    rm = args.name
    ls = args.list_podcasts
    
    if url:
        print(url)
    if rm:
        print(rm)
    if ls:
        print(ls)

if __name__ == '__main__':
    main()