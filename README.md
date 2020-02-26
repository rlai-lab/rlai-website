## Code for rlai.ualberta.ca

1. Install miniconda (3.7)
2. Install gunicorn and pyyaml
3. Install google API tools
4. Install flask
5. Clone website repo

To run the server, execute:
``` bash
gunicorn -w 2 -b 0.0.0.0:80 server:app
```
