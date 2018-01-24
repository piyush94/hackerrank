if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        actual_time = input()
        actual_time_list = list(actual_time)
        if actual_time[8:] == 'AM':
            if int(actual_time[:2]) == 12:
                actual_time_list[:2] = '00'
        else:
            if actual_time[:2] != '12':
                actual_time_list[:2] = str(int(actual_time[:2]) + 12)
        actual_time = ''.join(actual_time_list)
        print(actual_time[:8])
