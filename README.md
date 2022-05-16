# SNMP Spy
> Spies are stubs that also record some information based on how they were called.
> - Martin Fowler

This is a Simple Network Management Protocol (SNMP) service that records when it last 
sent a response and the ability to change the values for each object identifier (OID).

When monitoring network connected devices that expose the SNMP it can be troublesome 
to test scenarios where the devices are misbehaving - which is exactly why we monitor 
them!

## Usage

This SNMP spy exposes multiple ways on how to spy on the SNMP monitoring tool. It can
act as a full-blown host that can run for as long as needed. It can spawn and kill the
host within a very short period of time. It exposes three interfaces:
1) A webinterface to create, maintain, and delete one or more hosts,
2) A command-line interface to create, maintain, and delete a single host, and
3) A Python module that can be invoked as any other module

### Webinterface

TODO

### Command-line interface

TODO

### Python module

TODO

## Installation

TODO

## Examples

TODO

## License

[Apache 2.0](/LICENSE)