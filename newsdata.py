#!/usr/bin/env python
#
# newsdata.py -- helper module for newsstats.py reporting tool
#
import psycopg2
import sys


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect(database="news")
    except:
        print ("You could not connect to the news database. Please check\
         check your connection and try again.")


def execute_query(query):
    """execute_query takes an SQL query as a parameter.Executes the query\
     and returns the results as a list of tuples.
       args:
           query - an SQL query statement to be executed.

       returns:
           A list of tuples containing the results of the query.
    """
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(query)
        ans = cur.fetchall()

        conn.close()  # don't leave links to the db open!
        return ans

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def artRank():
    """Returns a list of articles, sorted by page views, descending.

    The first entry in the list should be the article with the most views.

    Returns:
      A list of tuples, each of which contains (title, visits):
        title: the full title of the article
        visits: the number of pageviews that article has received
    """
    query = "select title, visits from art_rank LIMIT 3;"

    ans = execute_query(query)
    return ans


def authRank():
    """Returns a list of authors, sorted by pageviews.

    The first entry in the list should be the author with the most pageviews.

    Returns:
      A list of tuples, each of which contains (name, page_views):
        name: the full name of the author
        visits: the sum of the number of pageviews across all articles for
        that particular author
    """
    query = "select * from auth_rank LIMIT 3;"

    ans = execute_query(query)
    return ans


def onePercentErrorDay():
    """Returns a list of days, sorted by the percentage error rates on http
     requests for that particular day, descending.

    The first entry in the list should be the day with the highest percentage
    of page errors relative to total page requests during that day.

    Returns:
      A list of tuples, each of which contains (date, percent_errors):
        date: in full date form
        percent_errors: the percentage of http requests that resulted in
        an errors on that day.
            ***NOTE This only catches 404 errors at this time**
    """
    query = "select day, percent_errors from log_status_rank;"

    ans = execute_query(query)
    return ans
