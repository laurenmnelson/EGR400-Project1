import platform
import datetime
import os


class Logger:
    def __init__(self, logfile):
        self.logfile = logfile

        # TODO: Verify logfile is not itself a directory
        if os.path.isdir(logfile):
            raise Exception("The path for the log file must be a file, not a directory.")
        # TODO: Verify directory exists (note file not needed)
        folder = os.path.dirname(logfile)
        if not os.path.dirname(folder):
            raise Exception("The folder for the log file does not exist.")

    def log(self, msg):
        machine = platform.node()
        now = datetime.datetime.now()
        date = "{0}_{1}_{2} {3}:{4}:{5}".format(
            now.year, now.month, now.day,
            now.hour, now.minute, now.second)

        text = "{0}/{1}: {2}".format(machine, date, msg)
        # TODO: Print to console
        print("    log=" + text)
        # TODO: Append line to log file
        with open(self.logfile, 'a+') as file_out:
            file_out.write("{0}\n".format(text))
