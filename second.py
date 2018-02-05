
def convert_seconds(s):
    hour = int(s)//3600
    minute = int(s) % 3600 // 60
    second = s - hour * 3600 - minute * 60
    if hour == 1:
        if minute == 1:
            if second == 1:
                return str(hour) + ' hour' + ',' + str(minute) + ' minute' + ',' + str(second) + ' second'
            else:
                return str(hour) + ' hour' + ',' + str(minute) + ' minute' + ',' + str(second) + ' seconds'
        else:
            if second == 1:
                return str(hour) + ' hour' + ',' + str(minute) + ' minutes' + ',' + str(second) + ' second'
            else:
                return str(hour) + ' hour' + ',' + str(minute) + ' minutes' + ',' + str(second) + ' seconds'
    else:
        if minute == 1:
            if second == 1:
                return str(hour) + ' hours' + ',' + str(minute) + ' minute' + ',' + str(second) + ' second'
            else:
                return str(hour) + ' hours' + ',' + str(minute) + ' minute' + ',' + str(second) + ' seconds'
        else:
            if second == 1:
                return str(hour) + ' hours' + ',' + str(minute) + ' minutes' + ',' + str(second) + ' second'
            else:
                return str(hour) + ' hours' + ',' + str(minute) + ' minutes' + ',' + str(second) + ' seconds'

def convert_bit(size,unit):
    if unit == 'kB':
        return size * 2 ** 10 * 8
    elif unit == 'kb':
        return size * 2 ** 10
    elif unit == 'Mb':
        return size * 2 ** 20
    elif unit == 'MB':
        return size * 2 ** 20 * 8
    elif unit == 'Gb':
        return size * 2 ** 30
    elif unit == 'GB':
        return size * 2 ** 30 * 8
    elif unit == 'Tb':
        return size * 2 ** 40
    elif unit == 'TB':
        return size * 2 ** 40 * 8

def download_time(file,f_unit,band,b_unit):
    a = convert_bit(file,f_unit)
    b = convert_bit(band,b_unit)
    return convert_seconds(a/b)


print(download_time(1024,'kB', 1, 'MB'))