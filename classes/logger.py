#Written by @Cosm00_
#Stay Based Youngins...

import time, os

class logger:
        def __init__(self):
                self.string = '[{}]\033[3{}m {}\033[0m'
                os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
                time.tzset()
        def log(self, msg, code):
                code = code.lower()
                string = self.string.format(time.strftime('%X %Z'), '{}', str(msg))
                if code == 'red':
                        print string.format('1')
                elif code == 'green':
                        print string.format('2')
                elif code == 'yellow':
                        print string.format('3')
                elif code == 'purple':
                        print string.format('4')
                elif code == 'magenta':
                        print string.format('5')
                elif code == 'cyan':
                        print string.format('6')
                elif code == 'white':
                        print string.format('7')
                elif code == 'rain' or code == 'rainbow':
                        print self.rainbow(msg)
                else:
                        return(raw_input(string.format('3')))

        def rainbow(self, msg):
                length = len(msg) - 1
                count = 0
                colorstring = '\033[3{}m'
                passstring = time.strftime('[%X %Z] ')
                rainbow = {'1':'1','2':'3','3':'2','4':'4','5':'5'}
                raincount = 1
                while count < length:
                        if raincount == 6:
                                raincount = 1
                        if msg[count:count + 1] == ' ':
                                passstring = passstring + ' '
                                count = count + 1
                        else:
                                passstring = passstring + colorstring.format(rainbow[str(raincount)]) + msg[count:count + 1]
                                count = count + 1
                                raincount = raincount + 1
                if raincount == 6:
                    raincount = 1
                passstring = passstring + colorstring.format(rainbow[str(raincount)]) + msg[len(msg) - 1:] + '\033[0m'
                return(passstring)



if __name__ == '__main__':
        log = logger().log
        log('Written By @Cosm00_', 'green')
        log('Stay Based Youngins', 'purple')
        log('  _            _                ', 'rain')
        log(' (_)          | |               ', 'rain')
        log('  _  ___  __ _| |_ __ _ ___ ___ ', 'rain')
        log(' | |/ _ \/ _` | __/ _` / __/ __|', 'rain')
        log(" | |  __/ (_| | || (_| \__ \__ \"", 'rain')
        log(' |_|\___|\__,_|\__\__,_|___/___/', 'rain')
