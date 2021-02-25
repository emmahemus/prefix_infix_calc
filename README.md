# Prefix &amp; Infix Calculator
This repo contains functions to perform prefix and infix calculations, defined in kheiron.py. 

## Requirements
The repo runs python version 3.7.4, and contains a requirements.txt file. 

## RESTful interface
Flask was used to create a simple interface, as defined in app.py. Example requests for the prefix and infix calculators are included in example_requests.py.

## Areas to improve:
- expand unit tests to cover RESTful interface
- use html to create interactive hosted interface (something with buttons/user input functionality)
- validity check:
  - the primary issue with both the prefix and infix calculators is that they don't properly handle user input errors/illegal operations (eg "+ + 3" in prefix)
  - I started to write a function (validity_check) for the infix calculator to catch all such exceptions, but it is flawed and does not catch them all. If I had more time I would re-work this so that all invalid inputs were filtered out. 
  - there is no such function for the prefix calculator, which is why one of the unit tests fails (ideally I would catch such an error and the test could be changed accordingly)
- I suspect there is probably a cleaner way to do the infix calculation
