import sys
import streamlit
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "web_page.py"]
    sys.exit(stcli.main())
