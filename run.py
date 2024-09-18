import sys
import os

# Add 'punchcard/src' to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'punchcard', 'src'))

from punchcard.app import PunchcardApp

def main():
    app = PunchcardApp('Punchcard System', 'com.example.punchcard')
    app.main_loop()

if __name__ == '__main__':
    main()

from punchcard.src.app import PunchcardApp


def main():
    app = PunchcardApp('Punchcard System', 'com.example.punchcard')
    app.main_loop()

if __name__ == '__main__':
    main()
