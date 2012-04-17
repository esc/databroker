    --- Databroker Tools ---

Databroker tools are a package of tools for editing Netrunner deck
files. The package has been created by esc and documented by photon79.

            ---
    Deck taxonomy file structure

Title:
<title, e.g.: My best runner deck>

Format:
<format, e.g. Revised, 15>

Author:
<author's name, e.g..: Neal>

Date:
<unformatted date stamp, or just year>

Deck list:
<number of copies followed by space and the card name>
<number of copies followed by space and the card name> ....

Description:
<some explanatory text>

            - OR -
Theme:
<theme, e.g.: Tag‘n‘bag>

Tournament:
<name of the corresponding tournament>

Player:
<author's name, e.g..: Neal>

Deck list:
<number of copies followed by space and the card name>
<number of copies followed by space and the card name> ....

[Description: ]
<some explanatory text>

            ---
            Tools

converter.py is applied onto a directory and recursively converts the
deck files with that structure into a format compatible to gccg,
i.e. a list of card names only, the remaining lines will be prefixed
with a hash # which is the comment symbol for the gccg parser.

Exemplary usage:
> python converter.py <directory name>


gccg_parser.py is applied on a single file and compares occurances of
numbers followed by names at the start of a line with names in the xml
card data base (/gccg_data/). Its output is a list of those names that
have no exact match.

Exemplary usage on a whole directory recursively:
> find taxonomy -type f | while read line ; do python gccg_parser.py $line; done;

Make sure that you use a shell that can handle white space in names
properly, for example zsh.


mws_parser.py is yet to be described.
