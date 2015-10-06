# search

Processing for HTML dumps.

## Functions

### search.py

Searches them compressed dumps for keys.

Features:

#### search archive files

    Search is case-insensitive.

    Maintains sanity by comparing to a black-list 
    as well as being lazy. 

    Used for lead-generation, statistics, and shrinking database.

    ----------

    Text Search:

    Returns whether a key-word is in a string.

    -----

    URL Search:

    Finds a keyword and returns string up-until the next apostrophe.

    Will not return a string over 256 characters.

    -----

    *this_is_a_song_without_words

    Suggest a better name and if I accept your answer 
    I'll send you some Litecoin or Bitcoin!

#### benchmarking

    Test functionality on N files.
    Predicts execution time for whole database.

    -----

    ToDO:

    - Pre-compile list of random-N files.
    - Move starts time inside loop.

#### testing

    Test N-random files.

    -----

    ToDO:

    - Smart debugging / error-reporting.

## Modules

### keys.py

    Dictionary-like JSON interface for keys and options.*

*options actually isnt finished yet

### /process

#### Dirs:

/json
    
    dumps for jsondb

/txt

    plain-text dumps for read-ability

#### Files:

01.py

    processes /dumps/01*

03.py

    processes /dumps/03*

*too domain-specific