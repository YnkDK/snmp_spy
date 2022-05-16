Feature: Lunch the command-line interface from SNMP walk capture

  Scenario: Listing all objects after the lunch
    Given an SNMP walk output
    When the command-line interface is lunched
    Then all objects are shown