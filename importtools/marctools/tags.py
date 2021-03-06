TAGS = {
    "001": u"Control Number - REQUIRED",
    "003": u"Control Number Identifier - REQUIRED",
    "005": u"Date and Time of Latest Transaction - REQUIRED",
    "008": u"""Fixed - Length Data Elements - REQUIRED\r\n/00 - 05 Date of creation\r\n/06 Type of publication date\r\n/07 - 10 Date 1\r\n/11 - 14 Date 2\r\n/15 - 17 Country of publication code\r\n/35 - 37 Language of publication code""",
    "020": u"ISBN",
    "022": u"ISSN",
    "028": u"Publisher Number",
    "040": u"Cataloging Agency - REQUIRED",
    "041": u"Language Codes",
    "082": u"DDC Call Number",
    "100": u"Main Entry - Personal Name",
    "100 $a": u"Personal name",
    "100 $b": u"Numeration",
    "100 $c": u"Words associated with a name",
    "100 $d": u"Dates associated with a name",
    "110": u"Main Entry - Corporate Name",
    "111": u"Main Entry - Meeting Name",
    "111 $a": u"Meeting name entry element",
    "111 $n": u"Number of meeting",
    "111 $d": u"Year of meeting",
    "111 $c": u"Place of meeting",
    "242": u"Translation of Title",
    "245": u"Title Statement",
    "245 $a": u"Title proper",
    "245 $h": u"General medium designator",
    "245 $b": u"Other title information",
    "245 $c": u"Statement of responsibility",
    "246": u"Variant Title",
    "247": u"Former Title",
    "250": u"Edition Statement",
    "254": u"Musical Presentation Statement",
    "255": u"Cartographic Mathematical Data",
    "260": u"Imprint - REQUIRED",
    "260 $a": u"Place of publication",
    "260 $b": u"Publisher/distributor",
    "260 $c": u"Date(s of publication)",
    "300": u"Physical Description",
    "300 $a": u"Extent",
    "300 $b": u"Other physical details",
    "300 $c": u"Dimensions",
    "310": u"Current Publication Frequency",
    "362": u"Dates of Publication and/or Sequential Designation",
    "440": u"Series Statement",
    "440 $a": u"Main series title",
    "440 $x": u"ISSN",
    "440 $v": u"Volume/sequential designation",
    "440 $n": u"and $p Subseries number and title",
    "500": u"General Note",
    "505": u"Formatted contents note",
    "520": u"Summary",
    "600": u"Subject - Personal Name",
    "600 $a": u"Personal name",
    "600 $b": u"Numeration",
    "600 $c": u"Words associated with a name",
    "600 $d": u"Dates associated with a name",
    "600 $x": u"General subdivision",
    "600 $2": u"Source of name",
    "610": u"Subject - Corporate Name",
    "610 $a": u"Corporate name entry element",
    "610 $b": u"Subordinate unit",
    "610 $x": u"General subdivision",
    "610 $2": u"Source of name",
    "611": u"Subject - Meeting Name",
    "611 $a": u"Meeting name entry element",
    "611 $n": u"Number of meeting",
    "611 $d": u"Year of meeting",
    "611 $c": u"Place of meeting",
    "611 $x": u"General subdivision",
    "611 $2": u"Source of name",
    "630": u"Subject - Uniform Title",
    "630 $a": u"Uniform title",
    "630 $x": u"General subdivision",
    "630 $2": u"Source of name",
    "650": u"Subject - Topical Term",
    "650 $a": u"Topical term",
    "650 $x": u"General subdivision",
    "650 $2": u"Source of name",
    "651": u"Subject - Geographic Name",
    "651 $a": u"Geographic name",
    "651 $x": u"General subdivision",
    "651 $2": u"Source of name",
    "700": u"Personal Name",
    "700 $a": u"Personal name",
    "700 $b": u"Numeration",
    "700 $c": u"Words associated with a name",
    "700 $d": u"Dates associated with a name",
    "710": u"Corporate Name",
    "710 $a": u"Corporate name entry element",
    "710 $b": u"Subordinate unit",
    "711": u"Meeting Name",
    "711 $a": u"Meeting name entry element",
    "711 $n": u"Number of meeting",
    "711 $d": u"Year of meeting",
    "711 $c": u"Place of meeting",
    "856": u"Electronic Location and Access",
    "923": u"Local Acquisitions Information",
    "923 $d": u"Invoice date",
    "923 $n": u"Invoice number",
    "923 $s": u"Source code",
}

def meaning(tag, subfield=""):
    if subfield:
        key = "%s $%s" % (tag, subfield)
    else:
        key = tag
    return TAGS.get(key, u"")
    