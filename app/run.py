import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', type=str, required=True)
    parser.add_argument('--research', '-r', action='store_true')
    return parser.parse_args()

# subprocess.run(['source', './bin/activate'])
args = parse_args()
if args.research:
    print('Researching the URL provided...')
    subprocess.run(['python', 'app/scrape.py', '-u', args.url])
    subprocess.run(['python', 'app/preprocess.py', '-u', args.url])

subprocess.run(['python', 'app/q_and_a.py', '-u', args.url])
