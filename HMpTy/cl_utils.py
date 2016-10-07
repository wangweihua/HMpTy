#!/usr/local/bin/python
# encoding: utf-8
"""
Documentation for HMpTy can be found here: http://HMpTy.readthedocs.org/en/stable

Usage:
    hmpty table <tableName> <primaryIdCol> <raCol> <decCol> -s <pathToSettingsFile>
    hmpty table --host=<host> --user=<user> --passwd=<passwd> --dbName=<dbName> <tableName> <primaryIdCol> <raCol> <decCol> [-s <pathToSettingsFile>]

    COMMANDS
    ========
    table                 add HTMids to database table

    ARGUMENTS
    =========
    tableName             name of the table to add the HTMids to
    primaryIdCol          the name of the unique primary ID column of the database table
    raCol                 name of the talbe column containing the right ascension
    decCol                name of the talbe column containing the declination
    host                  database host address
    user                  database username
    passwd                database password
    dbName                database name

    FLAGS
    =====
    -h, --help            show this help message
    -s, --settings        the settings file
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
from docopt import docopt
from fundamentals import tools, times
from HMpTy.mysql import add_htm_ids_to_mysql_database_table
# from ..__init__ import *


def main(arguments=None):
    """
    *The main function used when ``cl_utils.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="DEBUG",
        options_first=False,
        projectName="HMpTy",
        tunnel=False
    )
    arguments, settings, log, dbConn = su.setup()

    # tab completion for raw_input
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(tab_complete)

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        if arg[0] == "-":
            varname = arg.replace("-", "") + "Flag"
        else:
            varname = arg.replace("<", "").replace(">", "")
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    ## START LOGGING ##
    startTime = times.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE cl_utils.py AT %s' %
        (startTime,))

    # CALL FUNCTIONS/OBJECTS
    if table:
        add_htm_ids_to_mysql_database_table(
            raColName=raCol,
            declColName=decCol,
            tableName=tableName,
            dbConn=dbConn,
            log=log,
            primaryIdColumnName=primaryIdCol
        )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE cl_utils.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return


if __name__ == '__main__':
    main()
