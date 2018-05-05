{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from xml.etree.ElementTree import ElementTree\n",
    "from datetime import datetime\n",
    "import time\n",
    "from sys import argv\n",
    "import json\n",
    "tree = ElementTree()\n",
    "if (len(argv) < 3):\n",
    "    print \"specify an input & output filename, and year. input is osm, output is geojson\"\n",
    "    exit()\n",
    "tree.parse(argv[1])\n",
    "geojson = { \"type\": \"FeatureCollection\", \"features\": [] }\n",
    "nodeidx = {}\n",
    "print 'mapping nodes'\n",
    "for n in tree.iterfind('node'):\n",
    "    if (n.attrib.has_key('user')):\n",
    "        pt = {\n",
    "            \"type\": \"Feature\",\n",
    "            \"geometry\": {\n",
    "                \"type\": 'Point',\n",
    "                \"coordinates\": [float(n.attrib['lon']), float(n.attrib['lat'])]\n",
    "            },\n",
    "            \"properties\": {\n",
    "                \"user\": n.attrib['user'],\n",
    "                \"version\": n.attrib['version'],\n",
    "                \"timestamp\": time.mktime(datetime.strptime(n.attrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ').utctimetuple())\n",
    "            }\n",
    "        }\n",
    "        geojson['features'].append(pt)\n",
    "json.dump(geojson, open(argv[2], 'w'))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
