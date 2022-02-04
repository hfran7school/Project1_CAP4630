# Project1_CAP4630 (Spring 2022)
CAP4630 Project 1 -- Python Basics
 * @author Hailey Francis (n01402670@unf.edu)
 * @version February 3, 2022

Project1.py
  * This program will take States.csv
    and create a list of State objects that
    contain information about each state in
    the file.
    The user will be able to select from 5
    different option: printing a report, 
    sorting the States by either name or
    case fatality rate, searching for a 
    specific state's information, and
    giving a Spearman's rho matrix based
    on the data.
  
 State.py
  * This module contains the class State
    and its subsequent functions, including
    an initializer, getter&setter methods,
    a __str__ method and a __gt__ method.

    The __str__ method prints the state's
    information to be formatted properly when
    printing reports in the main project.

    __gt__ is used to compare the states based
    on their names.

Notes:
  * This program is hardcoded to read the file "States.csv"
  * This program expects States.csv to have a header -- it removes the first object from the list, presuming its the     header, upon list creation. *(See Project1.py line 28)*
