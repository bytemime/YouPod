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

    args = parser.parse_args()
    url = args.url

    if url:
        print(url)

if __name__ == '__main__':
    main()