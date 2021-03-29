#!/usr/bin/python3

import dbus.service
import clipboard
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from datetime import datetime, timezone

DBusGMainLoop(set_as_default=True)

objpath = "/epochreadable"

iface = "org.kde.krunner1"


class Runner(dbus.service.Object):
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.service.BusName("org.kde.epochreadable", dbus.SessionBus()), objpath)

    @dbus.service.method(iface, in_signature='s', out_signature='a(sssida{sv})')
    def Match(self, query: str):
        """This method is used to get the matches and it returns a list of tupels"""
        if query.isdigit():
            parsedZTime = datetime.fromtimestamp(int(query) / 1000.0, timezone.utc);
            zTime = parsedZTime.isoformat(timespec='milliseconds')
            asLocalTime = parsedZTime.astimezone()
            localTime = asLocalTime.isoformat(timespec='milliseconds')
            localTz = asLocalTime.tzname()
            # data, text, icon, type (Plasma::QueryType), relevance (0-1), properties (subtext, category and urls)
            return [(zTime, zTime, "clock", 100, 1.0, {'subtext': 'UTC'}), (localTime, localTime, "clock", 100, 1.0, {'subtext': localTz})]
        return []

    @dbus.service.method(iface, out_signature='a(sss)')
    def Actions(self):
        # id, text, icon
        return [("epochreadable", "Convert Epoch Millis to UTC and local", "clock")]

    @dbus.service.method(iface, in_signature='ss')
    def Run(self, data: str, action_id: str):
        clipboard.put(data)


runner = Runner()
loop = GLib.MainLoop()
loop.run()

#def main():
#    print(Runner().Match("1617043619"))

#if __name__ == "__main__":
#    main()
