#!/usr/bin/env python

from __future__ import absolute_import

import pkg_resources
import sys;
import click
import utils.logger as logger
import scrennshot as ss

VERSION = 1 #pkg_resources.require("webshot")[0].version  

def debug_logging(verbose):
    pass

@click.command()
@click.option('--filepath',  prompt='Give your input file path of URLs to tests', help='Add a path containing list of URLs to test')
@click.option('--divclass', help='If you want to take screenshot of particular div on your page, use this option')
def webshot(filepath, divclass):  # pragma: no cover
    logger.log_r("filepath got initialized : " + filepath)
    ss.execute(filepath, 20)

if __name__ == '__main__':  # pragma: no cover
    webshot()